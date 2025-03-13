import pandas as pd

movies_df = pd.read_csv("./resources/movies.csv")
ratings_df = pd.read_csv("./resources/ratings.csv")

merged = pd.merge(movies_df, ratings_df, left_on='movieId', right_on='movieId', how='left')
print(merged.head())

# Count how many times each movieId is present in the merged DataFrame
merged_with_count = merged.groupby("movieId").size().reset_index(name='count').sort_values(by='count', ascending=False)
print(merged_with_count)

final_df = pd.merge(merged, merged_with_count, left_on='movieId', right_on='movieId', how='left')

# Create movie_title_input_profiles without the count
movie_title_input_profiles = final_df.groupby("movieId").agg({
    "title": lambda x: x.drop_duplicates().iloc[0] if not x.isnull().all() else "Unknown",
    "genres": lambda x: " | ".join(set("|".join(x.dropna()).split("|"))) if not x.isnull().all() else "Unknown",
    "rating": "mean",
    "count": "size"
}).reset_index()
print(movie_title_input_profiles)

