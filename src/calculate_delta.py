from datetime import datetime, timedelta
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("ExchangeRates")

def get_rates_with_delta():
    today = datetime.utcnow().strftime("%Y-%m-%d")
    yesterday = (datetime.utcnow() - timedelta(days=1)).strftime("%Y-%m-%d")

    currency_codes = fetch_all_currency_codes()

    result = []
    for currency_code in currency_codes:
        today_rates = fetch_rates_by_date(today, currency_code)
        yesterday_rates = fetch_rates_by_date(yesterday, currency_code)

        for currency, today_rate in today_rates.items():
            yesterday_rate = yesterday_rates.get(currency, None)
            change = today_rate - yesterday_rate if yesterday_rate else None
            result.append({
                "currency": currency,
                "rate": str(today_rate),
                "change": str(change) if change is not None else None 
            })
    
    return result


def fetch_rates_by_date(date, currency_code):
    response = table.query(
        KeyConditionExpression="#c = :currency_code and #d = :date", 
        ExpressionAttributeNames={
            "#c": "currency_code", 
            "#d": "date" 
        },
        ExpressionAttributeValues={
            ":currency_code": currency_code, 
            ":date": date 
        }
    )
    return {item["currency_code"]: item["rate"] for item in response.get("Items", [])}
    
def fetch_all_currency_codes():
    response = table.scan(
        ProjectionExpression="currency_code"
    )
    return set(item["currency_code"] for item in response.get("Items", []))