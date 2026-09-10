"""Minimal environment and data-access check for the Week 1 lab."""

from loading import DEFAULT_DATA, REPO_ROOT, load_plant_log


df = load_plant_log()
relative_data_path = DEFAULT_DATA.relative_to(REPO_ROOT)
print(
    f"Setup OK: {len(df)} rows and {len(df.columns)} columns loaded "
    f"from {relative_data_path}."
)
