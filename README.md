# Currency Exchange Tracker

This application tracks currency exchange rates using European Central Bank data, storing them in DynamoDB and exposing them through a REST API.

## Features
- Fetch daily exchange rates
- Calculate rate deltas
- Expose REST API for rates and deltas

## Setup
1. Deploy infrastructure using `deploy.sh`.
2. Add the Lambda function code to the specified S3 bucket.
3. Run `aws cloudformation deploy` to create the resources.

## Testing
Run `pytest` from the project root to execute tests.

## Usage
- `/rates`: Get current rates.
- `/rates/delta`: Get rates with deltas.

# docs/architecture.png
(Placeholder: Include an architecture diagram detailing the flow of data between AWS Lambda, DynamoDB, and the REST API Gateway.)

# docs/requirements.md
# Project Requirements

## Business Requirements
- Provide current exchange rates.
- Show how rates have changed since the previous day.

## Technical Requirements
- Python-based Lambda functions.
- Use DynamoDB to store exchange rate data.
- Deployable with AWS CloudFormation or equivalent.
- Include test cases for critical functionality.

## API Endpoints
1. `/rates` - Retrieve current exchange rates.
    ```
    Browser
    - https://3yqkv00gj5.execute-api.us-east-1.amazonaws.com/development/rates 
    Curl
    - curl -X GET https://3yqkv00gj5.execute-api.us-east-1.amazonaws.com/development/rates
    ```
2. `/rates/delta` - Retrieve rates with daily deltas.
    ```
    Browser
    - https://3yqkv00gj5.execute-api.us-east-1.amazonaws.com/development/rates/delta    
    Curl
    - curl -X GET https://3yqkv00gj5.execute-api.us-east-1.amazonaws.com/development/rates/delta

    ```


## AWS Services Used
- AWS Lambda
- DynamoDB
- API Gateway
- CloudFormation
- CloudWatch
- S3 (for deployment)


