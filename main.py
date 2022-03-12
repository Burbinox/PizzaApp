from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
import utils
from bson.objectid import ObjectId
from pydantic import BaseModel, validator
from statistics import mean

client = MongoClient("mongodb://localhost:27017/")
db = client.pizza
collection = db["pizzas"]


app = FastAPI()


class Vote(BaseModel):
    user_id: int
    vote: int

    @validator("vote")
    def vote_must_be_in_range_1_to_5(cls, value):
        if value not in [1, 2, 3, 4, 5]:
            raise ValueError("Allowed vote values are 1,2,3,4,5")
        return value


@app.get("/")
def welcome():
    return {"Message": "Welcome to rate pizza app!"}


@app.get("/pizza")
def get_all_pizzas():
    try:
        pizzas_sanitized = utils.sanitize_mongodb_document(list(collection.find({})))
        return {"pizzas": pizzas_sanitized}
    except:
        raise HTTPException(status_code=400, detail="Item not found")


@app.get("/pizza/{item_id}")
def get_one_pizza(item_id):
    try:
        pizza_obj = collection.find_one(ObjectId(item_id))
        pizza_sanitized = utils.sanitize_mongodb_document(pizza_obj)
        return {"pizza": pizza_sanitized}
    except:
        raise HTTPException(status_code=404, detail="Item not found")


@app.post("/pizza/{item_id}")
def vote_on_pizza(item_id, vote: Vote):
    try:
        pizza_obj = collection.find_one(ObjectId(item_id))
    except:
        raise HTTPException(status_code=404, detail="Item not found or invalid item")
    pizza_obj["rate"].update({str(vote.user_id): vote.vote})
    pizza_obj["average_rate"] = mean(list(pizza_obj["rate"].values()))
    collection.replace_one({"_id": ObjectId(item_id)}, pizza_obj)
    return {f"Now average rate of {pizza_obj['name']} is {pizza_obj['average_rate']}"}
