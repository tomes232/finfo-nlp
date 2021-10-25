import os
import openai
openai.organization = "org-9eeR7LXRyCEwLMGEtfhmQLms"
openai.api_key = os.getenv("OPENAI_API_KEY")

def getSearchResults(query, file):

    response = openai.Engine("ada").search(
                search_model="ada",
                query=query,
                max_rerank=5,
                file=file
                )

    return response
