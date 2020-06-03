#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from fastapi import FastAPI
from pydantic import BaseModel
import time

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False

@app.get("/")
def read_root():
    print('Hello World')
    return dict(hello = 'world')

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    '''
    http ":8000/items/1?q=wxnacy"
    '''
    return locals()

@app.post("/items/{item_id}")
def save_item(item_id: int, item: Item):
    '''
    curl -X POST "http://127.0.0.1:8000/items/1" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"name\":\"string\",\"price\":0,\"is_offer\":false}"
    '''
    return locals()

@app.get("/async")
async def read_async():
    return dict(hello = 'world')

@app.get("/time/{seconds}")
async def time_out(seconds: int):
    time.sleep(seconds)
    return dict(hello = 'world')
