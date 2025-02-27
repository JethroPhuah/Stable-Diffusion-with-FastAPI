# Stable Diffusion FastAPI Server

This project provides an API wrapper around a Stable Diffusion model using FastAPI, enabling image generation via HTTP requests. The model is containerized using Docker for easy deployment.

## Features
- Uses PyTorch with CUDA acceleration for fast inference.
- Runs a FastAPI server to handle image generation requests.
- Generates images from text prompts and saves them inside the container.
- Fully containerized with Docker and supports GPU acceleration.

## Prerequisites
Ensure you have the following installed:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- NVIDIA GPU with CUDA support (for faster processing)
- NVIDIA Container Toolkit ([setup guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html))

## Getting Started
### 1. Clone the repository
```sh
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2. Build a pretrained model
Run the following command to build and save the pretrained model to the folder 'sd2_model'
```sh
python model.py
```

### 3. Build and start the container
Run the following command to build the Docker image:
```sh
docker-compose build
```
Then, start the server:
```sh
docker-compose up
```
This will launch a FastAPI server on `http://localhost:8000`.

### 4. Run the test script
Once the container is running, open another terminal and execute:
```sh
python test.py
```
This script sends a request to the API to generate an image.

## API Usage
After starting the container, you can manually test the API using:
```sh
curl -X POST "http://localhost:8000/generate-image/" -H "Content-Type: application/json" -d '{"prompt": "A fantasy landscape at sunset"}'
```
The generated image will be saved inside the `output/` directory in your local directory.


## Stopping the Server
To stop the running container, use:
```sh
docker-compose down
```

## Troubleshooting
- If you see an error related to CUDA, ensure that your GPU drivers and NVIDIA Container Toolkit are correctly installed.
- If the build process takes too long, ensure that your model files are properly copied or mounted using volumes in `docker-compose.yml`.
- For permission issues, try running `sudo docker-compose up` if on Linux.

---

Enjoy generating images with Stable Diffusion! 🚀

