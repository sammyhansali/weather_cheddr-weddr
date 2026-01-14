REPO=cheddr-weddr-airflow
ECR=345204681263.dkr.ecr.us-east-1.amazonaws.com/$REPO
REGION=us-east-1
TAG=1.0

aws login

aws ecr create-repository \
    --repository-name $REPO \
    --region $REGION

aws ecr get-login-password --region $REGION \
    | docker login --username AWS --password-stdin $ECR

docker build \
    -t cheddr-weddr-airflow:$TAG \
    -f airflow/Dockerfile .

docker tag $REPO:$TAG $ECR:$TAG
docker tag $REPO:$TAG $ECR:latest

docker push $ECR:$TAG
docker push $ECR:latest
