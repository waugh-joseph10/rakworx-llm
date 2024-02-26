# Use the official Python image with your specific version
FROM python:3.11.4

# Install curl (if not already available in the base image)
RUN apt-get update && apt-get install -y curl

# Set the working directory inside the container
WORKDIR /usr/src/app

# Download a file from a given URL
RUN curl -L "https://huggingface.co/TheBloke/Llama-2-13B-chat-GGUF/blob/main/llama-2-13b-chat.Q4_K_M.gguf" -o llama-2-13b-chat.Q4_K_M.gguf

# Copy the requirements.txt file into the container
COPY requirements.txt ./

# Install any dependencies in the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code into the container
COPY . .

# Command to run on container start
CMD ["python", "./test.py"]
