#!/bin/bash

# Pull the Docker image
docker pull savatar101/marker-api:0.3

# Check if GPU is available
if command -v nvidia-smi &> /dev/null
then
    # Run the Docker container with GPU support
    docker run --gpus all -p 8000:8000 savatar101/marker-api:0.3
else
    # Run the Docker container without GPU support
    docker run -p 8000:8000 savatar101/marker-api:0.3
fi
