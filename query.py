import os
import openai
openai.organization = "org-9eeR7LXRyCEwLMGEtfhmQLms"
openai.api_key = os.getenv("OPENAI_API_KEY")
def genQuery(query, in_file):
    completion = openai.Completion()
    response = completion.get(query, in_file)
    return response.choices[0].text
def genAnswer(query, in_file):
    completion = openai.Completion()
    start_chat_log = '''Human: Hello, who are you?
AI: I am doing great. How can I help you today?
'''
    with open(in_file, 'w') as f:
        f.write(start_chat_log)
        f.write(query)
    with open(in_file, 'r') as f:
        chat_log = f.read()
    chat_log = chat_log.replace('\n', ' ')
    chat_log = chat_log.replace('\t', ' ')
    chat_log = chat_log.replace('\r', ' ')
    chat_log = chat_log.replace('\b', ' ')
    chat_log = chat_log.replace('\f', ' ')
    chat_log = chat_log.replace('\v', ' ')
    chat_log = chat_log.replace('\a', ' ')
    chat_log = chat_log.replace('\e', ' ')
    chat_log = chat_log.replace('\x1b', ' ')
    chat_log = chat_log.replace('\x1c', ' ')
    chat_log = chat_log.replace('\x1d', ' ')
    chat_log = chat_log.replace('\x1e', ' ')
    chat_log = chat_log.replace('\x1f', ' ')
    chat_log = chat_log.replace('\x7f', ' ')
    chat_log = chat_log.replace('\x1b[0m', ' ')
    chat_log = chat_log.replace('\x1b[1m', ' ')
    chat_log = chat_log.replace('\x1b[2m', ' ')
    chat_log = chat_log.replace('\x1b[3m', ' ')
    chat_log = chat_log.replace('\x1b[4m', ' ')
    chat_log =