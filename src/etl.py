# Compat layer: re-export from the real package `santanderdv2026`
# This keeps `from src.etl import run_etl` working for users that import the old path.
from santanderdv2026.etl import run_etl

__all__ = ["run_etl"]
