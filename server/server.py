from flask import Flask, request
from config import db
import json

app = Flask(__name__)

@app.get("/")
def home():
  return "Hello from Flask"

@app.get("/about")
def testAbout():
  me ={"name": "Alexis"}
  return json.dumps(me)

def fixID(obj):
  obj["_id"] = str(obj["_id"])
  return obj

products = []
@app.get("/api/products")
def getProducts():
  products = []
  cursor = db.products.find({})
  for product in cursor:
    products.append(fixID(product))
  return json.dumps(products)

@app.get("/api/products/count")
def countProducts():
  products = []
  return json.dumps(len(products))

@app.get("/api/products/<category>")
def getCategory(category):
  products = []
  items = json.loads(getProducts())
  for item in items:
    if item["Category"] == category:
      products.append(fixID(item))
  return json.dumps(products)

@app.post("/api/products")
def addProduct():
  prod = request.get_json()
  print("New product added", prod)
  products.append(prod)
  db.products.insert_one(prod)
  fixID(prod)
  return json.dumps(products)

@app.patch("/api/products/<int:index>")
def patchProduct(index):
  updtField = request.get_json()
  print(updtField)
  if 0 <= index < len(products):
    products[index].update(updtField)
    return json.dumps(products)
  else:
    return "ERROR: Invalid index"

@app.put("/api/products/<int:index>")
def updateProduct(index):
  updtProd = request.get_json()
  print(updtProd)
  if 0 <= index < len(products):
    products[index] = updtProd
    return json.dumps(products)
  else:
    return "ERROR: Invalid index"

@app.delete("/api/products/<int:index>")
def deleteProduct(index):
  delProd = request.get_json()
  print(delProd)
  if 0 <= index < len(products):
    products.pop(index)
    return json.dumps(products)
  else:
    return "ERROR: Invalid index"

app.run(debug = True)