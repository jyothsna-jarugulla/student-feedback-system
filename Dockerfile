FROM python:3.9

WORKDIR /app

# Copy all files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (important for Flask apps)
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
