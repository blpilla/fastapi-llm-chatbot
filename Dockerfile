# Use Python 3.12.5 full image as the base image
FROM python:3.12.5

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir langchain fastapi uvicorn

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV LLAMA_API_KEY your-api-key-here

# Run main.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]