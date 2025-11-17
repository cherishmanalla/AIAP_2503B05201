from datetime import datetime


def convert_date_format(date_str):
    """Converts YYYY-MM-DD to DD-MM-YYYY. Returns None for invalid inputs."""
    if not isinstance(date_str, str):
        return None
    try:
        parsed = datetime.strptime(date_str, "%Y-%m-%d")
        return parsed.strftime("%d-%m-%Y")
    except ValueError:
        return None


def test_convert_date_format():
    """AI-generated tests for convert_date_format."""
    # Valid conversions
    assert convert_date_format("2023-10-15") == "15-10-2023"
    assert convert_date_format("2000-01-01") == "01-01-2000"
    assert convert_date_format("1999-12-31") == "31-12-1999"
    assert convert_date_format("2024-02-29") == "29-02-2024"  # leap year
    assert convert_date_format("2025-07-04") == "04-07-2025"

    # Invalid formats
    assert convert_date_format("15-10-2023") is None
    assert convert_date_format("2023/10/15") is None
    assert convert_date_format("20231015") is None
    assert convert_date_format("2023-1-5") is None  # missing padding

    # Invalid dates
    assert convert_date_format("2023-02-30") is None
    assert convert_date_format("2023-13-01") is None
    assert convert_date_format("2023-00-10") is None
    assert convert_date_format("2023-04-31") is None

    # Edge/empty inputs
    assert convert_date_format("") is None
    assert convert_date_format(None) is None
    assert convert_date_format(20231015) is None
    assert convert_date_format([]) is None

    print("All convert_date_format tests passed! ✓")


if __name__ == "__main__":
    test_convert_date_format()
    print("\nFunction converts input format correctly for all test cases ✓")

