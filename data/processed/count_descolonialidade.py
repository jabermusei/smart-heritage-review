import pandas as pd

# 1. Carregue a planilha processada
df = pd.read_excel('data/processed/Planilha_Artigos_Automatizada.xlsx')

# 2. Crie uma máscara para filtrar linhas com 'descolonialidade'
mask = df['Etiqueta_Tematica'].str.contains('descolonialidade', case=False, na=False)

# 3. Conte quantos registros satisfazem essa condição
count = mask.sum()

print(f"Total de estudos com etiqueta 'descolonialidade': {count}")
