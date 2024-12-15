import json
from .fetch_rates import fetch_exchange_rates
from .calculate_delta import get_rates_with_delta

def lambda_handler(event, context):
    path = event.get("path", "")

    if path == "/rates":
        return {
            "statusCode": 200,
            "body": json.dumps(fetch_exchange_rates())
        }
    elif path == "/rates/delta":
        return {
            "statusCode": 200,
            "body": json.dumps(get_rates_with_delta())
        }
    else:
        return {
            "statusCode": 404,
            "body": json.dumps({"message": "Not Found"})
        }