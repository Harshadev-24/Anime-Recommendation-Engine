# Anime Recommendation Engine

A machine learning-based Anime Recommendation Engine, implemented in Python, designed to suggest anime titles based on content similarity. This project showcases data exploration, preprocessing, feature engineering, and basic recommendation algorithms using the included anime dataset.

## 📚 Table of Contents

- [Features](#features)
- [MLOps Architecture](#mlops-architecture)
- [Getting Started](#getting-started)
- [API Deployment](#api-deployment)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Results](#results)
- [License](#license)

## 🚀 MLOps Architecture

This project now includes a production-ready MLOps pipeline with:

### FastAPI REST API
- **Endpoint**: `/recommend/{anime_name}` - Get personalized anime recommendations
- **Features**:
  - Fast, async API built with FastAPI
  - Automatic API documentation (Swagger UI at `/docs`)
  - Input validation and error handling
  - Pre-loaded similarity matrix for instant recommendations

### Docker Containerization
- **Dockerfile** included for reproducible deployments
- **Port**: Exposed on `8000`
- **Benefits**: 
  - Consistent environment across development and production
  - Easy deployment to cloud platforms (AWS, GCP, Azure)
  - Isolated dependencies

### Key Components
- `anime-app/main.py` - FastAPI application with recommendation logic
- `anime-app/anime_list.pkl` - Serialized dataframe with similarity scores
- `anime-app/Dockerfile` - Container configuration
- `anime-app/requirements.txt` - API dependencies

## Features

- **Data source:** Uses `anime.csv` (Kaggle anime dataset).
- **Recommendation Algorithms:**
  - Content-based filtering (genre, synopsis, etc.)
  - (Extendable for collaborative filtering)
- **Jupyter Notebook:** All code and explanations in `Anime_Recommendation_Engine.ipynb`.

## Getting Started

1. **Clone the repository:**
   ```bash 
   git clone https://github.com/<your-username>/Anime-Recommendation-Engine.git
   ```
2. **Install requirements:**
   ```bash
   pip install requirements.txt
   ```
3. **Run the notebook:**
- Open `Anime_Recommendation_Engine.ipynb` in Jupyter Notebook, JupyterLab, or Colab.

4. **Dataset:**
- The project includes `anime.csv`. No separate download needed.

- ## 📡 API Deployment

### Local Development

**1. Navigate to the API directory**
```bash
cd anime-app
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the FastAPI server**
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**4. Access the API**
- API: `http://localhost:8000`
- Interactive Docs (Swagger UI): `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

**5. Test the endpoint**
```bash
curl http://localhost:8000/recommend/Naruto
```

### Docker Deployment

**1. Build the Docker image**
```bash
cd anime-app
docker build -t anime-recommendation-api .
```

**2. Run the container**
```bash
docker run -d -p 8000:8000 anime-recommendation-api
```

**3. Verify the deployment**
```bash
curl http://localhost:8000/
```

### API Usage Example

**Request:**
```bash
GET /recommend/Death%20Note
```

**Response:**
```json
{
  "anime": "Death Note",
  "recommendations": [
    "Code Geass",
    "Steins;Gate",
    "Monster",
    "Psycho-Pass",
    "Ergo Proxy"
  ]
}
```

## Project Structure
```
anime-recommendation-engine/
│
├── Anime_Recommendation_Engine.ipynb   # Main notebook with code 
├── /data/anime.csv                          # Anime dataset
├── requirements.txt                    # required libraries
└── README.md                          # Project documentation
├── /anime-app/                       # FastAPI deployment
│   ├── main.py                      # FastAPI application
│   ├── anime_list.pkl               # Serialized data & similarity matrix
│   ├── Dockerfile                   # Container configuration
│   ├── requirements.txt             # API dependencies
│   └── .gitignore                   # API-specific ignores
```

## Results

- **Sample recommendations:**  
  The notebook demonstrates how the system recommends similar anime titles.

  ## 🛠️ Technologies Used

| Category | Technologies |
|----------|-------------|
| **Language** | Python 3.9+ |
| **ML/Data Science** | pandas, NumPy, scikit-learn |
| **NLP** | CountVectorizer, TF-IDF |
| **API Framework** | FastAPI, Uvicorn |
| **Deployment** | Docker |
| **Development** | Jupyter Notebook |
| **Version Control** | Git, GitHub |

## License

Distributed under the MIT License. See `LICENSE` for details.
