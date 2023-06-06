import os

import openai
from langchain.llms import OpenAIChat
from langchain import PromptTemplate

from config import config_langchain
config_langchain()

llm = OpenAIChat(temperature=0.9)

template = """
我真的很想去{location}旅行。 我应该在那里做什么？

用一句话回答
"""

prompt = PromptTemplate(
    input_variables=['location'],
    template=template,
)

final_prompt = prompt.format(location='罗马')
print(f'Final Prompt: {final_prompt}')
print(f'LLM Output: {llm(final_prompt)}')
