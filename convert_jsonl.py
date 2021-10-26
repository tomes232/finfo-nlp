import json 
#This strips an input file and adds it to our sandboxjson file
#TODO: Make this work. Standardize the datascraping input
with open('sandbox.txt', 'r') as in_file:
    text = in_file.read()
    data = text.rstrip('\n\n')
    print(data[1])
    for datum in data:
        data_dic = {"text": datum}
        with open('sandbox.jsonl', 'w') as jsonl_file:
            json.dump(data_dic, jsonl_file)

