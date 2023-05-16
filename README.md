# Deploying a Machine Learning Model for the Penguins Dataset

This educational project shows how to create and deploy a docekrized API that serves a Random Forest model to classify penguin species among Chinstrap, Gentoo, and Adélie according to the [penguins dataset](https://www.openml.org/d/42585).

<img src="https://imgur.com/orZWHly.png" alt="Penguin species in the dataset" width="800"/>

Artwork by [@allison_horst](https://github.com/allisonhorst/palmerpenguins#meet-the-palmer-penguins)

The main objective of the project is to demonstrate the use of the following technologies:

- FastAPI
- Docker
- AWS Elastic Container Service (ECS)
- AWS Lambda

If you're only interested in a FastAPI example, you should see [this file](./ecs_deployment/main.py). If, in addition, you're interested in how to dockerize that FastAPI application, you should go to the [`ecs_deployment` folder](./ecs_deployment/) and follow the instructions there up to the "How to Create and Start the Docker Container" section.

If you're also interested in deploying the dockerized application to AWS, you should decide whether you want to use ECS or Lambda and follow the instructions in the appropriate folder:

- [`ecs_deployment` folder](./ecs_deployment/)
- [`lambda_deployment` folder](./lambda_deployment/)
