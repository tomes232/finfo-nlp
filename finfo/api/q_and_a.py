import os
import openai
import json

# load_dotenv()
openai.organization = "org-9eeR7LXRyCEwLMGEtfhmQLms"
openai.api_key = os.getenv("OPENAI_API_KEY")


def genAnswer(query, in_file):
  response = openai.Answer.create(
   search_model="davinci",
   model="curie",
   question=query,
   file= in_file,
   examples_context="OnChain Studios has raised $7.5 million in a seed funding round led by Andreessen Horowitz (a16z) to develop Cryptoys: a new non-fungible token (NFT) platform that combines digital toys and gaming.",
   examples=[["Who led the funding rounnd for OnChain"," Andreessen Horowitz of a16z led the funding"]],
   max_rerank=5,
   max_tokens=50,
   stop=["\n", "<|endoftext|>"]
  )
  return response

def genAnswer_config(query, in_file, classification):
  with open('finfo/api/config.json', 'r') as f:
    config = json.load(f)
  model_config = config[classification]["answering"]

  response = openai.Answer.create(
  search_model=model_config['params']["search_model"],
  model=model_config['params']["model"],
  question=query,
  file= in_file,
  examples_context=model_config["qa_context"],
  examples=model_config["examples"],
  max_rerank=model_config['params']["max_rerank"],
  max_tokens=model_config['params']["max_tokens"],
  stop=model_config['params']["stop"]
  )
  return response


def main():
  print("Hello! Welcome to finfo ai.")
  print("Im am here for all your financial needs")
  print("call me sugar daddy")
  while (True):
    query = input("Enter your question here: ")
    answer = genAnswer(query, "file-m0ha2QN8KdLFsP15VoOj7scz")["answers"][0]
    print("Easy")
    print(answer)



    
    #answer = genAnswer("Who lead the most recent funding round for Superplastic?", "file-QRZKYePIEhaQGkjS8ajlzPXJ")



if __name__ == "__main__":
    main()






#path = '/home/tommypickup/projects/umich/eecs498/finfo/clincArticle"
#files = os.listdir(path)
#for file in files:
#    curl https://api.openai.com/v1/files \
#  -H "Authorization: Bearer YOUR_API_KEY" \
#  -F purpose="answers" \
#  -F file='@puppy.jsonl'
