from src.etl.normaliser import normalize_year, normalize_ticker
from src.etl.loader import clean_dataframe
import pandas as pd


# ---------------- YEAR TESTS ----------------

def test_normalize_year_integer():
    assert normalize_year(2024) == 2024


def test_normalize_year_float():
    assert normalize_year(2024.0) == 2024


def test_normalize_year_string():
    assert normalize_year("2024") == 2024


def test_normalize_year_with_spaces():
    assert normalize_year(" 2024 ") == 2024


def test_normalize_year_fy_space():
    assert normalize_year("FY 2024") == 2024


def test_normalize_year_fy_dash():
    assert normalize_year("FY-2024") == 2024


def test_normalize_year_empty():
    assert normalize_year("") is None


def test_normalize_year_none():
    assert normalize_year(None) is None


def test_normalize_year_invalid_text():
    assert normalize_year("abcd") is None


def test_normalize_year_decimal_string():
    assert normalize_year("2024.0") == 2024


# ---------------- TICKER TESTS ----------------

def test_normalize_ticker_uppercase():
    assert normalize_ticker("reliance") == "RELIANCE"


def test_normalize_ticker_already_uppercase():
    assert normalize_ticker("TCS") == "TCS"


def test_normalize_ticker_ns_suffix():
    assert normalize_ticker("TCS.NS") == "TCS"


def test_normalize_ticker_bo_suffix():
    assert normalize_ticker("INFY.BO") == "INFY"


def test_normalize_ticker_spaces():
    assert normalize_ticker(" hdfc bank ") == "HDFCBANK"


def test_normalize_ticker_mixed_case():
    assert normalize_ticker("Reliance") == "RELIANCE"


def test_normalize_ticker_empty():
    assert normalize_ticker("") is None


def test_normalize_ticker_none():
    assert normalize_ticker(None) is None


def test_normalize_ticker_with_inner_spaces():
    assert normalize_ticker("hdfc life") == "HDFCLIFE"


def test_normalize_ticker_numeric():
    assert normalize_ticker(123) == "123"


# ---------------- DATAFRAME CLEANING TESTS ----------------

def test_clean_dataframe_column_lowercase():
    df = pd.DataFrame({"Company Name": ["ABC"]})
    cleaned = clean_dataframe(df)
    assert "company_name" in cleaned.columns


def test_clean_dataframe_column_space_removed():
    df = pd.DataFrame({"Total Sales": [100]})
    cleaned = clean_dataframe(df)
    assert "total_sales" in cleaned.columns


def test_clean_dataframe_column_dash_replaced():
    df = pd.DataFrame({"Net-Profit": [50]})
    cleaned = clean_dataframe(df)
    assert "net_profit" in cleaned.columns


def test_clean_dataframe_year_column_normalized():
    df = pd.DataFrame({"year": ["FY 2024"]})
    cleaned = clean_dataframe(df)
    assert cleaned.loc[0, "year"] == 2024


def test_clean_dataframe_ticker_column_normalized():
    df = pd.DataFrame({"ticker": ["tcs.ns"]})
    cleaned = clean_dataframe(df)
    assert cleaned.loc[0, "ticker"] == "TCS"


def test_clean_dataframe_year_invalid():
    df = pd.DataFrame({"year": ["wrong"]})
    cleaned = clean_dataframe(df)
    assert cleaned.loc[0, "year"] is None


def test_clean_dataframe_ticker_empty():
    df = pd.DataFrame({"ticker": [""]})
    cleaned = clean_dataframe(df)
    assert cleaned.loc[0, "ticker"] is None


def test_clean_dataframe_multiple_columns():
    df = pd.DataFrame({
        "Company Name": ["ABC"],
        "Year": ["2024"],
        "Ticker": ["abc.ns"]
    })
    cleaned = clean_dataframe(df)
    assert "company_name" in cleaned.columns
    assert cleaned.loc[0, "year"] == 2024
    assert cleaned.loc[0, "ticker"] == "ABC"


def test_clean_dataframe_keeps_values():
    df = pd.DataFrame({"sales": [1000]})
    cleaned = clean_dataframe(df)
    assert cleaned.loc[0, "sales"] == 1000


def test_clean_dataframe_no_year_no_ticker():
    df = pd.DataFrame({"company": ["ABC"], "sales": [100]})
    cleaned = clean_dataframe(df)
    assert cleaned.loc[0, "company"] == "ABC"
    assert cleaned.loc[0, "sales"] == 100


# ---------------- EXTRA EDGE CASE TESTS ----------------

def test_normalize_year_zero():
    assert normalize_year(0) == 0


def test_normalize_year_negative():
    assert normalize_year("-2024") == -2024


def test_normalize_ticker_special_suffix_lowercase():
    assert normalize_ticker("tcs.ns") == "TCS"


def test_normalize_ticker_bo_lowercase():
    assert normalize_ticker("infy.bo") == "INFY"


def test_normalize_ticker_extra_spaces_suffix():
    assert normalize_ticker(" tcs.ns ") == "TCS"


def test_clean_dataframe_original_not_modified():
    df = pd.DataFrame({"Ticker": ["tcs.ns"]})
    cleaned = clean_dataframe(df)
    assert "Ticker" in df.columns
    assert "ticker" in cleaned.columns