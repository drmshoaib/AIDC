"""Interpretable baseline for the plant-operations scenario.

Week 1 uses a *naive, transparent* rule, not a trained model. The point is to
have a defensible baseline you can explain — later weeks improve it with
validation, residual analysis, and proper evaluation.

Decision supported: which production line should be looked at first at the
next shift handover?
"""
try:  # support both `python src/model.py` and `python -m src.model`
    from .loading import CONFIG_PATH, add_rejection_rate, load_plant_log, load_settings
except ImportError:  # pragma: no cover - exercised by the script command
    from loading import CONFIG_PATH, add_rejection_rate, load_plant_log, load_settings

DEFAULT_THRESHOLDS = {
    "motor_temp_c_max": 95.0,
    "mean_downtime_min_max": 20.0,
}


def load_thresholds(path=CONFIG_PATH):
    """Read alert thresholds, using illustrative defaults for absent keys."""
    settings = load_settings(path)
    configured_thresholds = settings.get("thresholds", {})
    return {**DEFAULT_THRESHOLDS, **configured_thresholds}


def line_summary(df):
    """Line-level summary used to explain the flags."""
    d = add_rejection_rate(df)
    return (
        d.groupby("line_id")
        .agg(
            mean_downtime_min=("downtime_min", "mean"),
            mean_rejection_rate_pct=("rejection_rate_pct", "mean"),
            max_motor_temp_c=("motor_temp_c", "max"),
        )
        .round(2)
    )


def flag_lines(df, thresholds=None):
    """Flag lines using maximum temperature and mean downtime.

    Returns a summary DataFrame with a boolean `flagged` column. This is a
    baseline heuristic, not a validated decision rule.
    """
    thr = thresholds or load_thresholds()
    summ = line_summary(df)
    summ["flagged"] = (
        (summ["max_motor_temp_c"] > thr["motor_temp_c_max"])
        | (summ["mean_downtime_min"] > thr["mean_downtime_min_max"])
    )
    return summ


if __name__ == "__main__":
    df = load_plant_log()
    result = flag_lines(df)
    print("Baseline line review (Week 1 heuristic):\n")
    print(result)
    flagged = result.index[result["flagged"]].tolist()
    print(f"\nLines to inspect first: {flagged or 'none under current thresholds'}")
