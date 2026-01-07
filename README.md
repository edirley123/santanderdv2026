# santanderdv2026
Projeto da DIO
b# Santander Dev Week 2023 - ETL com Python 📊

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Library-Pandas-orange.svg)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📌 Descrição do Projeto
Este projeto foi desenvolvido como parte do desafio técnico do **Bootcamp Santander / DIO**. O objetivo é construir um pipeline de **ETL (Extract, Transform, Load)** utilizando a linguagem Python para manipular dados de clientes bancários e gerar recomendações personalizadas.

## ⚙️ O Pipeline ETL

### 1. Extract (Extração)
Os dados são extraídos de um ficheiro CSV (`usuarios.csv`) que contém informações básicas dos clientes, como ID, Nome e Saldo atual.

### 2. Transform (Transformação)
Utilizando a biblioteca **Pandas**, foi aplicada uma regra de negócio para segmentar os clientes:
- Clientes com saldo acima de **1.000,00** recebem uma recomendação para investimentos e cartões Black.
- Clientes com saldo abaixo deste valor recebem dicas de poupança e cashback.

### 3. Load (Carregamento)
Os dados processados e as novas recomendações são exportados para um novo ficheiro (`clientes_com_recomendacao.csv`), prontos para serem utilizados pela equipa de Marketing.

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**
- **Pandas**: Para manipulação e análise de dados.
- **Google Colab / VS Code**: Ambiente de desenvolvimento.

## 🚀 Como executar o projeto
1. Clone este repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
   cd NOME_DO_REPOSITORIO
   ```

2. Criar e ativar ambiente virtual e instalar dependências:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux / macOS
   pip install -r requirements.txt
   ```

3. Executar o ETL (exemplo):
   ```bash
   python scripts/run_etl.py --input data/usuarios.csv --output data/clientes_com_recomendacao.csv
   ```

4. Rodar testes:
   ```bash
   pip install pytest
   pytest -q
   ```

5. Notebook: abra `notebooks/etl.ipynb` no Jupyter/Colab; a primeira célula instala as dependências.

6. (Opcional) Instalar e configurar `pre-commit` para hooks locais:
```bash
pip install pre-commit ruff black
pre-commit install
# rodar checks em todos os arquivos
pre-commit run --all-files
```

Dica: os hooks configurados incluem `black` (formatação), `ruff` (lint) e verificação de espaços finais/fim de arquivo.