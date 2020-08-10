#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from fastapi import FastAPI
from typing import Optional
from fastapi import Body

from fastapi import Depends

app = FastAPI()

async def common_parameters(q: Optional[str] = None, skip: int = Body(0, title='test'), limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons
