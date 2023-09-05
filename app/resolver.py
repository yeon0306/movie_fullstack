import pandas as pd

def random_items():
    movie_df = pd.read_csv("data/movies_final.csv")
    movie_df = movie_df.fillna('')
    result_items = movie_df.sample(n=5).to_dict("records")
    return result_items

def random_geners_items(genre):
    movie_df = pd.read_csv("data/movies_final.csv")
    genre_df = movie_df[movie_df['genres'].apply(lambda x: genre in x.lower())]
    genre_df = genre_df.fillna('')
    result_items = genre_df.sample(n=5).to_dict("records")
    return result_items