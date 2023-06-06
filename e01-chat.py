from langchain.llms import OpenAIChat

from config import config_langchain
config_langchain()

llm = OpenAIChat(temperature=0.9)
text = "一家生产彩色袜子的公司取什么名字好？"
print(llm(text))
