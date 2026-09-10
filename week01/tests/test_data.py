"""Example tests for the project.

These are *meaningful* tests: they check that loading and the derived measure
behave as expected. They are intentionally simple — you will add more as the
project grows (Week 9 covers testing in depth).

Run from the repository root:  pytest -q
"""
import sys
from pathlib import Path

# make src/ importable without installing the package
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from loading import (  # noqa: E402
    DEFAULT_DATA,
    EXPECTED_COLUMNS,
    add_rejection_rate,
    load_plant_log,
    load_settings,
)
from model import flag_lines, load_thresholds  # noqa: E402


def test_load_returns_expected_columns():
    df = load_plant_log()
    for col in EXPECTED_COLUMNS:
        assert col in df.columns, f"missing column: {col}"


def test_load_is_non_empty():
    df = load_plant_log()
    assert len(df) > 0


def test_timestamp_is_parsed():
    import pandas.api.types as ptypes
    df = load_plant_log()
    assert ptypes.is_datetime64_any_dtype(df["timestamp"])


def test_rejection_rate_is_valid():
    df = add_rejection_rate(load_plant_log())
    rr = df["rejection_rate_pct"]
    assert rr.notna().all(), "rejection rate should never be null"
    assert (rr >= 0).all() and (rr <= 100).all(), "rejection rate must be 0-100%"


def test_configured_data_path_exists():
    settings = load_settings()
    assert settings["data"]["raw_path"] == "data/raw/plant_shift_log.csv"
    assert DEFAULT_DATA.exists()


def test_baseline_uses_named_summary_thresholds():
    thresholds = load_thresholds()
    assert "mean_downtime_min_max" in thresholds
    result = flag_lines(load_plant_log(), thresholds)
    assert bool(result.loc["Line_B", "flagged"])
