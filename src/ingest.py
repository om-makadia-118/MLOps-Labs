#!/usr/bin/env python3
"""Generate synthetic MovieLens ratings data."""
import pandas as pd
import numpy as np
from pathlib import Path

np.random.seed(42)  # Reproducible

# Generate 2,000 ratings (user_id, movie_id, rating 0-5.0)
users = np.random.randint(1, 501, 2000)
movies = np.random.randint(1, 1001, 2000)
ratings = np.round(np.random.uniform(0.5, 5.0, 2000), 1)

df = pd.DataFrame({
    'user_id': users,
    'movie_id': movies, 
    'rating': ratings
})

Path("data/raw/ratings.csv").parent.mkdir(exist_ok=True)
df.to_csv("data/raw/ratings.csv", index=False)
print(f"Generated {len(df)} ratings → data/raw/ratings.csv")
