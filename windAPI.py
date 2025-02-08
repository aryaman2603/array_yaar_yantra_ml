from fastapi import FastAPI
import pandas as pd
from io import StringIO
import requests

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all domains (change this in production!)
    allow_credentials=True,
    allow_methods=["*"],  # Allow GET, POST, etc.
    allow_headers=["*"],  # Allow all headers
)


# GitHub Raw CSV URL
CSV_URL = "https://raw.githubusercontent.com/AshmanSodhi/array_yaar_yantra_ml/refs/heads/main/efficiency_data.csv"

@app.get("/")
def read_root():
    return {"message": "CSV API is running!"}

@app.get("/data")
def get_csv_data():
    try:
        # Fetch CSV from GitHub
        response = requests.get(CSV_URL)
        response.raise_for_status()
        
        # Read CSV into Pandas DataFrame
        df = pd.read_csv(StringIO(response.text))
        
        # Convert to JSON
        data_json = df.to_dict(orient="records")
        
        return {"data": data_json}

    except Exception as e:
        return {"error": str(e)}

