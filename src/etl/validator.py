import pandas as pd


def check_pk_unique(df, pk_column):
    """DQ-01: Check primary key uniqueness."""
    return bool(df[pk_column].is_unique)


def check_composite_pk_unique(df, columns):
    """DQ-02: Check composite primary key uniqueness."""
    return bool(not df.duplicated(subset=columns).any())


def check_fk_integrity(child_df, parent_df, child_key, parent_key):
    """DQ-03: Check foreign key values exist in parent table."""
    return bool(child_df[child_key].isin(parent_df[parent_key]).all())


def check_positive_values(df, column):
    """DQ-04: Check values are positive."""
    return bool((df[column] > 0).all())


def check_non_negative_values(df, column):
    """DQ-05: Check values are zero or positive."""
    return bool((df[column] >= 0).all())


def check_not_null(df, column):
    """DQ-06: Check column has no null values."""
    return bool(df[column].notnull().all())


def check_year_range(df, column, min_year=2000, max_year=2030):
    """DQ-07: Check year is within valid range."""
    return bool(df[column].between(min_year, max_year).all())


def check_percentage_range(df, column, min_value=-100, max_value=100):
    """DQ-08: Check percentage values are within valid range."""
    return bool(df[column].between(min_value, max_value).all())


def check_required_columns(df, required_columns):
    """DQ-09: Check all required columns exist."""
    return bool(all(col in df.columns for col in required_columns))


def check_no_duplicates(df):
    """DQ-10: Check complete duplicate rows."""
    return bool(not df.duplicated().any())


def check_valid_url(df, column):
    """DQ-11: Check URL starts with http or https."""
    return bool(
        df[column]
        .dropna()
        .astype(str)
        .str.startswith(("http://", "https://"))
        .all()
    )


def check_eps_sign(df, eps_column):
    """DQ-12: Check EPS is numeric."""
    return bool(pd.to_numeric(df[eps_column], errors="coerce").notnull().all())


def check_balance_difference(df, left_col, right_col, tolerance=0.01):
    """DQ-13: Check two financial columns are balanced within tolerance."""
    diff = (df[left_col] - df[right_col]).abs()
    return bool((diff <= tolerance).all())


def check_opm_calculation(
    df,
    operating_profit_col,
    sales_col,
    opm_col,
    tolerance=1
):
    """DQ-14: Check OPM calculation."""
    calculated_opm = (
        df[operating_profit_col] / df[sales_col]
    ) * 100

    diff = (calculated_opm - df[opm_col]).abs()

    return bool((diff <= tolerance).all())


def check_minimum_year_coverage(
    df,
    company_col,
    year_col,
    min_years=5
):
    """DQ-15: Check each company has minimum year coverage."""
    coverage = df.groupby(company_col)[year_col].nunique()

    return bool((coverage >= min_years).all())


def check_allowed_values(
    df,
    column,
    allowed_values
):
    """DQ-16: Check column values are from allowed list."""
    return bool(df[column].isin(allowed_values).all())