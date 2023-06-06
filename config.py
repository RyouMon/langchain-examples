import os

import openai

OPENAI_API_KEY = ''
OPENAI_API_BASE = ''
SERPAPI_API_KEY = ''


def config_langchain():
    assert OPENAI_API_KEY
    openai.api_key = OPENAI_API_KEY
    if OPENAI_API_BASE:
        openai.api_base = OPENAI_API_BASE

    os.environ["OPENAI_API_KEY"] = openai.api_key
    os.environ['SERPAPI_API_KEY'] = SERPAPI_API_KEY
