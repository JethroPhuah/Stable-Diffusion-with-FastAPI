import torch
print(torch.cuda.is_available())  # Returns True if CUDA is available
print(torch.cuda.current_device())  # Returns the current CUDA device ID
print(torch.cuda.get_device_name(torch.cuda.current_device()))  # Get the name of the GPU
print(torch.version.cuda)
print(torch.__version__)