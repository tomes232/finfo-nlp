import os
import openai
import dotenv
from dotenv import load_dotenv

load_dotenv()
openai.organization = "org-9eeR7LXRyCEwLMGEtfhmQLms"
openai.api_key = os.getenv("OPENAI_API_KEY")
# print("this is the api key: ", openai.api_key)
document_list = ["Google was founded in 1998 by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University in California. Together they own about 14 percent of its shares and control 56 percent of the stockholder voting power through supervoting stock. They incorporated Google as a privately held company on September 4, 1998. An initial public offering (IPO) took place on August 19, 2004, and Google moved to its headquarters in Mountain View, California, nicknamed the Googleplex. In August 2015, Google announced plans to reorganize its various interests as a conglomerate called Alphabet Inc. Google is Alphabet's leading subsidiary and will continue to be the umbrella company for Alphabet's Internet interests. Sundar Pichai was appointed CEO of Google, replacing Larry Page who became the CEO of Alphabet.",
"Amazon is an American multinational technology company based in Seattle, Washington, which focuses on e-commerce, cloud computing, digital streaming, and artificial intelligence. It is one of the Big Five companies in the U.S. information technology industry, along with Google, Apple, Microsoft, and Facebook. The company has been referred to as 'one of the most influential economic and cultural forces in the world', as well as the world's most valuable brand. Jeff Bezos founded Amazon from his garage in Bellevue, Washington on July 5, 1994. It started as an online marketplace for books but expanded to sell electronics, software, video games, apparel, furniture, food, toys, and jewelry. In 2015, Amazon surpassed Walmart as the most valuable retailer in the United States by market capitalization."]

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


def main():
  print("Hello! Welcome to finfo ai.")
  print("Im am here for all your financial needs")
  print("call me sugar daddy")
  while (True):
    query = input("Enter your question here: ")
    answer = genAnswer(query, "file-QRZKYePIEhaQGkjS8ajlzPXJ")["answers"][0]
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
