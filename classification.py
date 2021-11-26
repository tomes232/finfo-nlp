import openai
import os
import json

with open('config.json', 'r') as f:
    config = json.load(f)
classification = config["classification"]

openai.organization = "org-9eeR7LXRyCEwLMGEtfhmQLms"
openai.api_key = os.getenv("OPENAI_API_KEY")

def classification(query, in_file):
    response = openai.Classification.create(
    search_model="ada",
    model=classification["model"],
    examples=classification["examples"],
    query=query,
    labels=classification["labels"],
    )
    return response.label

def
