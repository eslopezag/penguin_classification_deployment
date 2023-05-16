# Base image:
FROM public.ecr.aws/lambda/python:3.9

# Copy the requirements file:
COPY ./requirements.txt "${LAMBDA_TASK_ROOT}"

# Install dependecies:
RUN pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Copy the current local directory to the image's task folder:
COPY . "${LAMBDA_TASK_ROOT}"

CMD ["main.handler"]
