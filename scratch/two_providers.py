import os
from anthropic import Anthropic
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
print(Anthropic().messages.create(model="claude-haiku-4-5-20251001", max_tokens=50, messages=[{"role": "user", "content": "Say hi"}]).content[0].text)
print(OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.environ["OPENROUTER_API_KEY"]).chat.completions.create(model="anthropic/claude-haiku-4.5", max_tokens=50, messages=[{"role": "user", "content": "Say hi"}]).choices[0].message.content)
