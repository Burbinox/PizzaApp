from fastapi import FastAPI
from pymongo import MongoClient
from bson import json_util, ObjectId
import json

client = MongoClient('mongodb://localhost:27017/')
db = client.pizza
collection = db["pizzas"]


app = FastAPI()


@app.get("/")
def welcome():
    return {"Message": "Welcome to rate pizza app!"}


@app.get("/pizza")
def get_all_pizzas():
    pizzas_sanitized = json.loads(json_util.dumps(list(collection.find({}))))
    return {"pizzas": pizzas_sanitized}
