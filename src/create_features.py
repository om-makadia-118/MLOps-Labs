#!/usr/bin/env python3
"""Compute user similarity features."""
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path

df = pd.read_csv("data/processed/ratings_clean.csv")

# Pivot to user-movie matrix (sparse → dense for similarity)
user_movie = df.pivot_table(
    index='user_id', 
    columns='movie_id', 
    values='rating',
    fill_value=0
)

# Cosine similarity matrix (50x50 for demo)
user_sim = cosine_similarity(user_movie)
user_sim_df = pd.DataFrame(
    user_sim, 
    index=user_movie.index, 
    columns=user_movie.index
)

Path("models/user_similarity.pkl").parent.mkdir(exist_ok=True)
user_sim_df.to_pickle("models/user_similarity.pkl")
print(f"User similarity matrix: {user_sim_df.shape}")
