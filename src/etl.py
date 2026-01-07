"""ETL implementation for santanderdv2026.

Provides a single entrypoint `run_etl(input_path, output_path)` that:
- lê um CSV de entrada com `pandas.read_csv`
- normaliza nomes de colunas para lowercase
- cria coluna `recomendacao` com base na regra: saldo > 1000 -> investimentos, cartão Black; senão poupança, cashback
- escreve CSV de saída com `df.to_csv(index=False)`
"""
from __future__ import annotations

from pathlib import Path
import logging
from typing import Union

import pandas as pd

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def run_etl(input_path: Union[str, Path], output_path: Union[str, Path]) -> None:
    input_path = Path(input_path)
    output_path = Path(output_path)

    logger.info("Lendo dados de %s", input_path)
    df = pd.read_csv(input_path)

    # Normalizar nomes de colunas para facilitar detecção (ex.: 'Saldo' ou 'saldo')
    df.columns = df.columns.str.strip().str.lower()

    if "saldo" not in df.columns:
        raise KeyError("esperado arquivo com coluna 'saldo' (case-insensitive)")

    # Garantir que saldo seja numérico
    df["saldo"] = pd.to_numeric(df["saldo"], errors="coerce").fillna(0.0)

    # Aplicar regra de negócio
    def _recomendacao(saldo: float) -> str:
        if saldo > 1000.0:
            return "investimentos, cartão Black"
        return "poupança, cashback"

    df["recomendacao"] = df["saldo"].apply(_recomendacao)

    # Escrever CSV de saída
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    logger.info("Arquivo de saída escrito em %s", output_path)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Executa ETL simples de usuários -> recomendações")
    parser.add_argument("--input", required=True, help="Caminho para usuarios.csv de entrada")
    parser.add_argument("--output", required=True, help="Caminho para arquivo CSV de saída")
    args = parser.parse_args()

    run_etl(args.input, args.output)
