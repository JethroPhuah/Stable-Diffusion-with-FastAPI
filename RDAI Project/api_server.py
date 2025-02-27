import asyncio
from fastapi import FastAPI
from pydantic import BaseModel
import model_server 

app = FastAPI()

class Article(BaseModel):
    txt: str

@app.post("/generate-image/")
async def generate_image(data: Article):
    """Accepts text input and returns generated image path."""
    model = model_server.MyModel()
    emb = model.generate_image([data.txt])
    return {"generated_image_paths": emb}

# To run the server: uvicorn api_server:app --reload
