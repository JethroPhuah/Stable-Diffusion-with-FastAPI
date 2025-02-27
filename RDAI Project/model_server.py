import torch
from diffusers import StableDiffusion3Pipeline
from typing import List
import os

class MyModel:
    def __init__(self):
        # Load your Stable Diffusion model here
        # self.model = StableDiffusion3Pipeline.from_pretrained("tensorart/stable-diffusion-3.5-medium-turbo", torch_dtype=torch.float16,).to("cuda")
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        # Define relative path from the script's directory
        model_path = os.path.join(BASE_DIR, "../sd2_model")

        # Normalize the path to avoid issues
        model_path = os.path.normpath(model_path)

        print("Model Path:", model_path)  # Debugging
        
        self.model = StableDiffusion3Pipeline.from_pretrained(
            model_path, 
            torch_dtype=torch.float16
        ).to("cuda")
         # Ensure the output directory exists
        self.output_dir = "./generated_images"
        os.makedirs(self.output_dir, exist_ok=True)
    
    def generate_image(self, prompts: List[str]) -> List[str]:
            """ Generate images from text prompts."""
            print(f"Received {len(prompts)} text prompt(s).")
            image_batch = []

            for prompt in prompts:
                image = self.model(
                    prompt,
                    num_inference_steps=8,
                    guidance_scale=1.5,
                    height=1024,
                    width=768
                ).images[0]

                image_path = os.path.join(self.output_dir, f"{prompt}.png")
                image.save(image_path)
                image_batch.append(image_path)

            print(f"Generated {len(image_batch)} images.")
            return image_batch