import os
import torch
from diffusers import StableDiffusion3Pipeline

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define relative path for sd2_model
model_path = os.path.join(BASE_DIR, "sd2_model")

# Ensure the directory exists
os.makedirs(model_path, exist_ok=True)

pipe = StableDiffusion3Pipeline.from_pretrained("tensorart/stable-diffusion-3.5-medium-turbo", torch_dtype=torch.float16,)
                                                
pipe = pipe.to("cuda")

# Saves the model locally
pipe.save_pretrained(model_path) 

print(f"Model saved at: {model_path}")
