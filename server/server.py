from flask import Flask, request
import json

app = Flask(__name__)

@app.get("/")
def home():
  return "Hello from Flask"

@app.get("/about")
def testAbout():
  me ={"name": "Alexis"}
  return json.dumps(me)

products = []
@app.get("/api/products")
def getProducts():
  return json.dumps(products)

@app.get("/api/products/count")
def countProducts():
  return json.dumps(len(products))

@app.post("/api/products")
def addProduct():
  prod = request.get_json()
  print(prod)
  products.append(prod)
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