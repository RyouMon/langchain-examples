from langchain.llms import OpenAIChat
from langchain import PromptTemplate, LLMChain

from config import config_langchain
config_langchain()

llm = OpenAIChat(temperature=0.9)
prompt = PromptTemplate(
    input_variables=['location'],
    template="""
    我真的很想去{location}旅行。 我应该在那里做什么？
    
    用一句话回答
    """,
)
chain = LLMChain(llm=llm, prompt=prompt)
print(chain.run("北京"))
