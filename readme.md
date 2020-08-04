# Ready to use configuration mlflow tracking server + local S3 storage based on Docker and Minio

## Prerequisites:

For mlflow tracking server machine:

* [Docker](https://docs.docker.com/get-docker/)
* [Docker-compose](https://docs.docker.com/compose/install/)

For client machine:

* just install [mlflow](https://www.mlflow.org/docs/latest/quickstart.html) and [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) libraries to your environment

It's possible to use the same machine as the server and the client

## Configurations

[Client and server are the same machine](#configuration-client-and-server-are-the-same-machine)  
[Server on remote machine](#configuration-server-is-remote-machine)


## Configuration Client and Server are the same machine

1. Go to the directory, where your server will run and clone project

```shell script
git clone https://github.com/leoromanovich/mlflow_tracking_server && cd mlflow_tracking_server
```

2. Go to mlflow_server directory

```shell script
cd mlflow_server
```

3. Run server

```shell script
sudo docker-compose up --build
```

4. Server is ready, so [add few lines to client code](#Client-configuration)
5. Check `localhost:5555` for MLflow server and `localhost:9001` for Minio 
6. Enjoy!


## Configuration Server is remote machine

1. Connect to your remote machine
2. Go to the directory, where your server will run and clone project

```shell script
git clone https://github.com/leoromanovich/mlflow_tracking_server && cd mlflow_tracking_server
```

3. Go to mlflow_server directory

```shell script
cd mlflow_server
```

4. Run server

```shell script
sudo docker-compose up --build
```

5. Server is ready, so [add few lines to client code](#Client-configuration)

6. Check `your_server_ip:5555` for MLflow server and `your_server_ip:9001` 
7. Enjoy!

## Client configuration

Add this lines to your experiment

```python
import os
import mlflow

# Use IP of your remote machine here
# Don't change if client and server is the same machine
server_ip = '0.0.0.0'

os.environ['AWS_ACCESS_KEY_ID'] = 'minio'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'minio123'
os.environ['MLFLOW_S3_ENDPOINT_URL'] = f'http://{server_ip}:9001'

mlflow.set_tracking_uri(f"http://{server_ip}:5555")
mlflow.set_experiment("awesome-experiment")
```

## What if I want to change

1. Aritfact-bucket and save artifacts there?

Open [docker-compose.yml](/mlflow_server/docker-compose.yml) file and change all "mlflow-artifacts" entries to "new_bucket_name"



## Acknowledgments

[Mikhail Knyazev](https://github.com/9dogs)  
[Dmitry Kozlov](https://github.com/dkozlov)  
[OCRV](http://www.ocrv.ru/)
