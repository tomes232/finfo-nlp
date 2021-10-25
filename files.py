import os
import openai
openai.organization = "org-9eeR7LXRyCEwLMGEtfhmQLms"
openai.api_key = os.getenv("OPENAI_API_KEY")

openai.File.create(file=open("sandbox.jsonl"), purpose="search")
print("done")
