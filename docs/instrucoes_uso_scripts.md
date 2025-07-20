# Instruções de Uso dos Scripts

Antes de executar os scripts, instale as dependências:

```bash
pip install pandas pillow

## Scripts disponíveis

- `scripts/generate_prisma_diagram.py`: gera o diagrama PRISMA em `protocol/prisma_diagrama.png`.
- `scripts/extract_data.py`: extrai e codifica dados, salvando em `data/processed/Planilha_Artigos_Automatizada.xlsx`.
- `scripts/analysis_quantitative.py`: produz CSVs de frequência e cruzamentos em `data/processed/quantitative/`.
- `scripts/analysis_qualitative.py`: gera amostras por temática em `data/processed/qualitative/` e log em `data/logs/codificacao_log.csv`.

## Estrutura de Pastas

- `data/raw/`: dados originais (RIS, CSV).
- `data/processed/`: dados processados e resultados.
- `data/logs/`: logs de triagem e codificação.
- `protocol/`: documentação do protocolo PRISMA.

Para executar um script:python scripts/<nome_do_script>.py