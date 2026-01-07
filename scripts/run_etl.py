#!/usr/bin/env python3
"""Entry script to run the ETL from command line.

Usage:
    python scripts/run_etl.py --input data/usuarios.csv --output data/clientes_com_recomendacao.csv
"""
from santanderdv2026.etl import run_etl

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser("Run ETL pipeline")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    run_etl(args.input, args.output)
