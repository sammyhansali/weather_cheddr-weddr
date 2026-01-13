aws login

aws ecr create-repository \
    --repository-name cheddr-weddr-airflow \
    --region us-east-1

aws ecr get-login-password --region us-east-1 \
    | docker login --username AWS --password-stdin \
    345204681263.dkr.ecr.us-east-1.amazonaws.com/cheddr-weddr-airflow

docker tag cheddr-weddr-airflow:latest 345204681263.dkr.ecr.us-east-1.amazonaws.com/cheddr-weddr-airflow
docker push 345204681263.dkr.ecr.us-east-1.amazonaws.com/cheddr-weddr-airflow:latest