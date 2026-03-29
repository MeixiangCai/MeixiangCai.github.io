#项目目标是创建一个完整的数据分析Agent，并且自动发送报告到邮箱
from langchain_openai import ChatOpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
import json
import matplotlib.pyplot as plt
from langchain.tools import tool

#定义相关绘图函数
def setup_plot():
    """全局绘图配置（字体、画布、样式）"""
    plt.rcParams["font.sans-serif"] = ["Arial Unicode MS"]  # 中文字体
    plt.rcParams["axes.unicode_minus"] = False  # 正常显示负号
    plt.figure(figsize=(8, 5))  # 统一画布大小
    plt.grid(True, linestyle="--", alpha=0.5)  # 默认网格线


def ensure_dir(path):
    import os
    """确保保存目录存在"""
    # 提取出文件所在的文件夹路径
    dir_name = os.path.dirname(path)
    # 如果文件夹不存在，就自动创建
    if dir_name and not os.path.exists(dir_name):
        os.makedirs(dir_name)


def draw_chart(data):
    """ 根据AI给出的数据绘制图表
    data：{
        chart_type: "bar" | "line" | "scatter"
        "x": [...],
        "y_series": {"系列1": [...], "系列2": [...]},
        "title": "标题",
        "xlabel": "X轴名",
        "ylabel": "Y轴名"
    }
    """
    # 绘图全局设置：中文字体、画布大小、网格线等；
    setup_plot()
    # 根据标题生成图像保存路径，例如 artifacts/销售趋势.png
    save_path = f"artifacts/{data.get('title','default_chart')}.png"
    # 检查文件目录是否存在
    ensure_dir(save_path)

    # 从data中提取图表类型、x轴数据与y轴数据
    chart_type = data.get('chart_type','line')
    x = data.get("x",[])
    y_series = data.get("y_series",{})
    if not x or not y_series:
        print("⚠️ 数据缺失，无法绘图:", data)
        return ""
    '''根据不同的类型绘图'''
    # 当需要绘制柱状图时
    if chart_type == "bar":
        # 计算每组柱子的宽度，使多组柱状图不会重叠
        width = 0.8 / len(y_series)
        # 使用 enumerate 遍历每个系列（例如“用户数”“转化率”）
        for i, (label, y_values) in enumerate(y_series.items()):
                        # 对齐长度，避免 x 和 y 长度不一致导致报错
            min_len = min(len(x), len(y_values))
            x_aligned = x[:min_len]
            y_aligned = y_values[:min_len]
            plt.bar(
                [p + i * width for p in range(len(x_aligned))],
                y_aligned,
                width=width,
                label=label
            )
        # 设置 X 轴的刻度标签，使它们与每组柱子的中心位置对齐
        plt.xticks([p for p in range(len(x))], x)

    # 当需要绘制折线图时
    elif chart_type == "line":
        for label, y_values in y_series.items():
            min_len = min(len(x), len(y_values))
            x_aligned = x[:min_len]
            y_aligned = y_values[:min_len]

            plt.plot(
                x_aligned,
                y_aligned,
                marker="o",
                label=label
            )
    # 当需要绘制散点图时
    elif chart_type == "scatter":
        for label, y_values in y_series.items():
            min_len = min(len(x), len(y_values))
            x_aligned = x[:min_len]
            y_aligned = y_values[:min_len]

            plt.scatter(
                x_aligned,
                y_aligned,
                label=label
            )

    else:
        # 无法生成图表的数据返回空字符串
        return ''

    '''设置通用的图表样式'''
    # 设置图表标题
    plt.title(data.get("title", "数据分析图表"))
    # 设置 X 轴标题
    plt.xlabel(data.get("xlabel", "X轴"))
    # 设置 Y 轴标题
    plt.ylabel(data.get("ylabel", "Y轴"))
    # 显示右上角的图例，用于区分不同数据系列
    plt.legend()
    # 自动调整边距，让图表元素不会被裁剪
    plt.tight_layout()
    # 将绘制好的图表保存为 PNG 图片
    plt.savefig(save_path, dpi=144, bbox_inches="tight")
    plt.show()
    # 关闭当前图表窗口
    plt.close()
    # 返回图像的保存路径，方便后续报告引用
    return save_path

