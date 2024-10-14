# README - How to create the python webclient container

## Test locally
1. Build the Docker image: Navigate to the root of your project directory (where your Dockerfile is located) and build the Docker image with the following command:

```bash
docker build . -t python-webclient
```

2. Run the Docker container: Once the build is complete, run the container with:

```bash
docker run -p 8000:8000 python-webclient
```

This will map port 8000 of the container to port 8000 on your local machine.

3. Access the web server: Open your browser and go to http://localhost:8000 to see your web server running with the index.html and style.css.

## Run on Red Hat OpenShift on IBM Cloud
