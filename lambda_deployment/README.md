# Deploying a Machine Learning Model for the Penguins Dataset using AWS Lambda

## How to Build the Docker Image

To build the Docker image, run the following command with this folder (`lambda_deployment`) as the current directory:

```
docker build -t penguin-app .
```

Note that Docker images intended to run a whole API using AWS Lambda are, in general, not expected to be run locally. If you want to get a locally-running docker container that serves the application, you should probably follow the instructions in the [`ecs_deployment` folder](./ecs_deployment/) instead.

## How to Deploy the Application to AWS Lambda

Steps to deploy a container to AWS Lambda:

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

1. Create a Lambda Function through the AWS console specifying it is based on a container image and passing the URI of the image you pushed to ECR (`[AWS ACCOUNT ID].dkr.ecr.[REGION].amazonaws.com/[REPO NAME]:[USER-DEFINED TAG]`).

1. Create an API Gateway through the AWS console using the non-private REST API type and the Regional endpoint type.

1. In the API's default resource (`/`), create a proxy resource (mark the "create as proxy resource" checkbox), configure its corresponding `ANY` method with a Lambda Function Proxy integration type, and pass the name or ARN of the Lambda function you created.

1. In the API Gateway console, click "Actions" and then click "Deploy API". In the "deployment stage" dropdown menu, select "[New Stage]" and in the "stage name" field write "dev". Then click the "Deploy" button.

1. Take note of the invoke URL provided by API Gateway after the deployment and use to send requests to it or to see the documentation.