PROMPT_TEMPLATE='''
你扮演“数据分析助理”。你只能对注入的 Pandas DataFrame `df` 进行只读分析，不得直接绘图。
- 如需派生请使用副本（例如 `tmp = df.copy()`）。
- 除了源数据的字段名、数据内容外，所有描述内容均使用中文作答。
- 最终仅返回**一个合法 JSON**，不可有额外文本或符号（包括但不限于```）。


【统一返回 JSON 结构】

{
  "data": {
    "chart_type": "line or bar or scatter",
    "x": [],
    "y_series": {
      "系列1": []
    },
    "title": "图表标题",
    "xlabel": "X轴名称",
    "ylabel": "Y轴名称"
  }
}
'''
def data_analyze_agent(csv_path,user_query):
    model=ChatOpenAI(
        api_key="sk-ae518d28b0b144179862cccbe5594daa",
        model="deepseek-chat",
        base_url="https://api.deepseek.com",
        response_format={"type":"json_object"} #注意这里是让AI以JSON形式输出回答
    )
    #准备数据
    import pandas as pd
    df=pd.read_csv(csv_path)
    #使用langchain的内置agent
    agent=create_pandas_dataframe_agent(
        llm=model,
        verbose=False,
        df=df,
        agent_type="tool-calling",
        allow_dangerous_code=True
    )
    raw=agent.invoke({"input":PROMPT_TEMPLATE+user_query})
    answer=json.loads(raw.get("output",{}))
    chart_paths=draw_chart(answer.get("data",{})) #调用draw_chart绘图函数
    answer["chart_paths"]=chart_paths
    return answer

#尝试调用该数据分析agent
file_path="/Users/xiaoxiao/Downloads/14/data/销售数据.csv"
query="按[月份]与[品类]统计月度收入，生成一张多折线图（x 轴为月份，y 轴为收入，多条线代表不同‘品类’），用于观察 2025 年 1–8 月的趋势变化。"
answer=data_analyze_agent(file_path,query)
print(answer)

'''#测试agent解决问题的能力
user_query="请统计2025年上半年（1–6 月）各销售员的平均单笔利润与总销售额，并按从高到低排序返回前5名"
ret=agent.invoke({"input":user_query})
print(ret["output"])
#让AI直接上手画图
user_query2="按月份与品类统计月度收入，画一张多折线图（x 轴为月份，y 轴为收入，多条线代表不同‘品类’），用于观察 2025 年 1–8 月的趋势变化。将生成的图表保存在本地文件夹 'artifacts' 中"
ret2=agent.invoke({"input":user_query2})
print(ret2["output"])
#让AI提供用于绘图的数据，再编写函数绘图
user_query3="按月份与品类统计月度收入，生成绘制折线图所需的数据（x 轴为月份，y 轴为收入，多条线代表不同‘品类’），用于观察 2025 年 1–8 月的趋势变化。要求使用JSON生成以下结构的数据："
ret3=agent.invoke({"input":user_query3})'''

#让AI做好数据分析后，需要让它发送分析报告
analysis_log=[] #存储分析结果列表
csv_path="/Users/xiaoxiao/Downloads/14/data/lesson_data.csv"
user_query="给出全月规模与转化概况，按月汇总 PV/UV/Trial/Add/Pay/Refunds，生成核心漏斗图表与转换率标注数据。"
#调用数据分析agent
answer=data_analyze_agent(csv_path, user_query)
analysis_log.append(answer)
#继续处理剩下两个需求
user_query="分析自然/广告/社媒贡献度与效率？给出 自然流量pv_organic/广告流量pv_ads/社媒流量pv_social 的总计与占比，生成堆叠柱形数据。"
answer=data_analyze_agent(csv_path,user_query)
analysis_log.append(answer)
user_query="英语/IT/AI/通识哪类更强？按 category 聚合 ，计算完课率：sum(completions)/sum(starts)，生成分组柱形图数据"
answer=data_analyze_agent(csv_path,user_query)
analysis_log.append(answer)

