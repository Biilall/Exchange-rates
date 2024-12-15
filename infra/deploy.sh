#!/bin/bash
set -e

BUCKET_NAME=test-bucket-unique123
STACK_NAME=currency-tracker-stack

if [ -z "$BUCKET_NAME" ] || [ -z "$STACK_NAME" ]; then
  echo "Usage: ./deploy.sh <bucket-name> <stack-name>"
  exit 1
fi

zip -r function.zip src
aws s3 cp function.zip s3://$BUCKET_NAME/function.zip

aws cloudformation deploy \
  --template-file infra/template.yaml \
  --stack-name $STACK_NAME \
  --region us-east-1 \
  --capabilities CAPABILITY_NAMED_IAM

