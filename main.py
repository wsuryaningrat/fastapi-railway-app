from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from huggingface_hub import login
import os

app = FastAPI()

# Login ke Huggingface pakai token
# login(token=os.getenv("HF_TOKEN"))   

# Load model pipeline sekali saat app start
pretrained_name = "w11wo/indonesian-roberta-base-predict-id"
nlp = pipeline(
    "sentiment-analysis",
    model=pretrained_name,
    tokenizer=pretrained_name
)

# Define request body
class TextRequest(BaseModel):
    text: str

# Endpoint predict
@app.post("/predict")
async def predict_emotion(request: TextRequest):
    prediction = nlp(request.text)
    return {"result": prediction}

# Root endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Indonesian Text Prediction API"}
