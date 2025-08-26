# scripts/count_descolonialidade.py

import os
import sys
import pandas as pd

def find_project_root():
    """
    Procura recursivamente, a partir do diretório corrente, 
    a pasta que contenha data/processed/Planilha_Artigos_Automatizada.xlsx.
    """
    path = os.getcwd()
    while True:
        candidate = os.path.join(path, 'data', 'processed', 'Planilha_Artigos_Automatizada.xlsx')
        if os.path.isfile(candidate):
            return path
        parent = os.path.dirname(path)
        if parent == path:
            return None
        path = parent

# 1. Localiza raiz do projeto
root = find_project_root()
if root is None:
    print("Erro: não consegui encontrar 'data/processed/Planilha_Artigos_Automatizada.xlsx' em nenhum diretório acima.")
    sys.exit(1)

xlsx_path = os.path.join(root, 'data', 'processed', 'Planilha_Artigos_Automatizada.xlsx')

# 2. Carrega a planilha
try:
    df = pd.read_excel(xlsx_path)
except Exception as e:
    print(f"Erro ao abrir o Excel: {e}")
    sys.exit(1)

# 3. Filtra pela etiqueta
mask = df['Etiqueta_Tematica'].str.contains('descolonialidade', case=False, na=False)
count = int(mask.sum())

# 4. Imprime o resultado
print(f"Total de estudos com etiqueta 'descolonialidade': {count}")
if count:
    print("\nTítulos marcados com 'descolonialidade':")
    for i, title in enumerate(df.loc[mask, 'Título'], 1):
        print(f"{i}. {title}")

