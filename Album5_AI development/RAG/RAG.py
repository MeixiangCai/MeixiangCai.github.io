#项目目标是创建一个能检索外部文件并且利用llm生成回答的agent
#先使用文档加载器读取文档
from langchain_community.document_loaders.csv_loader import CSVLoader #也可以读取TextLoader/PyPDFLoader
#指定文件路径
file_path="/Users/xiaoxiao/Downloads/movie/movies.csv"
#创建加载器实例
loader=CSVLoader(file_path)
data=loader.load()
#查看每一行的数据
print(data[0].page_content) #查看的是第一页
#文档内容过多时，需要用到文档拆分器先进行拆分，以PDF为例
from langchain_community.document_loaders import PyPDFLoader
file_path="/Users/xiaoxiao/Downloads/vector_spaces.pdf"
loader=PyPDFLoader(file_path)
docs=loader.load()
from langchain_text_splitters import RecursiveCharacterTextSplitter
#创建文本切分器实例
text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=90,
    chunk_overlap=20,
    separators=[
        "\n\n",
        "\n",
        "。","！","？",
        ".","!","?",
        ""
    ]
)
chunks=text_splitter.split_documents(docs) #开始切分
print(chunks[0].page_content) #输出第一个切分块的内容

#接下来尝试做文档向量化
from langchain_huggingface import HuggingFaceEmbeddings
embeddings=HuggingFaceEmbeddings(
    model_name="/Users/xiaoxiao/Desktop/yequbiancheng/AI_development/all-MiniLM-L6-v2"
) #如果本地模型文件中某些配置文件缺失，会自动去用HuggingFace官网的模型
vector=embeddings.embed_query("夜曲编程") #将字符串转换为向量
print(vector)
texts=["夜曲编程","百职帮","嘻嘻嘻"]
vectors=embeddings.embed_documents(texts) #批量向量化
print(vectors[0])

#构建向量数据库
from langchain_community.vectorstores import FAISS #导入本地型内存数据库
db=FAISS.from_documents(chunks,embeddings) #刚才切分好的PDF
retriever=db.as_retriever() #将向量库转换为检索器
retrieved_docs=retriever.invoke("What is vector space?")
print(retrieved_docs[0].page_content)

#接下来让检索和生成同时完成
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
#创建聊天模型客户端
model=ChatOpenAI(
    api_key="sk-ae518d28b0b144179862cccbe5594daa",
    model="deepseek-chat",
    base_url="https://api.deepseek.com"
)
#创建记忆
memory=ConversationBufferMemory(memory_key="chat_history",return_messages=True)
#向AI发起多轮带有检索的对话
from langchain.chains import ConversationalRetrievalChain #导入对话式RAG链
qa=ConversationalRetrievalChain.from_llm(
    llm=model,
    retriever=retriever,
    memory=memory
)
#发起第一轮对话
ret=qa.invoke({"question":"简单说明vector space是什么东西"})
print(ret["answer"])
ret=qa.invoke({"question":"它在编程中有什么用"})
print(ret["answer"])




