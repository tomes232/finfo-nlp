import requests


def upload():

    headers = {
        'Authorization': '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',
    }

    files = {
        'purpose': (None, 'answers'),
        'file': ('sandbox.jsonl', open('sandbox.jsonl', 'rb')),
    }

    response = requests.post('https://api.openai.com/v1/files', headers=headers, files=files)
    print(response)
