# docker
Welcome to my GitHub repository dedicated to Docker!
<br>
Here, you'll find the source code of the project, which involves the containerization of a streamlit diabetes prediction web app.

## Table of Contents
 - [Overview]()
 - [App Test on Local Host](#app-test-on-local-host)
 - [Docker Installation](#docker-installation)
 - [Docker Setup](#docker-setup)
 - [Dockerfile Setup](#dockerfile-setup)
 - [Build Docker Image](#build-docker-image)
 - [Run Docker Image as a Container](#run-docker-image-as-a-container)
 - [Push Docker Image to Docker Hub](#push-docker-image-to-docker-hub)
 - [Notes]()
 - [License]()

## App Test on Local Host
1. Clone the repository:

    ```bash
    git clone https://github.com/umairsiddique3171/diabetes_prediction_web_app_using_streamlit.git
    cd diabetes_prediction_web_app_using_streamlit
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv env
    .\env\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

5. Access the app in your browser at returned local host (e.g. `http://localhost:80`).
## Docker Installation
* For Docker Desktop installation, please visit [here](https://www.docker.com/products/docker-desktop/).
* To see system requirements, please visit official Docker Documentation [here](https://docs.docker.com/desktop/).

## Docker Setup 
To check docker installation in your system, run following command in your terminal : 
```
PS C:\Users\US593> docker
```
Terminal should be returning lists of docker commands.

## Dockerfile Setup 
Setup "Dockerfile" as mentioned [here]().

## Build Docker Image 
To build docker image, use the following command in your terminal : 
```
docker build -t <image_name>:<tag> .
```
```
docker build -t diabetes_app:v1.0 .
```
To see whether docker image has been built or not, use the following command in your terminal : 
```
docker images
```
This will show all the docker images in your local host.
<br>
If you want to remove docker image, you can use the following command in your terminal : 
```
docker rmi -f <image_name>:<tag>
docker rmi -f <image_id>
```
If you want to rename docker image, you can use the following command in your terminal : 
```
docker tag <image_name>:<tag> <new_name>:<tag>
```

## Run Docker Image as a Container
To run docker image as a container, type the following command in your terminal : 
```
docker run -p <host_port>:<container_port> <image_name>:<tag>
docker run -p <host_port>:<container_port> <image_id>
```
```
docker run -p 80:80 diabetes_app:v1.0
```
In Windows, basically, this url `http://0.0.0.0:80` usually doesn't work. Try running `http://localhost/` in your browser.
<br>
To check whether the container is running, type the following command in your terminal : 
```
docker ps
```
To stop the container from running, type the following command in your terminal : 
```
docker stop <container_id>
```
To view stopped containers, type the following command in your terminal : 
```
docker ps -a
```
To delete all the stopped containers, as they take up some space, type the following command in your terminal : 
```
docker container prune
```

## Push Docker Image to Docker Hub

To push a Docker image to Docker Hub, follow these steps:

1. **Login to Docker Hub**: 

    Before pushing the image, you need to authenticate yourself with your Docker Hub credentials. Use the following command:
   
    ```
    docker login
    ```

    After running this command, you'll be prompted to enter your Docker Hub username and password.

2. **Tag the Docker Image**:

    Before pushing the image, you need to tag it with your Docker Hub username and the repository name. This is done using the following command:

    ```
    docker tag <image_name>:<tag> <username>/<repository>:<tag>
    ```
    ```
    docker tag diabetes_app:v1.0 umairsiddique3171/diabetes_app:v1.0
    ```

3. **Push the Docker Image**:

    Finally, push the tagged image to Docker Hub using the following command:

    ```
    docker push <username>/<repository>:<tag>
    ```
    ```
    docker push umairsiddique3171/diabetes_app:v1.0
    ```
    This command will push the tagged image to your Docker Hub repository. Make sure you have appropriate permissions to push to the repository.




