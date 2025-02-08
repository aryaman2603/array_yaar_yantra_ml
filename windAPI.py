from fastapi import FastAPI
import pandas as pd
import requests

app = FastAPI()

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
        df = pd.read_csv(pd.compat.StringIO(response.text))
        
        # Convert to JSON
        data_json = df.to_dict(orient="records")
        
        return {"data": data_json}

    except Exception as e:
        return {"error": str(e)}

