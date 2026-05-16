# Use an official PyTorch image with CUDA
FROM pytorch/pytorch:2.5.1-cuda12.1-cudnn9-runtime

# Set the working directory
WORKDIR /opt/rdaiproj

# Copy the model directory into the container
COPY ./sd2_model /opt/sd2_model

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Expose the FastAPI port
EXPOSE 8000

# Run the FastAPI server
CMD ["uvicorn", "api_server:app", "--host", "0.0.0.0", "--port", "8000"]
