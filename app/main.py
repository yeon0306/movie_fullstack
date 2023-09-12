from typing import Optional, List

from fastapi import FastAPI, Query
from resolver import random_items, random_geners_items
from recommender import item_based_recommendation,user_based_recommendation

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
origins = ['*', ]
app.add_middleware(CORSMiddleware,
                   allow_origins = origins,
                   allow_credentials = True,
                   allow_methods = ["*"],
                   allow_headers = ["*"]
                   )
@app.get("/")
async def root():
    return {"message": "Hello 박혜연"}

@app.get("/all")
async def all_movies():
    result = random_items()
    return {"result":result}

@app.get("/genres/{genre}")
async def genre_movies(genre: str):
    result = random_geners_items(genre)
    return {"result": result}

@app.get("/item-based/{item_id}")
async def item_based(item_id: str):
    result = item_based_recommendation(item_id)
    return {"result": result}

@app.get("/user-based/")
async def user_based(params: Optional[List[str]] = Query(None)):
    input_rating_dict = dict(
        (int(x.split(":")[0]), float(x.split(":")[1])) for x in params
    )
    result = user_based_recommendation(input_rating_dict)
    return {"result": result}

