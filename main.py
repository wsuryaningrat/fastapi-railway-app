from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Init FastAPI app
app = FastAPI()

# Load model pipeline once when app starts
model = pipeline("text-classification", model="w11wo/indonesian-roberta-base-predict-id")

# Define request body
class TextRequest(BaseModel):
    text: str

# Define response route
@app.post("/predict")
async def predict_emotion(request: TextRequest):
    prediction = model(request.text)
    return {"result": prediction}

# Root endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Indonesian Text Prediction API"}
