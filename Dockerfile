# Use a Node.js and Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install Node.js and npm
RUN apt-get update && apt-get install -y \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

# Copy package.json and install Node.js dependencies
COPY package.json .
RUN npm install

# Copy Python requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Build Tailwind CSS
RUN npm run build

# Expose port
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "-m", "run"]