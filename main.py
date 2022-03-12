from fastapi import FastAPI, HTTPException, Response, status
from pymongo import MongoClient
import utils
from bson.objectid import ObjectId
from statistics import mean
from schemas.vote import Vote
import os

client = MongoClient(os.environ.get('MONGODB'))
db = client.Pizza
collection = db["Pizzas"]


app = FastAPI()


@app.get("/")
def welcome():
    """Just welcome page."""
    return {"Message": "Welcome to rate pizza app!"}


@app.get("/pizza")
def get_all_pizzas():
    """Get all available pizzas."""
    try:
        pizzas_sanitized = utils.sanitize_mongodb_document(list(collection.find({})))
        return {"pizzas": pizzas_sanitized}
    except:
        raise HTTPException(status_code=400, detail="Something went wrong")


@app.get("/pizza/{item_id}")
def get_one_pizza(item_id):
    """Get one pizza."""
    try:
        pizza_obj = collection.find_one(ObjectId(item_id))
        pizza_sanitized = utils.sanitize_mongodb_document(pizza_obj)
        return {"pizza": pizza_sanitized}
    except:
        raise HTTPException(status_code=404, detail="Item not found")


@app.post("/pizza/{item_id}")
def vote_on_pizza(item_id, vote: Vote, response: Response):
    """
    Allow user to vote on specific pizza.
    Create user vote in pizza document or update vote if it exist.
    """
    try:
        pizza_obj = collection.find_one(ObjectId(item_id))
    except:
        raise HTTPException(status_code=404, detail="Item not found or invalid item")
    pizza_obj["rate"].update({str(vote.user_id): vote.vote})
    pizza_obj["average_rate"] = round(mean(list(pizza_obj["rate"].values())), 2)
    collection.replace_one({"_id": ObjectId(item_id)}, pizza_obj)
    response.status_code = status.HTTP_201_CREATED
    return {f"Now average rate of {pizza_obj['name']} is {pizza_obj['average_rate']}"}
