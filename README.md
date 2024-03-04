# docker

## Installation
* For Docker Desktop installation, please visit [here](https://www.docker.com/products/docker-desktop/).
<br>
* To see system requirements, please visit official Docker Documentation [here](https://docs.docker.com/desktop/).

## Docker Setup 
To check docker installation in your system, run following command in your terminal : 
```
PS C:\Users\US593> docker
```
Terminal should be returning lists of docker commands.

## Dockerfile Setup 
Create a file with name "Dockerfile" and write the code with following steps : 
1.  Use any base image.
2. Copy the local directory containing the application files into the container.
3. Set the working directory inside the container.
4. Install the Python dependencies listed in requirements.txt.
5. Command to run when the container starts.
```
From python:3.8-alpine
COPY ./app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python app.py
```

## Build Docker Image 
To build docker image, use the following command in your terminal : 
```
docker build -t diabetes_app .
```
To see whether docker image has been built or not, use the following command in your terminal : 
```
docker images
```
This will show all the docker images in your local host.
<br>
If you want to remove docker image, you can use the following command in your terminal : 
```
docker image rm -f diabetes_app
```
If you want to rename docker image, you can use the following command in your terminal : 
```
docker tag <previous_name> <new_name>
```

## Run Docker Image as a Container
To run docker image as a container, type the following command in your terminal : 
```
docker run -p <host-port>:<container-port> diabetes_app
```
To check whether the container is running, type the following command in your terminal : 
```
docker ps
```
To stop the container from running, type the following command in your terminal : 
```
docker stop <container-id>
```

## Push Docker Image to Docker Hub

To push a Docker image to Docker Hub, follow these steps:

1. **Login to Docker Hub**: 

    Before pushing the image, you need to authenticate yourself with your Docker Hub credentials. Use the following command:
   
    ```bash
    docker login
    ```

    After running this command, you'll be prompted to enter your Docker Hub username and password.

2. **Tag the Docker Image**:

    Before pushing the image, you need to tag it with your Docker Hub username and the repository name. This is done using the following command:

    ```
    docker tag <image_name>:<tag> <username>/<repository>:<tag>
    ```

    Replace `<image_name>` with the name of your Docker image, `<tag>` with the tag you want to assign to the image, `<username>` with your Docker Hub username, and `<repository>` with the name of the repository you want to push the image to.
    <br>
    In my case, it would be: 
    ```
    docker tag diabetes_app umairsiddique3171/diabetes_app
    ```

3. **Push the Docker Image**:

    Finally, push the tagged image to Docker Hub using the following command:

    ```
    docker push <username>/<repository>:<tag>
    ```
    That is : 
    ```
    docker push umairsiddique3171/diabetes_app
    ```
    This command will push the tagged image to your Docker Hub repository. Make sure you have appropriate permissions to push to the repository.

Following these steps will allow you to push your Docker image to Docker Hub successfully. Make sure to replace placeholders like `<image_name>`, `<tag>`, and `<username>/<repository>` with your actual values.




