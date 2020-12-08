# Serverless ML Workshop

This workshop focusses on deployment of ML models with Serverless APIs (AWS Lambda) and Docker.

- Training a model inside a container
- Packaging the service with an image
- Serving the model with serverless API
- Testing locally
- CI/CD workflow

## Technologies
- Docker + ECR: Container & Registy
- AWS Lambda: Serving API
- SAM: Serverless Framework (optional)
- GitHub Actions: CI/CD

## Project Structure
```
|-- service
     |-- app.py: source code lambda handler
     |-- train.py: to train the model
     |-- Dockerfile: to build the Docker image
     |-- requirements.txt: dependencies
|-- tests
     |-- unit
          |--test_handler.py: unit test/s for lambda handler
|-- tests
|-- template.yaml: A template that defines the application's AWS resources.
```

## Pre-requisites

* **python3.8** (used by this service) or python3 [Installed Python 3](https://www.python.org/downloads/)
* **Docker** - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)
* **awscli** - [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)
* **aws-sam-cli** - [Install SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

### Setup
* AWS account with IAM user & [required permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)
* ECR Repository
(Here's how you create one:)
```$ aws ecr create-repository --repository-name <repo-name> [--image-scanning-configuration scanOnPush=true]```

## Steps
### Build

1. Using Docker
```bash
$ docker build -t docker-lambda ./service
```
2. Using SAM
```bash
$ sam build
```
The SAM CLI builds a docker image from a Dockerfile and then installs dependencies defined in `hello_world/requirements.txt` inside the docker image. The processed template file is saved in the `.aws-sam/build` folder.


### Testing locally

1. Using Docker
```bash
$ docker run -p 8080:8080 docker-lambda

$ curl -XPOST "http://localhost:8080/2015-03-31/functions/function/invocations" -d '{"body": {"data": ".10"}}'
```
2. Using SAM
```bash
$ sam local start-api

$ curl -XPOST http://127.0.0.1:3000/classify -H 'Content-Type: application/json' -d '{"data":".10"}'
```

#### Unit tests

Tests are defined in the `tests` folder in this project. Use PIP to install the [pytest](https://docs.pytest.org/en/latest/) and run unit tests from your local machine.

```bash
$ pip install pytest pytest-mock --user
$ python -m pytest tests/ -v
```

### Deployment

1. Using Docker
```bash
$ aws ecr get-login-password | docker login --username AWS --password-stdin xxxxxxxxxxxx.dkr.ecr.eu-central-1.amazonaws.com

$ docker push xxxxxxxxxxxx.dkr.ecr.eu-central-1.amazonaws.com/docker-lambda:latest
```

2. Using SAM
```bash
sam deploy --guided
```


### Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
aws cloudformation delete-stack --stack-name <stack-name>
```

## Resources

### Model Deployment

* [Deploying a DL Model on AWS](https://github.com/alexeygrigorev/aws-lambda-docker) by [Alexey Grigorev](https://datatalks.club/people/alexeygrigorev.html)
* [Deploying models with Sagemaker](https://github.com/ds-muzalevskiy/sagemaker-docker-deploy) by [Dmitry Muzalevskiy](https://datatalks.club/people/dmitrymuzalevskiy.html)
* [Docker for Machine Learning](https://mlinproduction.com/docker-for-ml-part-1/) series by Luigi Patruno (MLinProduction)
* [Multi-stage Docker build](https://winderresearch.com/a-simple-docker-based-workflow-for-deploying-a-machine-learning-model/)

### Recent Updates on AWS
* [AWS Lambda – Container Image tutorial](https://aws.amazon.com/blogs/aws/new-for-aws-lambda-container-image-support/)
* [Update on AWS lambda - supports 10gb memory 6vcpu cores](https://aws.amazon.com/about-aws/whats-new/2020/12/aws-lambda-supports-10gb-memory-6-vcpu-cores-lambda-functions/)

### Comparison (AWS Lambda vs. ...)
* [Post-update evaluation and tradeoffs](https://dev.to/eoinsha/container-image-support-in-aws-lambda-deep-dive-2keh)
* [Pre-update comparison with Sagemaker](https://towardsdatascience.com/saving-95-on-infrastructure-costs-using-aws-lambda-for-scikit-learn-predictions-3ff260a6cd9d)
* [Alternative workflow - Model deployment](https://medium.com/swlh/how-to-deploy-your-scikit-learn-model-to-aws-44aabb0efcb4)
