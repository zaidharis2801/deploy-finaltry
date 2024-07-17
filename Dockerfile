# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set environment variables
ENV OPENAI_API_KEY=sk-proj-3b3GU5akFxFYZTOLTYoIT3Blb
ENV LANGCHAIN_API_KEY=lsv2_pt_c58bf9d2e3664480839f01
ENV LANGCHAIN_TRACING_V2=true

# Expose the port the app runs on
EXPOSE 8000

# Run the FastAPI server
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
