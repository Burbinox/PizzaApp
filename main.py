from fastapi import FastAPI
from pymongo import MongoClient
import utils
from bson.objectid import ObjectId

client = MongoClient('mongodb://localhost:27017/')
db = client.pizza
collection = db["pizzas"]


app = FastAPI()


@app.get("/")
def welcome():
    return {"Message": "Welcome to rate pizza app!"}


@app.get("/pizza")
def get_all_pizzas():
    pizzas_sanitized = utils.sanitize_mongodb_document(list(collection.find({})))
    return {"pizzas": pizzas_sanitized}


@app.get("/pizza/{item_id}")
def get_one_pizza(item_id):
    pizza_obj = collection.find_one(ObjectId(item_id))
    pizza_sanitized = utils.sanitize_mongodb_document(pizza_obj)
    return {"pizza": pizza_sanitized}
