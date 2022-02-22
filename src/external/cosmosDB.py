from operator import le
import os
from azure.cosmos import exceptions, CosmosClient, PartitionKey
import json
from dotenv import load_dotenv
load_dotenv()

endpoint = os.getenv('COSMOSDB_ENDPOINT')
key = os.getenv('COSMOSDB_KEY')

client = CosmosClient(endpoint, key)

DATABASE_NAME = 'WordleDB'
database = client.get_database_client(DATABASE_NAME)
CONTAINER_NAME = 'records'
container = database.get_container_client(CONTAINER_NAME)

def insertData(data):
    container.upsert_item(data)



