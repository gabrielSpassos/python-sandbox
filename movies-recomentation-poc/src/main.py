from sentence_transformers import SentenceTransformer
import re
import pandas as pd
import chromadb
import os
import shutil
import time

def clean_title(title):
    return re.sub('\(\d+\)$', '', title).strip()


def get_year_on_title(title):
    match = re.search('\(\d+\)$', title)
    if match:
        return match.group(0).replace("(", "").replace(")", "")

    return None

print("\n📥 Cleaning data...")
shutil.rmtree("./chroma_db", ignore_errors = True)
os.mkdir("./chroma_db")

print("\n📥 Loading data...")
movies_df = pd.read_csv("./resources/movies.csv")

movies_df["year"] = movies_df["title"].apply(get_year_on_title)
movies_df["title"] = movies_df["title"].apply(clean_title)

ratings_df = pd.read_csv("./resources/ratings.csv")
tags_df = pd.read_csv("./resources/tags.csv")

merged = pd.merge(movies_df, ratings_df, left_on='movieId', right_on='movieId', how='left')

# Count how many times each movieId is present in the merged DataFrame
merged_with_count = merged.groupby("movieId").size().reset_index(name='count').sort_values(by='count', ascending=False)

final_df = pd.merge(merged, merged_with_count, left_on='movieId', right_on='movieId', how='left')

# Create movie_title_input_profiles without the count
movie_title_input_profiles = final_df.groupby("movieId").agg({
    "title": lambda x: x.drop_duplicates().iloc[0] if not x.isnull().all() else "Unknown",
    "year": lambda x: x.drop_duplicates().iloc[0] if not x.isnull().all() else "Unknown",
    "genres": lambda x: " | ".join(set("|".join(x.dropna()).split("|"))) if not x.isnull().all() else "Unknown",
    "rating": "mean",
    "count": "size"
}).reset_index()
print(movie_title_input_profiles.head())

print("🔍 Loading AI model...\n")
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

print("💾 Connecting to ChromaDB...\n")
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="user_preferences")

print("🚀 Saving embeddings to ChromaDB...\n")

for index, row in movie_title_input_profiles.iterrows():
    movie_id = str(row["movieId"])
    rating = float(f"{row['rating']:.2f}")
    movie_description = f"Year: {row['year']} | Id: {row['movieId']} | Genres: {row['genres']} | Rating: {rating} | Views: {row['count']}"
    # print(movie_description)
    embedding_movie = model.encode(movie_description).tolist()

    collection.add(
        ids=[movie_id],
        embeddings=[embedding_movie],
        metadatas=[{"description": movie_description, "title": row['title'], "year": row['year'], "genres": row['genres'], "rating": rating, "views": row["count"]}]
    )

print("✅ Embeddings successfully stored in ChromaDB!\n")

while True:
    question = input("\n🎬 Ask me something: ")
    query_embedding = model.encode(question)
    results = collection.query(query_embeddings=query_embedding, n_results=1)
    print(results)
