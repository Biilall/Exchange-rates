import requests
from decimal import Decimal
import boto3
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("ExchangeRates")

def fetch_exchange_rates():
    url = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"
    response = requests.get(url)
    response.raise_for_status()
    data = response.text
    rates = parse_rates(data)
    store_exchange_rates (rates)
    return convert_decimal_to_str(rates)

def parse_rates(data):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(data)
    namespace = {"ns": "http://www.ecb.int/vocabulary/2002-08-01/eurofxref"}
    rates = {}
    for cube in tree.findall(".//ns:Cube[@currency]", namespace):
        rates[cube.attrib["currency"]] = Decimal(cube.attrib["rate"])
    return rates

def store_exchange_rates(rates):
    for currency, rate in rates.items():
        saved = table.put_item(
            Item={
                "currency_code": currency,
                "date": datetime.utcnow().strftime("%Y-%m-%d"),
                "rate": rate
            }
        )

def convert_decimal_to_str(rates):
    return {currency: str(rate) if isinstance(rate, Decimal) else rate for currency, rate in rates.items()}