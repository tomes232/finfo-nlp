import os
import openai 

openai.api_key = os.environ.get('OPENAI_KEY')
completion = openai.Completion()

start_chat_log = '''Human: Hello, who are you?
AI: I am doing great. How can I help you today?
'''
def genAnswer(query, in_file):
  response = openai.Answer.create(
   search_model="davinci",
   model="curie",
   question=query,
   file= in_file,
   examples_context="OnChain Studios has raised $7.5 million in a seed funding round led by Andreessen Horowitz (a16z) to develop Cryptoys: a new non-fungible token (NFT) platform that combines digital toys and gaming.",
   examples=[["Who led the funding rounnd for OnChain?","Andreessen Horowitz of a16z led the funding"]],
   max_rerank=5,
   max_tokens=50,
   stop=["\n", "<|endoftext|>"]
  )
  return response


def ask(question, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    print(question)
    prompt = f'{chat_log}Human: {question}\nAI:'
    response = completion.create(
        prompt=prompt, engine="davinci", stop=['\nHuman'], temperature=0.3,
        frequency_penalty=0, presence_penalty=0.6, best_of=1,
        max_tokens=150)
    answer = response.choices[0].text.strip()
    return answer

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    return f'{chat_log}Human: {question}\nAI: {answer}\n'    


if __name__ == "__main__":
    main()
