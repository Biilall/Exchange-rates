from src.fetch_rates import fetch_exchange_rates, parse_rates

def test_fetch_exchange_rates():
    rates = fetch_exchange_rates()
    assert isinstance(rates, dict)
    assert "USD" in rates
    assert rates["USD"] > 0