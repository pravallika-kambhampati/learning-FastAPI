from sys import float_repr_style
from typing import Optional
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

inventory = {
    1:{
        "name":"Milk",
        "price": 3.99,
        "brand":"Regular"
    }
}

@app.get("/")
def welcome():
    return {"Message":"Learning FastAPI"}

@app.get("/get-all")
def get_all():
    return inventory

@app.get("/get-item/{item_id}")
def get_item(item_id:int=Path(None,description="The ID of the item you would like to retrieve",gt=0)):
    return inventory[item_id]

# query parameters
# name: str = None => makes the query name optional
@app.get("/get-by-name/{item_id}")
def get_item(item_id:int, name: Optional[str] = None):
    
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
     
    return {"Data":"Not Found"}


@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error":"Item ID already exists"}
    inventory[item_id] = item
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in inventory:
        return {"Error":"Item ID does not exist"}
    inventory[item_id].update(item)
    return inventory[item_id]
  

# https://youtu.be/-ykeT6kk4bk?t=2792