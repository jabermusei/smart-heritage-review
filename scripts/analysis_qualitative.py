import pandas as pd, os

# Cria pastas de saída, se não existirem
os.makedirs('data/processed/qualitative', exist_ok=True)
os.makedirs('data/logs', exist_ok=True)

# Carrega dados processados
df = pd.read_excel('data/processed/Planilha_Artigos_Automatizada.xlsx')

# Lista de temáticas para amostragem
themes = [
    'memória', 'tecnologia', 'governança', 'sustentabilidade',
    'educação', 'engajamento', 'descolonialidade', 'justiça territorial',
    'inovação', 'acessibilidade'
]

# Log de codificação
cod_log = []

# Extrai amostra diversificada por tema
for theme in themes:
    subset = df[df['Etiqueta_Tematica'].str.contains(theme, case=False, na=False)]
    sample = subset.drop_duplicates('Tecnologia').head(10)[[
        'Título', 'Resultado_central', 'Tecnologia', 'País/Cidade', 'Ano'
    ]]
    sample.to_csv(f'data/processed/qualitative/sample_{theme}.csv', index=False)
    for idx, row in sample.iterrows():
        cod_log.append({
            'Temática': theme,
            'Study_ID': idx,
            'Título': row['Título'],
            'Timestamp': ''
        })

# Salva o log de codificação
pd.DataFrame(cod_log).to_csv('data/logs/codificacao_log.csv', index=False)
