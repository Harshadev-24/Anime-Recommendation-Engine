from fastapi import FastAPI, HTTPException
import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = FastAPI()

# Global variables to hold our data and model
df = None
similarity = None

def load_model():
    """
    Loads the dataframe and calculates the similarity matrix on startup.
    This avoids shipping a 1GB pickle file.
    """
    global df, similarity
    
    print("Loading data...")
    # Load the processed dataframe
    # Ensure 'anime_list.pkl' is in the same folder
    df = pickle.load(open('anime_list.pkl', 'rb'))
    
    print("Calculating similarity matrix... (This may take 10-20 seconds)")
    
    # Re-create the CountVectorizer and Similarity Matrix
    # We use the 'combined_features' column you created in your notebook
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df["combined_features"])
    
    # Compute the cosine similarity
    similarity = cosine_similarity(count_matrix)
    
    print("Model loaded and ready!")

# Trigger the loading function when the app starts
load_model()

@app.get("/")
def home():
    return {"message": "Anime Recommendation API is Live!"}

@app.get("/recommend/{anime_name}")
def recommend(anime_name: str):
    global df, similarity
    
    # 1. Handle case sensitivity (Optional but good UX)
    # We try to find an exact match first
    if anime_name not in df['Name'].values:
        # If not found, you might want to return a helpful error
        raise HTTPException(status_code=404, detail=f"Anime '{anime_name}' not found in database.")

    # 2. Find the index of the anime
    # We use .iloc[0] to get the actual integer index
    anime_index = df[df['Name'] == anime_name].index[0]

    # 3. Get similarity scores for this anime
    distances = similarity[anime_index]

    # 4. Sort and get top 5 (skipping the first one which is itself)
    # enumerate(distances) gives us pairs of (index, score)
    anime_list_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    # 5. Fetch titles
    recommendations = []
    for i in anime_list_indices:
        # i[0] is the index of the anime in the dataframe
        recommended_title = df.iloc[i[0]]['Name']
        recommendations.append(recommended_title)

    return {
        "input_anime": anime_name,
        "recommendations": recommendations
    }

# This block allows you to run it directly with 'python main.py'
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)