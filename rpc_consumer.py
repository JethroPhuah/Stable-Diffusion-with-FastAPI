import asyncio
from model_server import MyModel

if __name__ == "__main__":
    model = MyModel()
    user_prompt = input("Enter a text prompt: ")
    generated_images = model.generate_image([user_prompt])
    print("Generated images saved at:", generated_images)

