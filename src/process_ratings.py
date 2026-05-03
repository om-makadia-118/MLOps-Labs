#!/usr/bin/env python3
"""Clean and validate ratings data."""
import pandas as pd
from pathlib import Path

df = pd.read_csv("data/raw/ratings.csv")

# Remove duplicates, invalid ratings
df_clean = df.drop_duplicates().query("rating >= 0.5 and rating <= 5.0")
df_clean = df_clean[df_clean['user_id'] > 0]

print(f"Raw: {len(df)} → Clean: {len(df_clean)} ratings")
print(f"Users: {df_clean['user_id'].nunique()}, Movies: {df_clean['movie_id'].nunique()}")

Path("data/processed/ratings_clean.csv").parent.mkdir(exist_ok=True)
df_clean.to_csv("data/processed/ratings_clean.csv", index=False)
