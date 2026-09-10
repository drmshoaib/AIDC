"""Data loading for the plant-operations project.

A small, reusable module — the industrial habit is to load data through one
tested function rather than re-reading a CSV in every notebook cell.
"""
from pathlib import Path
import pandas as pd
import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = REPO_ROOT / "config" / "settings.yaml"

EXPECTED_COLUMNS = [
    "timestamp", "line_id", "shift", "units_produced",
    "downtime_min", "energy_kwh", "rejected_units", "motor_temp_c",
]


def load_settings(path=CONFIG_PATH):
    """Load the project settings as a dictionary."""
    config_path = Path(path)
    if not config_path.is_absolute():
        config_path = REPO_ROOT / config_path
    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    settings = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
    if not isinstance(settings, dict):
        raise ValueError(f"Configuration must contain a mapping: {config_path}")
    return settings


def configured_data_path(config_path=CONFIG_PATH):
    """Resolve the raw-data path declared in the project configuration."""
    settings = load_settings(config_path)
    raw_path = settings.get("data", {}).get("raw_path")
    if not raw_path:
        raise KeyError("Missing required setting: data.raw_path")

    data_path = Path(raw_path)
    return data_path if data_path.is_absolute() else REPO_ROOT / data_path


DEFAULT_DATA = configured_data_path()


def load_plant_log(path=None, parse_timestamp=True):
    """Load the plant shift log as a DataFrame.

    Parameters
    ----------
    path : str | Path | None
        CSV location. Defaults to data/raw/plant_shift_log.csv.
    parse_timestamp : bool
        If True, parse the `timestamp` column to datetime.

    Returns
    -------
    pandas.DataFrame
    """
    path = Path(path) if path else DEFAULT_DATA
    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {path}")
    df = pd.read_csv(path)
    if parse_timestamp and "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    return df


def add_rejection_rate(df):
    """Return a copy of df with a `rejection_rate_pct` column (0-100)."""
    out = df.copy()
    out["rejection_rate_pct"] = 100 * out["rejected_units"] / out["units_produced"]
    return out


if __name__ == "__main__":
    data = load_plant_log()
    print(
        f"Loaded {len(data)} rows, {len(data.columns)} columns "
        f"from {DEFAULT_DATA.relative_to(REPO_ROOT)}"
    )
    print(data.head())
