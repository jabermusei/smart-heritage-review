import pandas as pd, os

# Cria pasta de saída, se não existir
os.makedirs('data/processed/quantitative', exist_ok=True)

# Carrega dados processados
df = pd.read_excel('data/processed/Planilha_Artigos_Automatizada.xlsx')

# 1. Frequência por tecnologia
freq_tech = df['Tecnologia'].value_counts().rename_axis('Tecnologia').reset_index(name='Frequencia')
freq_tech.to_csv('data/processed/quantitative/freq_technology.csv', index=False)

# 2. Frequência por localização
freq_loc = df['País/Cidade'].value_counts().rename_axis('Localizacao').reset_index(name='Frequencia')
freq_loc.to_csv('data/processed/quantitative/freq_location.csv', index=False)

# 3. Frequência por ano
freq_year = df['Ano'].value_counts().sort_index().rename_axis('Ano').reset_index(name='Frequencia')
freq_year.to_csv('data/processed/quantitative/freq_year.csv', index=False)

# 4. Frequência de temáticas
df_t = df.assign(Tematica=df['Etiqueta_Tematica'].str.split('; ')).explode('Tematica')
freq_theme = df_t['Tematica'].value_counts().rename_axis('Tematica').reset_index(name='Frequencia')
freq_theme.to_csv('data/processed/quantitative/freq_theme.csv', index=False)

# 5. Frequência de impactos
impact_cols = ['Impacto_Institucional', 'Impacto_Visitante', 'Impacto_Cultural']
impact_counts = df[impact_cols].sum().rename_axis('Tipo_Impacto').reset_index(name='Frequencia')
impact_counts.to_csv('data/processed/quantitative/freq_impacts.csv', index=False)

# 6. Cruzamento tecnologia x impacto
cross_tech = df.groupby('Tecnologia')[impact_cols].sum().reset_index()
cross_tech.to_csv('data/processed/quantitative/tech_impact_cross.csv', index=False)

# 7. Cruzamento temática x impacto
cross_theme = df_t.groupby('Tematica')[impact_cols].sum().reset_index()
cross_theme.to_csv('data/processed/quantitative/theme_impact_cross.csv', index=False)
