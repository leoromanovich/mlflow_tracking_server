import mlflow
from mlflow import log_metric, log_param, log_artifact, set_tags
import matplotlib.pyplot as plt
import numpy as np
import os

# Use IP of your remote machine here
server_ip = "0.0.0.0"

os.environ['AWS_ACCESS_KEY_ID'] = 'minio'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'minio123'
os.environ['MLFLOW_S3_ENDPOINT_URL'] = f"http://{server_ip}:9001"

mlflow.set_tracking_uri(f"http://{server_ip}:5555")
mlflow.set_experiment("awesome-experiment")

#################################
#### YOUR EXPERIMENT IS HERE ####
#################################

run_name = 'Awesome experiment name'
run_tags = {'dataset': 'Awesome Dataset',
            'author': 'Awesome Name'}

with mlflow.start_run(run_name=run_name, nested=False) as run:
    log_param('model', "Awesome model")
    set_tags(run_tags)
    log_metric("accuracy", 0.9)

    # Check for simple artifacts writing
    with open("output.txt", "w") as f:
        f.write("This model is awesome!")

    log_artifact("output.txt")
    plt.imsave('img.png', np.zeros(shape=(20,20)))
    log_artifact('img.png')

    # Clear directory
    os.remove('img.png')
    os.remove('output.txt')




