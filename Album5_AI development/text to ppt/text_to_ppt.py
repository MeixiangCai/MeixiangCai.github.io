#项目目标是让TXT文档内容自动生成PPT
from openai import OpenAI
import json
client=OpenAI(
    api_key="sk-1032e547c2404c20940a4187e6b06845",
    base_url="https://api.deepseek.com"
)
#设计few-shot风格的提示词
msg=[
    # 全局提示词：
    {"role": "system",
     "content": '''你是一位擅长结构化内容改写的 PPT 助手，目标是帮助用户将非结构化的工作总结整理为适合制作演示文稿的内容结构，并提升表达质量。你的任务包括：
1. 提取文档的 main_title；
2. 拆分多个章节（chapter），每章包含：
   - chapter_title：章节名称（总结型）
   - describe：本章简介（用于章节封面页），请综合该章节各页内容提炼一个概括性引言，50字以内
   - pages：该章节下的多个内容页面，每页包含：
     - title：页面标题，应从原文抽象提炼，简洁有力
     - body：正文内容（50~100字）：
         - 在保留原文核心事实的基础上，
         - 可适当加入背景信息、分析角度或总结性修饰语，
         - 避免完全照抄原句，鼓励语言组织更有逻辑和层次。
3. 输出格式必须是严格的 JSON，字段包括：
main_title、directory、chapters、chapter_title、describe、pages、title、body。
不要添加任何解释说明或其他冗余内容，仅输出 JSON 数据结构。
'''},
    # few-shot 示例提示词：
    {"role": "user",
     "content": 
     '''2023年第四季度，我们重点完成了用户增长渠道的测试和投放优化, 在抖音、视频号等平台累计测试40+种投放方案，最终CTR提升至5.2%。同时我们上线了内容社区的A/B测试机制，参与度提升显著。在工具产品方面完成了移动端编辑器的0.9版本开发，并通过内部灰度。'''},
    {"role": "assistant",
     "content": '''{
     "main_title": "2023年Q4工作总结",
     "directory": ["用户增长与投放", "社区与内容机制", "工具产品进展"],
     "chapters": [
     {"chapter_title": "用户增长与投放",
      "describe": "本节聚焦于渠道测试与优化成果，展示了多平台投放的实践与CTR的显著提升。",
      "pages": [
      {"title": "渠道投放测试",
      "body": "本季度在抖音、视频号等平台测试了40余种投放方案，探索了短视频与图文内容的组合形式。"},
      {"title": "CTR优化结果",
      "body": "通过素材优化和精准定向投放，CTR 提升至5.2%，显著高于前一季度的3.1%，展现出广告内容与用户兴趣之间更高的匹配度。"}
      ]},
    {"chapter_title": "社区与内容机制",
    "describe": "本节介绍了社区互动策略与内容曝光优化手段，重点体现用户活跃度的提升与精准分发能力。",
    "pages": [
    {"title": "社区互动优化",
    "body": "新上线的互动机制提高了用户评论与点赞频率，社区活跃度显著提升，为社区生态注入了更多活力。"},
    {"title": "A/B测试应用",
    "body": "在社区内容排序策略中引入A/B测试方法，使内容曝光更贴合用户偏好，提升了整体点击率。"}]},
    {"chapter_title": "工具产品进展",
    "describe": "本节回顾了工具产品的核心开发进展与灰度测试反馈，体现平台技术迭代成果。",
    "pages": [
    {"title": "编辑器0.9版本开发",
    "body": "移动端编辑器0.9版本完成核心功能开发，支持文本编辑、图示插入等操作，满足日常使用需求。"},
    {"title": "灰度发布与反馈",
    "body": "通过灰度发布收集用户反馈，团队聚焦于编辑器性能与交互体验的持续优化。"}]}]}'''
}
]
with open("/Users/xiaoxiao/Downloads/aippt2/data/工作记录.txt","r") as file:
    text=file.read()
msg.append({"role":"user","content":text})
response=client.chat.completions.create(
    model="deepseek-chat",
    messages=msg,
    response_format={"type":"json_object"}
)
data=json.loads(response.choices[0].message.content) #将JSON格式字符串转为Python可操作的字典/列表
print(data)

from jinja2 import Template
#以下示例Template函数，即将包含占位符的模板填充数据后生成HTML文本
'''
方法1 直接写出模版:
tpl=Template(
<div>
  <p>欢迎，{{ name_cn }}！</p>
  <p>Hello，{{ name_en }}！</p>
</div>
)
result=tpl.render(name_cn="小羽",name_en="Xiaoyu"),
print(result)

#方法2 读取html文件并转换为模版
with open("html_template.html","r") as f:
   tpl=f.read()
   template=Template(tpl)
html=template.render(name_cn="小羽",name_en="Xiaoyu")
print(html)
'''

