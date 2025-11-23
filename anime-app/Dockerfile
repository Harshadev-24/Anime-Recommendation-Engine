# 1. Start with a lightweight Python base image
FROM python:3.9-slim

# 2. Set the working directory inside the container to /app
WORKDIR /app

# 3. Copy the dependencies file first (for better caching)
COPY requirements.txt .

# 4. Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy your code and the data file
COPY main.py .
COPY anime_list.pkl .

# 6. Expose port 8000 (The port your app uses)
EXPOSE 8000

# 7. The command to start the server when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]