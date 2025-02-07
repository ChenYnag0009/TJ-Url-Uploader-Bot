from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

try:
    # Replace with your MongoDB URI
    uri = "mongodb+srv://pangphu9:0pSRO3UHIoH5ouAx@cluster0.ipqp2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri)
    
    # Test the connection by getting server info
    print(client.server_info())  # If successful, this prints MongoDB server info
    
except ConnectionFailure as e:
    print(f"Could not connect to MongoDB: {e}")