#欢迎页模版
welcome_page_tpl=Template('''
<div class="welcome_page">
  <div class="bac_rect"></div>
  <div class="content">
    <div class="main_title">{{ main_title }}</div>
    <div class="title_des">{{ title_des }}</div>
  </div>
  <img class="img1" src="http://nocturne.bczcdn.com/img/1753423722076_38747/3.png" alt="img1">
  <img class="img2" src="http://nocturne.bczcdn.com/img/1753423718645_86698/2.png" alt="img2">
  <div class="author">
    <div class="author-cn">{{ author_cn }}</div>
    <div class="author-en">{{ author_en }}</div>
  </div>
  <div class="team">
    <div class="team-cn">{{ team_cn }}</div>
    <div class="team-en">{{ team_en }}</div>
  </div>
  <div class="line"></div>
</div>
''')
#目录页模版
directory_page_tpl=Template('''
<div class="directory_page">
  <div class="bac_rect"></div>
  <div class="dir_title">目录</div>
  <div class="dir_list">
    {% for item in directory %}
    <div class="dir_item">
      <div class="ellipse">{{ loop.index }}</div>
      <div class="item_text">{{ item }}</div>
    </div>
    {% endfor %}
  </div>
  <img class="img1" src="http://nocturne.bczcdn.com/img/1753425673715_46078/5.png" alt="img1">
  <img class="img2" src="http://nocturne.bczcdn.com/img/1753423662670_15166/1.png" alt="img2">
  <div class="line"></div>
</div>
''')
#创建一个列表，用来存放所有PPT页面
pages=[]
#开始渲染并让模版中传入数据
slide=welcome_page_tpl.render(
   main_title=data["main_title"],
   title_des="运营部门季度总结报告",
   author_cn="小羽",
   author_en="xiaoyu",
   team_cn="超有爱",
   team_en="baicizhan.com"
)
#将该页面加入到列表中
pages.append(slide)
#同样对目录页进行操作
pages.append(directory_page_tpl.render(directory=data["directory"]))
#章节页模版
chapter_page_tpl=Template('''
<div class="chapter_page">
  <div class="bac_rect"></div>
  <div class="content">
    <div class="chapter_title">{{ chapter_title }}</div>
    <div class="describe">{{ describe }}</div>
  </div>
  <img class="img1" src="http://nocturne.bczcdn.com/img/1753425673715_46078/5.png" alt="img1">
  <img class="img2" src="http://nocturne.bczcdn.com/img/1753423662670_15166/1.png" alt="img2">
  <div class="line"></div>
</div>
''')
#章节详情页模版
chapter_detail_page_tpl=Template('''
<div class="chapter_detail_page">
  <div class="chapter_title">{{ chapter_title }}</div>
  <div class="page_content">
    <div class="title">{{ title }}</div>
    <div class="body">{{ body }}</div>
  </div>
  <img class="img1" src="http://nocturne.bczcdn.com/img/1753423726769_97054/4.png" alt="img1">
  <div class="line"></div>
</div>
''')
#使用for循环遍历JSON数据中的每一个章节
for cpt in data["chapters"]:
   slide=chapter_page_tpl.render(
      chapter_title=cpt["chapter_title"],
      describe=cpt["describe"]
   )
   pages.append(slide)
   #使用for循环获取某一章节的所有详情页
   for pg in cpt["pages"]:
      slide=chapter_detail_page_tpl.render(
      chapter_title=cpt["chapter_title"],
      title=pg["title"],
      body=pg["body"]   
      )
      pages.append(slide)
#添加结束页
pages.append(welcome_page_tpl.render(
   main_title="Thank You!",
   title_des="感谢您的观看",
   author_cn="小羽",
   author_en="xiaoyu",
   team_cn="超有爱",
   team_en="baicizhan.com"
))
#获取整体框架模版
with open("/Users/xiaoxiao/Downloads/aippt2/data/ppt_temp_jinja.html","r") as f:
   tpl=f.read()
   template=Template(tpl)
html=template.render(pages=pages)
#将生成的PPT网页写入新的html文件中
with open("/Users/xiaoxiao/Downloads/aippt2/data/out_put.html","w",encoding="utf-8") as f:
   f.write(html)

   








