import pandas as pd
import re


def clean_title(title):
    return re.sub('\(\d+\)$', '', title).strip()


def get_year_on_title(title):
    match = re.search('\(\d+\)$', title)
    if match:
        return match.group(0).replace("(", "").replace(")", "")

    return None


movies_df = pd.read_csv("./resources/movies.csv")

movies_df["year"] = movies_df["title"].apply(get_year_on_title)
movies_df["title"] = movies_df["title"].apply(clean_title)

ratings_df = pd.read_csv("./resources/ratings.csv")

merged = pd.merge(movies_df, ratings_df, left_on='movieId', right_on='movieId', how='left')
# print(merged.head())

# Count how many times each movieId is present in the merged DataFrame
merged_with_count = merged.groupby("movieId").size().reset_index(name='count').sort_values(by='count', ascending=False)
# print(merged_with_count.head())

final_df = pd.merge(merged, merged_with_count, left_on='movieId', right_on='movieId', how='left')
# print(final_df.head())

# Create movie_title_input_profiles without the count
movie_title_input_profiles = final_df.groupby("movieId").agg({
    "title": lambda x: x.drop_duplicates().iloc[0] if not x.isnull().all() else "Unknown",
    "year": lambda x: x.drop_duplicates().iloc[0] if not x.isnull().all() else "Unknown",
    "genres": lambda x: " | ".join(set("|".join(x.dropna()).split("|"))) if not x.isnull().all() else "Unknown",
    "rating": "mean",
    "count": "size"
}).reset_index()
print(movie_title_input_profiles.head())

for index, row in movie_title_input_profiles.iterrows():
    movie_id = str(row["movieId"])
    print(movie_id)
    print(row["title"])
    print(row["year"])
    print(row["genres"])
    print(row['rating'])
    print(row['count'])
    print("------")