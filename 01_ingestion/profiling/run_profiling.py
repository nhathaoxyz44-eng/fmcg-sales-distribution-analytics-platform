"""
VietDist Source Profiling Runner

Purpose:
Reusable profiling entry point for raw FMCG source datasets.

Future usage:
python run_profiling.py --source SRC01_sales_transactions.csv
"""

from pathlib import Path
import argparse
from data_profiler import profile_dataset


def main():
    parser = argparse.ArgumentParser(
        description="Run dataset profiling for VietDist source files"
    )

    parser.add_argument(
        "--source",
        required=True,
        help="Path to source dataset"
    )

    args = parser.parse_args()

    result = profile_dataset(Path(args.source))

    print("Dataset profiling completed")
    print(result)


if __name__ == "__main__":
    main()
