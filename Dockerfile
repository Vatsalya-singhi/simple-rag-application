# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Prevent Python from writing .pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies (add more here if your libs need them)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency file first (for better Docker build caching)
# If your repo does not have requirements.txt, create one or change this line.
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Build the vector database once at image build time
# If you want to regenerate the DB on every container start instead,
# move this command into the CMD/ENTRYPOINT section.
# RUN python create_db.py

# Expose Streamlit's default port
EXPOSE 8501

# Streamlit configuration so it works inside Docker
ENV STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_ADDRESS=0.0.0.0 \
    STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Default command to run your Streamlit app
# If your main file is not main.py, change it accordingly.
# CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]


# Run create_db.py first (it will see GEMINI_API_KEY from env),
# then start Streamlit.
CMD ["bash", "-c", "python create_db.py && streamlit run main.py --server.port=8501 --server.address=0.0.0.0"]