#创建用于编写数据分析报告的AI
from langchain_openai import ChatOpenAI
llm=ChatOpenAI(
    api_key="security_code",
    model="deepseek-chat",
    base_url="https://api.deepseek.com",
    response_format={"type":"json_object"}
)
from langchain.prompts import ChatPromptTemplate
prompt = """
你是一名资深数据分析报告专家。你的任务是：  
根据用户传入的 **json 列表**（每个元素包含数据分析结果），将信息汇总并撰写成一份 **结构化报告**。  

【输入说明】  
- 输入是一个由多个 json 组成的列表；  
- 每个 json 至少包含：  
  - type：数据类型（例如 chart、table）  
  - input：用户任务描述  
  - data：包含 summary、指标、分析结论等  
  - chart_paths：图表文件路径（可选）  
  - export_paths：导出的数据表路径（可选）  

【输出要求】  
输出必须是一个 JSON 对象，严格符合以下结构：  
{{
    "subject": "<报告的总标题>",  
    "content_html": "<报告的完整HTML内容>", 
    "attachments": ["<附件地址1>", "<附件地址2>", ...]
}}

【content_html 生成规则】  
必须严格按照以下 HTML 层次生成：  

<h1> [总标题] </h1>

<h2> [小标题] </h2>  
<p> [内容概括，来自该 json 的 summary] </p>  

<h3>数据标题1</h3>  
<table>
  <tbody>
    [逐行列出核心指标及其数值]
  </tbody>
</table>  

<h3>数据标题2</h3>  
<table>
  <tbody>
    [逐行列出核心指标及其数值]
  </tbody>
</table>  

<h3>分析结论</h3>  
<p>[简明总结趋势、问题与亮点]</p>  

<h3>附件</h3>  
<p>[列出该 json 对应的 chart_paths 和 export_paths]</p>  

【参考示例】  
输入 json：  
{{
 'type': 'chart_data',
 'input': '给出全月规模与转化概况，按月汇总PV/UV/Trial/Add/Pay/Refunds，生成核心漏斗图表',
 'data': {{'chart_type': 'bar',
  'x': ['UV访问', '试用申请', '加入购物车', '完成购买', '退款'],
  'y_series': {{'用户数量': [237082, 103784, 25589, 12535, 381]}},
  'summary': '2024年6月核心转化漏斗分析报告：本月总PV为359,167次，UV为237,082人。从UV到试用的转化率为43.78%，试用到加入购物车的转化率为24.66%，购物车到购买的转化率为48.99%，退款率为3.04%。整体转化漏斗呈现典型递减趋势，试用阶段转化率较高，但购物车到购买环节存在较大流失。建议优化购物车体验和支付流程，提升最终转化率。',
  'title': '2024年6月核心转化漏斗',
  'xlabel': '转化阶段',
  'ylabel': '用户数量'}},
 'chart_paths': 'artifacts/2024年6月核心转化漏斗.png'
}}  

输出示例（content_html）：  
<h1>2024年6月数据分析报告</h1>  

<h2>核心转化漏斗分析</h2>  
<p>2024年6月平台总PV为359,167，UV为237,082，用户在试用、加购、购买及退款环节逐级递减。</p>  

<h3>核心数据</h3>  
<table>
  <tbody>
    <tr><th>试用用户数</th><td>103784</td></tr>
    <tr><th>加购用户数</th><td>25589</td></tr>
    <tr><th>购买用户数</th><td>12535</td></tr>
    <tr><th>退款用户数</th><td>381</td></tr>
  </tbody>
</table>  

<h3>转化率表现</h3>  
<table>
  <tbody>
    <tr><th>UV/PV</th><td>65.98%</td></tr>
    <tr><th>试用/UV</th><td>43.77%</td></tr>
    <tr><th>加购/试用</th><td>24.66%</td></tr>
    <tr><th>购买/加购</th><td>48.99%</td></tr>
    <tr><th>退款/购买</th><td>3.04%</td></tr>
  </tbody>
</table>  

<h3>分析结论</h3>  
<p>整体转化链路表现良好，加购到购买环节效率较高，退款率较低，表明转化质量较佳。</p>  

<h3>附件</h3>  
<p>artifacts/funnel_chart.png，outputTable/monthly_funnel_data.csv</p>  

【注意事项】  
- 每个 json 对应一个 <h2> 小节；  
- 所有表格必须使用 <table> 标签；  
- 内容要专业、简洁、结构清晰；  
- 输出的 JSON 必须严格符合规定的键名和层次。  
"""
report_prompt=ChatPromptTemplate.from_messages([
    ("system",prompt),
    ("user","输入的json列表如下：{json_list}请生成报告。")
])
pmt=report_prompt.invoke({"json_list":analysis_log})
ret=llm.invoke(pmt)
import json
data=json.loads(ret.content)

#创建邮箱服务器
import zmail
server=zmail.server("1140400521@qq.com","zgxjfekdiqurbagh")
'''mail={
    "subject":"数据分析报告",
    "content_html":"<p>请查收</P>",
    "attachments":""
}'''
server.send_mail("13508363537cai@gmail.com",data)


