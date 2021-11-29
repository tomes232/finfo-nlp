from pymongo import MongoClient
import json

# MongoDB: https://pymongo.readthedocs.io/en/stable/

# pprint library is used to make the output look more pretty
from pprint import pprint

# connect to MongoDB, set a 5-second connection timeout
articles_db = "mongodb+srv://tpickup232:33pJ6uixW4zUwJk@cluster0.8bxso.mongodb.net/articles?retryWrites=true&w=majority"
companies_db = "mongodb+srv://tpickup232:33pJ6uixW4zUwJk@cluster0.8bxso.mongodb.net/companies?retryWrites=true&w=majority"

def get_db(db_name):
    if db_name == "companies":
        conn_str = companies_db
    else:
        conn_str = articles_db
    # set a 5-second connection timeout
    client = MongoClient(conn_str, serverSelectionTimeoutMS=5000)
    
    try:
        client.server_info()
    except Exception:
        print("Unable to connect to the server.")
    
    db = client[db_name]
    return db

def get_collection(db, collection_name):
    if db == "companies":
        conn_str = companies_db
    else:
        conn_str = articles_db
    # set a 5-second connection timeout
    client = MongoClient(conn_str, serverSelectionTimeoutMS=5000)
    
    try:
        client.server_info()
    except Exception:
        print("Unable to connect to the server.")
    
    collection = db[collection_name]
    return collection

def upload_dict(dict_data, db_name, collection_name):
    if db_name == "companies":
        conn_str = companies_db
    else:
        conn_str = articles_db

    # set a 5-second connection timeout

    client = MongoClient(conn_str, serverSelectionTimeoutMS=5000)

    try:
        client.server_info()
    except Exception:
        print("Unable to connect to the server.")
    
    db = client[db_name]
    collection = db[collection_name]

    if db_name == "articles":
        #pymongo find dict_data["text"]
        if collection.find({"text": dict_data["text"]}).count() != 0:
            print(collection.find({"text": dict_data["text"]}))
            return False
    collection.insert_one(dict_data)
    return True

def upload_files(file_path, db_name, collection_name):
    if db_name == "companies":
        conn_str = companies_db
    else:
        conn_str = articles_db
    
    # set a 5-second connection timeout
    client = MongoClient(conn_str, serverSelectionTimeoutMS=5000)

    try:
        client.server_info()
    except Exception:
        print("Unable to connect to the server.")
    
    # get a handle to the database
    db = client[db_name]
    # get a handle to the collection
    collection = db[collection_name]
    # read the file and insert the data into the collection
    with open(file_path, 'r') as file:
        #jsonl file to list of dicts
        documents = [json.loads(line) for line in file]
        collection.insert_many(documents)

def search(db_name, collection_name, query):
    if db_name == "companies":
        conn_str = companies_db
    else:
        conn_str = articles_db
    
    # set a 5-second connection timeout
    client = MongoClient(conn_str, serverSelectionTimeoutMS=5000)

    try:
        client.server_info()
    except Exception:
        print("Unable to connect to the server.")
    
    # get a handle to the database
    db = client[db_name]
    # get a handle to the collection
    collection = db[collection_name]
    # search for the term

    cursor = collection.aggregate([
        {'$match': {'$text': {'$search': query}}},
        {'$project': {'text': 15}}])

    with open('sandbox.jsonl', 'a') as jsonl_file:
        for item in cursor:
            #print(data_dic)
            json.dump({"text": item["text"]}, jsonl_file)
            jsonl_file.write('\n')


# Issue the serverStatus command and print the results
#serverStatusResult=db.command("serverStatus")
#pprint(serverStatusResult)

#main function
if __name__ == "__main__":
    upload_dict({'name': 'John', 'age': 27}, 'myFirstDatabase', 'myFirstCollection')
    upload_files('sandbox.jsonl', 'myFirstDatabase', 'myFirstCollection')
    db = get_db('myFirstDatabase')
    collection = get_collection(db, 'myFirstCollection')
    print(collection.find_one())
    print(collection.find_one({'name': 'John'}))
    print(collection.find_one({'name': 'John'}, {'_id': False}))
    print(collection.find_one({'name': 'John'}, {'_id': False, 'name': True}))