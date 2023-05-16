# Deploying a Machine Learning Model for the Penguins Dataset using AWS ECS

## How to Build the Docker Image

To build the Docker image, run the following command with this folder (`ecs_deployment`) as the current directory:

```
docker build -t penguin-app .
```

## How to Create and Start the Docker Container

To create the Docker container from the image and start the uvicorn server locally, run the following command:

```
docker run -p 3000:80 penguin-app
```

Then you can go to http://localhost:3000/docs to see the API's documentation and test its endpoints.

## How to Deploy the Application to AWS ECS

Steps to deploy a container to AWS ECS:

1. Create a repository in ECR through the AWS console.

1. Set environment variables with the AWS credentials in PowerShell or linux shell:

        (PowerShell:)
        $env:aws_access_key_id=
        $env:aws_secret_access_key=

        (linux/MAC shell:)
        export aws_access_key_id=
        aws_secret_access_key=

    Alternatively, store this credentials in a `.aws/credentials` file inside your home folder as per the instructions [here](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#shared-credentials-file).

1. Login the CLI to ECR:

        aws ecr get-login-password --region [REGION] | docker login --username AWS --password-stdin [AWS ACCOUNT ID].dkr.ecr.[REGION].amazonaws.com

1. Tag the image with the AWS ECR Repository name:

        docker tag [ORIGINAL IMAGE NAME] [AWS ACCOUNT ID].dkr.ecr.[REGION].amazonaws.com/[REPO NAME]:[USER-DEFINED TAG]

1. Push the tagged container to the AWS ECR Repository:

        docker push [AWS ACCOUNT ID].dkr.ecr.[REGION].amazonaws.com/[REPO NAME]:[USER-DEFINED TAG]

1. Create an ECS cluster through the AWS console.

1. Create an ECS Task through the AWS console using the desired image in the ECR repository.

1. Run the ECS Task.

1. Take note of the Public IP of the instance where the container was deployed and send requests to it.