import pandas as pd
import requests
movies_df = pd.read_csv('data/movies.csv')
print(movies_df)

movies_df['movieId'] = movies_df['movieId'].astype(str)
links_df = pd.read_csv('data/links.csv', dtype=str)
merge_df = movies_df.merge(links_df, on='movieId', how='left')
print(merge_df)

def add_url(row):
    return f'http://www.imdb.com/title/tt{row}'

merge_df['url'] = merge_df['imdbId'].apply(lambda x:add_url(x))
print(merge_df)

rating_df = pd.read_csv('data/ratings.csv')
rating_df['movieId'] = rating_df['movieId'].astype(str)

agg_df = rating_df.groupby('movieId').mean()
print(agg_df)

agg_df = rating_df.groupby('movieId').count()
print(agg_df)

agg_df = rating_df.groupby('movieId').agg(rcount=('rating', 'count'),
                                          rmean = ('rating', 'mean'),
                                          uid = ('userId', 'sum'))
print(agg_df)

merge_df = merge_df.merge(agg_df, on='movieId')
print(merge_df)

from tqdm import tqdm

def add_poster(df):
    for i, row in tqdm(df.iterrows(), total=df.shape[0]):
        tmdb_id = row["tmdbId"]
        tmdb_url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key=f2a1fddeef038db026fb3e05415e80f2&language=en-US"
        result = requests.get(tmdb_url)
        # final url : https://image.tmdb.org/t/p/original/uXDfjJbdP4ijW5hWSBrPrlKpxab.jpg
        try:
            df.at[i, "poster_path"] = "https://image.tmdb.org/t/p/original" + result.json()['poster_path']
        except (TypeError, KeyError) as e:
            # toy story poster as default
            df.at[i, "poster_path"] = "https://image.tmdb.org/t/p/original/uXDfjJbdP4ijW5hWSBrPrlKpxab.jpg"
    return df

merge_df['poster_path'] = None
merge_df = add_poster(merge_df)
print(merge_df)

merge_df.to_csv('data/movies_final.csv', index=None)
