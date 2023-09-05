from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello 박혜연"}

from resolver import random_items, random_geners_items

@app.get("/all")
async def all_movies():
    result = random_items()
    return {"result":result}

@app.get("/genres/{genre}")
async def genre_movies(genre: str):
    result = random_geners_items(genre)
    return {"result": result}

from recommender import item_based_recommendation

@app.get("/item-based/{item_id}")
async def item_based(item_id: str):
    result = item_based_recommendation(item_id)
    return {"result": result}


