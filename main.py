from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from huggingface_hub import login
 
# Init FastAPI app
app = FastAPI()

# Load model pipeline once when app starts
pretrained_name = "w11wo/indonesian-roberta-base-prdect-id"
nlp = pipeline(
    "sentiment-analysis",
    model=pretrained_name,
    tokenizer=pretrained_name
)

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
