from pymongo.mongo_client import MongoClient
import certifi

uri = "mongodb+srv://Alexis:test123@107-ch46.ox6lm0b.mongodb.net/?retryWrites=true&w=majority&appName=107-ch46"

# Create a new client and connect to the server
client = MongoClient(uri, tlsCAfile = certifi.where())
db = client.get_database("107-ch46")

# Send a ping to confirm a successful connection
try:
  client.admin.command('ping')
  print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
  print(e)