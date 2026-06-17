import pandas as pd
from src.etl.validator import (
    check_pk_unique,
    check_composite_pk_unique,
    check_fk_integrity,
    check_positive_values,
    check_non_negative_values,
    check_not_null,
    check_year_range,
    check_percentage_range,
    check_required_columns,
    check_no_duplicates,
    check_valid_url,
    check_eps_sign,
    check_balance_difference,
    check_opm_calculation,
    check_minimum_year_coverage,
    check_allowed_values,
)


def test_check_pk_unique_true():
    df = pd.DataFrame({"company_id": [1, 2, 3]})
    assert check_pk_unique(df, "company_id") is True


def test_check_pk_unique_false():
    df = pd.DataFrame({"company_id": [1, 2, 2]})
    assert check_pk_unique(df, "company_id") is False


def test_check_composite_pk_unique_true():
    df = pd.DataFrame({"company_id": [1, 1, 2], "year": [2022, 2023, 2022]})
    assert check_composite_pk_unique(df, ["company_id", "year"]) is True


def test_check_composite_pk_unique_false():
    df = pd.DataFrame({"company_id": [1, 1], "year": [2022, 2022]})
    assert check_composite_pk_unique(df, ["company_id", "year"]) is False


def test_check_fk_integrity_true():
    parent = pd.DataFrame({"company_id": [1, 2, 3]})
    child = pd.DataFrame({"company_id": [1, 2]})
    assert check_fk_integrity(child, parent, "company_id", "company_id") is True


def test_check_fk_integrity_false():
    parent = pd.DataFrame({"company_id": [1, 2]})
    child = pd.DataFrame({"company_id": [1, 3]})
    assert check_fk_integrity(child, parent, "company_id", "company_id") is False


def test_check_positive_values_true():
    df = pd.DataFrame({"sales": [100, 200]})
    assert check_positive_values(df, "sales") is True


def test_check_positive_values_false():
    df = pd.DataFrame({"sales": [100, -50]})
    assert check_positive_values(df, "sales") is False


def test_check_non_negative_values_true():
    df = pd.DataFrame({"debt": [0, 100]})
    assert check_non_negative_values(df, "debt") is True


def test_check_non_negative_values_false():
    df = pd.DataFrame({"debt": [0, -10]})
    assert check_non_negative_values(df, "debt") is False


def test_check_not_null_true():
    df = pd.DataFrame({"ticker": ["TCS", "INFY"]})
    assert check_not_null(df, "ticker") is True


def test_check_not_null_false():
    df = pd.DataFrame({"ticker": ["TCS", None]})
    assert check_not_null(df, "ticker") is False


def test_check_year_range_true():
    df = pd.DataFrame({"year": [2020, 2021, 2022]})
    assert check_year_range(df, "year") is True


def test_check_year_range_false():
    df = pd.DataFrame({"year": [1990, 2022]})
    assert check_year_range(df, "year") is False


def test_check_percentage_range_true():
    df = pd.DataFrame({"return_pct": [10, -5, 20]})
    assert check_percentage_range(df, "return_pct") is True


def test_check_percentage_range_false():
    df = pd.DataFrame({"return_pct": [10, 150]})
    assert check_percentage_range(df, "return_pct") is False


def test_check_required_columns_true():
    df = pd.DataFrame({"company_id": [1], "ticker": ["TCS"]})
    assert check_required_columns(df, ["company_id", "ticker"]) is True


def test_check_required_columns_false():
    df = pd.DataFrame({"company_id": [1]})
    assert check_required_columns(df, ["company_id", "ticker"]) is False


def test_check_no_duplicates_true():
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    assert check_no_duplicates(df) is True


def test_check_no_duplicates_false():
    df = pd.DataFrame({"a": [1, 1], "b": [3, 3]})
    assert check_no_duplicates(df) is False


def test_check_valid_url_true():
    df = pd.DataFrame({"url": ["https://example.com", "http://test.com"]})
    assert check_valid_url(df, "url") is True


def test_check_valid_url_false():
    df = pd.DataFrame({"url": ["example.com"]})
    assert check_valid_url(df, "url") is False


def test_check_eps_sign_true():
    df = pd.DataFrame({"eps": [10.5, -2.3, 0]})
    assert check_eps_sign(df, "eps") is True


def test_check_eps_sign_false():
    df = pd.DataFrame({"eps": [10.5, "abc"]})
    assert check_eps_sign(df, "eps") is False


def test_check_balance_difference_true():
    df = pd.DataFrame({"assets": [100.00], "liabilities_equity": [100.00]})
    assert check_balance_difference(df, "assets", "liabilities_equity") is True


def test_check_balance_difference_false():
    df = pd.DataFrame({"assets": [100.00], "liabilities_equity": [90.00]})
    assert check_balance_difference(df, "assets", "liabilities_equity") is False


def test_check_opm_calculation_true():
    df = pd.DataFrame({"operating_profit": [20], "sales": [100], "opm": [20]})
    assert check_opm_calculation(df, "operating_profit", "sales", "opm") is True


def test_check_opm_calculation_false():
    df = pd.DataFrame({"operating_profit": [20], "sales": [100], "opm": [50]})
    assert check_opm_calculation(df, "operating_profit", "sales", "opm") is False


def test_check_minimum_year_coverage_true():
    df = pd.DataFrame({
        "company_id": [1, 1, 1, 1, 1],
        "year": [2020, 2021, 2022, 2023, 2024]
    })
    assert check_minimum_year_coverage(df, "company_id", "year") is True


def test_check_minimum_year_coverage_false():
    df = pd.DataFrame({
        "company_id": [1, 1, 1],
        "year": [2020, 2021, 2022]
    })
    assert check_minimum_year_coverage(df, "company_id", "year") is False


def test_check_allowed_values_true():
    df = pd.DataFrame({"sector": ["IT", "Banking"]})
    assert check_allowed_values(df, "sector", ["IT", "Banking", "FMCG"]) is True


def test_check_allowed_values_false():
    df = pd.DataFrame({"sector": ["IT", "Unknown"]})
    assert check_allowed_values(df, "sector", ["IT", "Banking", "FMCG"]) is False