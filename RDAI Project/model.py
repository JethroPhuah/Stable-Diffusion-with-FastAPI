import torch
from diffusers import StableDiffusion3Pipeline

pipe = StableDiffusion3Pipeline.from_pretrained("tensorart/stable-diffusion-3.5-medium-turbo", torch_dtype=torch.float16,)
                                                
pipe = pipe.to("cuda")

pipe.save_pretrained("./sd2_model")  # Saves the model locally
