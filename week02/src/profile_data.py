"""Bounded data profile for the Week 2 suitability review.

This script describes the supplied teaching data. It does not clean the raw
file, train a model, or claim that the dataset is suitable for deployment.
"""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "plant_shift_log.csv"


def load_data(path=DATA_PATH):
    """Load the raw teaching data and parse its timestamp column."""
    return pd.read_csv(path, parse_dates=["timestamp"])


def build_profile(df):
    """Return a small evidence dictionary for the suitability discussion."""
    return {
        "rows": len(df),
        "columns": len(df.columns),
        "start": df["timestamp"].min(),
        "end": df["timestamp"].max(),
        "hourly_periods": int(df["timestamp"].nunique()),
        "duplicate_rows": int(df.duplicated().sum()),
        "missing_values": df.isna().sum().to_dict(),
        "negative_energy_rows": int((df["energy_kwh"] < 0).sum()),
        "temperature_above_100_rows": int((df["motor_temp_c"] > 100).sum()),
        "lines": sorted(df["line_id"].dropna().unique().tolist()),
    }


def main():
    df = load_data()
    profile = build_profile(df)

    print("Week 2 data-suitability profile")
    print("--------------------------------")
    for key, value in profile.items():
        print(f"{key}: {value}")

    print("\nInterpretation reminder:")
    print("A data profile supplies evidence. It does not approve the project.")


if __name__ == "__main__":
    main()
