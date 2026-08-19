"""
VietDist Source Data Profiler

Reusable profiling utilities for Phase 2 Data Discovery.
"""

import pandas as pd


def load_dataset(file_path: str) -> pd.DataFrame:
    """Load CSV or Excel dataset."""
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    return pd.read_excel(file_path)


def profile_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Generate column-level profiling metrics."""
    profile = pd.DataFrame({
        'column_name': df.columns,
        'data_type': df.dtypes.astype(str).values,
        'null_count': df.isna().sum().values,
        'unique_count': df.nunique().values,
    })

    profile['null_percentage'] = (
        profile['null_count'] / len(df) * 100
    ).round(2)

    return profile


if __name__ == '__main__':
    print('VietDist profiling framework initialized')
