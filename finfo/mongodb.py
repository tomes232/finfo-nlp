from pymongo import MongoClient
import json

# MongoDB: https://pymongo.readthedocs.io/en/stable/

# pprint library is used to make the output look more pretty
from pprint import pprint

# connect to MongoDB, set a 5-second connection timeout
conn_str = "mongodb+srv://tpickup232:33pJ6uixW4zUwJk@cluster0.8bxso.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"


def get_db(db_name):
    # set a 5-second connection timeout
    client = MongoClient(conn_str, serverSelectionTimeoutMS=5000)
    
    try:
        client.server_info()
    except Exception:
        print("Unable to connect to the server.")
    
    db = client[db_name]
    return db

def get_collection(db, collection_name):
    # set a 5-second connection timeout
    client = MongoClient(conn_str, serverSelectionTimeoutMS=5000)
    
    try:
        client.server_info()
    except Exception:
        print("Unable to connect to the server.")
    
    collection = db[collection_name]
    return collection

def upload_dict(dict_data, db_name, collection_name):
    # set a 5-second connection timeout
    client = MongoClient(conn_str, serverSelectionTimeoutMS=5000)

    try:
        client.server_info()
    except Exception:
        print("Unable to connect to the server.")
    
    db = client[db_name]
    collection = db[collection_name]
    collection.insert_one(dict_data)

def upload_files(file_path, db_name, collection_name):
    
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