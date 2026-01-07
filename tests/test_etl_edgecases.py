import pandas as pd
import pytest
from santanderdv2026.etl import run_etl


def test_missing_saldo_raises_keyerror(tmp_path):
    df = pd.DataFrame({"id": [1], "nome": ["Ana"]})
    in_file = tmp_path / "usuarios.csv"
    out_file = tmp_path / "out.csv"
    df.to_csv(in_file, index=False)

    with pytest.raises(KeyError):
        run_etl(in_file, out_file)


def test_non_numeric_saldo_is_coerced_and_defaults(tmp_path):
    df = pd.DataFrame({"id": [1, 2], "nome": ["A", "B"], "saldo": ["N/A", None]})
    in_file = tmp_path / "usuarios.csv"
    out_file = tmp_path / "out.csv"
    df.to_csv(in_file, index=False)

    run_etl(in_file, out_file)
    out = pd.read_csv(out_file)
    # valores não numéricos passam a 0.0 e recebem recomendação 'poupança, cashback'
    assert all(out["recomendacao"] == "poupança, cashback")


def test_header_case_insensitive(tmp_path):
    df = pd.DataFrame({"ID": [1], "Nome": ["Ana"], "Saldo": [2000]})
    in_file = tmp_path / "usuarios.csv"
    out_file = tmp_path / "out.csv"
    df.to_csv(in_file, index=False)

    run_etl(in_file, out_file)
    out = pd.read_csv(out_file)
    assert out.loc[0, "recomendacao"] == "investimentos, cartão Black"
