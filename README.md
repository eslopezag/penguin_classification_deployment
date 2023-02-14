# Deploying a Machine Learning Model for the Penguins Dataset

This educational project creates a docekrized API that serves a Random Forest model to classify penguin species among Chinstrap, Gentoo, and Adélie according to the [penguins dataset](https://www.openml.org/d/42585).

<img src="https://imgur.com/orZWHly.png" alt="Penguin species in the dataset" width="800"/>

Artwork by [@allison_horst](https://github.com/allisonhorst/palmerpenguins#meet-the-palmer-penguins)

## How to Build the Docker Image

To build the Docker image, run the following command with the `Deployment` folder as the current directory:

```
docker build -t penguin-app .
```

## How to Create and Start the Docker Container

To create the Docker container from the image and start the uvicorn server, run the following command with the `Deployment` folder as the current directory:

```
docker run -p 3000:80 penguin-app
```

## How to Deploy the Application on AWS

Steps to deploy a container on AWS ECS:

1. Create a repository in ECR through the AWS console.

1. Set environment variables with the AWS credentials in PowerShell or linux shell:

        (PowerShell:)
        $env:aws_access_key_id=
        $env:aws_secret_access_key=

        (linux/MAC shell:)
        export aws_access_key_id=
        export aws_secret_access_key=

    Alternatively, store this credentials in a `.aws/credentials` file inside your home folder as per the instructions [here](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#shared-credentials-file).

1. Log in the CLI to ECR:

        aws ecr get-login-password --region [REGION] | docker login --username AWS --password-stdin [AWS ACCOUNT ID].dkr.ecr.[REGION].amazonaws.com

1. Tag the container image with AWS ECR Repository name:

        docker tag [ORIGINAL IMAGE NAME] [AWS ACCOUNT ID].dkr.ecr.[REGION].amazonaws.com/[REPO NAME]:[USER-DEFINED TAG]

1. Push the tagged container to the AWS ECR Repository:

        docker push [AWS ACCOUNT ID].dkr.ecr.[REGION].amazonaws.com/[REPO NAME]:[USER-DEFINED TAG]

1. Create an ECS cluster through the AWS console.

1. Make sure that the security group in front of the cluster instances has specific rules allowing inbound and outbound traffic through TCP port 80.

1. Create an ECS Task through the AWS console using the desired image in the ECR repository.

1. Run the ECS Task.

1. Take note of the Public IP of the instance where the container was deployed and send requests to it.