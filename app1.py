from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

model = joblib.load("rainfallprediction4.joblib")


class RainfallInput(BaseModel):
    cloud: float
    humidity: float
    windspeed: float
    dewpoint: float
    day: int
    pressure: float
    maxtemp: float
    mintemp: float
    temparature: float
    sunshine: float


@app.get("/")
def home():
    return {"message": "Rainfall Prediction API Running"}


@app.post("/predict")
def predict(data: RainfallInput):

    input_data = pd.DataFrame([{
        "cloud": data.cloud,
        "humidity": data.humidity,
        "windspeed": data.windspeed,
        "dewpoint": data.dewpoint,
        "day": data.day,
        "pressure": data.pressure,
        "maxtemp": data.maxtemp,
        "mintemp": data.mintemp,
        "temparature": data.temparature,
        "sunshine": data.sunshine
    }])

    prediction = float(model.predict(input_data)[0])

    return {
        "rainfall_probability": prediction
    }