# Flask Places Recommendation API

This is a simple Flask application that provides a list of places based on the activities and bucket list places provided in the request. The app is containerized using Docker, allowing you to build and run it easily.

## Features
- POST endpoint `/recommendations` that accepts a list of activities and bucket list places and returns a list of recommended places.

## Requirements

Before you begin, make sure you have the following installed:
- [Docker](https://docs.docker.com/get-docker/) (for containerization)

## Getting Started

Follow the instructions below to build and run the application inside a Docker container.

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/Dcoders-CeylonScape/Datathon-Model.git
cd Datathon-Model
```

### 2. Build the Docker Image

Use the following command to build the Docker image:

```bash
docker build -t recommendations-app .
```

### 3. Run the Docker Container

Use the following command to build the Docker image:

```bash
docker run -p 8080:5000 recommendations-app
```

This command maps port 8080 on your local machine to port 5000 in the container so that you can access the app from your machine.

### 4. Access the API

Once the container is running, you can access the API using `curl` or Postman.

```bash
curl -X POST http://127.0.0.1:5000/recommendations -H "Content-Type: application/json" -d '{"activities": ["beach", "museum"], "bucket_list": ["Galle", "Anuradhapura"]}'
```

### 5. Stopping the Docker Container

To stop the running container, press `Ctrl + C` in the terminal where the container is running, or list and stop the container using:

```bash
docker ps
docker stop <container_id>
```
