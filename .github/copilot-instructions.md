# GitHub Copilot instructions for santanderdv2026

## Objetivo do repositório
- Projeto ETL simples (Santander Dev Week 2023) que processa dados de clientes para gerar recomendações personalizadas.
- Entrada esperada: `usuarios.csv` (ID, Nome, Saldo, ...). Saída: `clientes_com_recomendacao.csv`.
- Regra de negócio conhecida: clientes com `saldo > 1000.00` recebem recomendação de investimentos e cartão Black; caso contrário, dicas de poupança/cashback (ver `README.md`).

## O que um agente deve entender primeiro ✅
1. Leia `README.md` para compreender o propósito e os nomes de arquivos de entrada/saída.
2. Este repositório atualmente não contém scripts ou testes - qualquer artefato novo deve ser colocado de forma organizada (ex.: `src/`, `scripts/`, `data/`, `tests/`).
3. Tecnologias: **Python 3.11+** e **Pandas** (conforme badges do `README.md`).

## Tarefas típicas que o agente pode executar 🔧
- Implementar um script executável (ex.: `scripts/run_etl.py`) que:
  - lê `usuarios.csv` com `pandas.read_csv()`;
  - aplica a regra `saldo > 1000.0` e cria a coluna `recomendacao` com valores textuais (`"investimentos, cartão Black"` ou `"poupança, cashback"`);
  - escreve `clientes_com_recomendacao.csv` com `df.to_csv()`.
- Criar uma versão em notebook (`notebooks/etl.ipynb`) compatível com Google Colab.
- Adicionar um `requirements.txt` ou `pyproject.toml` com `pandas` e outras dependências.
- Adicionar testes simples com `pytest` (ex.: `tests/test_etl.py`) que validem a saída para pequenos datasets.

## Convenções e padrões observáveis (e recomendados) 📌
- Nomes de arquivos de dados mencionados no doc são canônicos: **`usuarios.csv`** e **`clientes_com_recomendacao.csv`**.
- Use **Pandas** para leitura/transformação/escrita de CSVs (foco em clareza e legibilidade de transformações).
- Se adicionar código Python, prefira colocar implementação em `src/` e adicionar um entrypoint em `scripts/`.
- Para notebooks, coloque em `notebooks/` e deixe uma célula de instalação de dependências clara (ex.: `!pip install -r requirements.txt`).

## Fluxos de desenvolvimento & comandos úteis ⚙️
- Ambiente virtual local (sugerido):
  - `python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`
- Executar o ETL (exemplo, se existir `scripts/run_etl.py`):
  - `python scripts/run_etl.py --input data/usuarios.csv --output data/clientes_com_recomendacao.csv`
- Testes (se adicionados):
  - `pip install pytest && pytest -q`

> Nota: esses comandos não estão atualmente no repositório, mas refletem o fluxo esperado quando scripts e dependências forem adicionados.

## Boas práticas para commits / PRs do agente 📝
- Mantenha PRs pequenos e focados (ex.: "Adiciona script ETL básico e teste unitário").
- Inclua um teste simples quando adicionar lógica de negócio.
- Atualize `README.md` com instruções de execução se novos scripts/notebooks forem adicionados.

## Pontos que requerem atenção/validação humana ⚠️
- O repositório atual é mínimo — verifique com o mantenedor onde os dados serão armazenados (ex.: `data/` no repo vs. armazenamento externo).
- Confirme expectativas de formatação e colunas de `usuarios.csv` (tipos, nomes, separador) antes de assumir um schema.

---

**Observação:** já adicionei exemplos mínimos de `src/etl.py`, `scripts/run_etl.py`, `tests/test_etl.py` e `requirements.txt` para ajudar na integração rápida. Comandos úteis no workspace:

- Criar ambiente e instalar dependências:
  ```bash
  python -m venv .venv && source .venv/bin/activate
  pip install -r requirements.txt
  ```
- Executar ETL:
  ```bash
  python scripts/run_etl.py --input data/usuarios.csv --output data/clientes_com_recomendacao.csv
  ```
- Rodar testes:
  ```bash
  pytest -q
  ```

- Verificar lint (localmente):
  ```bash
  pip install ruff
  ruff check .
  ```

Também adicionei um notebook de exemplo em `notebooks/etl.ipynb` (compatível com Colab). Já incluí um workflow de GitHub Actions (`.github/workflows/pytest.yml`) que executa os testes (`pytest`) e um job de lint (`ruff check .`) em pushes e pull requests para `main`. Posso expandir os testes para cobrir mais casos de borda ou estender o CI para linting/formatting se desejar.