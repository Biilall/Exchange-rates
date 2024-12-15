from src.calculate_delta import get_rates_with_delta

def test_get_rates_with_delta():
    deltas = get_rates_with_delta()
    assert isinstance(deltas, list)
    for item in deltas:
        assert "currency" in item
        assert "rate" in item
        assert "change" in item