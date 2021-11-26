import openai
import os
import json

with open('finfo/api/config.json', 'r') as f:
    config = json.load(f)
classification_config = config["classification"]

openai.organization = "org-9eeR7LXRyCEwLMGEtfhmQLms"
openai.api_key = os.getenv("OPENAI_API_KEY")

def classification(query):
    response = openai.Classification.create(
    search_model=classification_config["search_model"],
    model=classification_config["model"],
    examples=classification_config["examples"],
    query=query,
    labels=classification_config["labels"],
    )
    return response.label

def classification_with_file(query, in_file):
    #upload file to openai
    file_id = openai.File.upload(in_file)

    response = openai.Classification.create(
    search_model=classification_config["search_model"],
    model=classification_config["model"],
    examples=classification_config["examples"],
    query=query,
    labels=classification_config["labels"],
    file= file_id,
    )

    #for 

    return response.label


