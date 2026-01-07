import pandas as pd
from src.etl import run_etl


def test_run_etl_creates_recommendation(tmp_path):
    # dataset de exemplo
    df = pd.DataFrame({"id": [1, 2], "nome": ["Ana", "Bruno"], "saldo": [1500, 500]})

    in_file = tmp_path / "usuarios.csv"
    out_file = tmp_path / "clientes_com_recomendacao.csv"

    df.to_csv(in_file, index=False)

    # executar ETL
    run_etl(in_file, out_file)

    # validar saída
    out = pd.read_csv(out_file)
    assert "recomendacao" in out.columns
    rec1 = out.loc[out["id"] == 1, "recomendacao"].iloc[0]
    rec2 = out.loc[out["id"] == 2, "recomendacao"].iloc[0]
    assert rec1 == "investimentos, cartão Black"
    assert rec2 == "poupança, cashback"
