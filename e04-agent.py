from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.llms import OpenAIChat

from config import config_langchain
config_langchain()


llm = OpenAIChat(temperature=0.9)
tools = load_tools(['serpapi', 'llm-math'], llm=llm)

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

agent.run('北京昨天的高温是多少度？ 这个数字的 .023 次方是多少？')
