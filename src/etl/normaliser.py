def normalize_year(year):
    """Convert year values into clean integer format."""
    if year is None:
        return None

    year_str = str(year).strip()

    if year_str == "":
        return None

    year_str = year_str.replace("FY-", "")
    year_str = year_str.replace("FY", "")
    year_str = year_str.strip()

    try:
        return int(float(year_str))
    except ValueError:
        return None


def normalize_ticker(ticker):
    """Convert ticker symbols into clean uppercase format."""
    if ticker is None:
        return None

    ticker_str = str(ticker).strip().upper()

    if ticker_str == "":
        return None

    ticker_str = ticker_str.replace(".NS", "").replace(".BO", "")
    ticker_str = ticker_str.replace(" ", "")

    return ticker_str