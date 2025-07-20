import pandas as pd

# Carrega a planilha bruta
df = pd.read_excel('data/raw/Planilha_Artigos_Preenchida.xlsx')

# Define palavras-chave para temáticas
tema_keywords = {
    'governança': ['governança', 'governance', 'gestão', 'política'],
    'sustentabilidade': ['sustentabilidade', 'sustainable', 'verde', 'eco'],
    'engajamento': ['engajamento', 'engagement', 'participação', 'interatividade', 'imersão', 'retenção', 'feedback'],
    'descolonialidade': ['descolonialidade', 'decolonial', 'colonial', 'pós-colonial', 'indígena', 'epistemologias do sul', 'pluriversal'],
    'justiça territorial': ['justiça territorial', 'territorial justice', 'equidade', 'acesso', 'inclusão territorial', 'desigualdade espacial'],
    'inovação': ['inovação', 'innovation', 'inovar', 'novidade', 'prototipação', 'experimentação', 'piloto', 'startup'],
    'acessibilidade': ['acessibilidade', 'accessibility', 'inclusão', 'usuários com deficiência', 'wcag', 'legibilidade', 'interface adaptativa'],
    'memória': ['memória', 'memory', 'histórico', 'heritage'],
    'educação': ['educação', 'education', 'formação', 'aprendizagem', 'capacitação', 'didático', 'mediador'],
    'tecnologia': ['tecnologia', 'digital', 'digitais']
}

# Função de mapeamento de temáticas
def map_temas(text):
    tags = []
    if isinstance(text, str):
        text = text.lower()
        for tema, kws in tema_keywords.items():
            if any(kw in text for kw in kws):
                tags.append(tema)
    return '; '.join(sorted(set(tags)))

# Coluna combinada para análise textual
df['combined'] = df[['Título', 'Tecnologia', 'Objetivo', 'Resultado_central']].fillna('').agg(' '.join, axis=1)

# Etiquetas Temáticas
df['Etiqueta_Tematica'] = df['combined'].apply(map_temas)

# Identificação de impactos
df['Impacto_Institucional'] = df['combined'].str.contains('gestão|institucional|política', case=False, na=False)
df['Impacto_Visitante'] = df['combined'].str.contains('visitante|usuário|experiência|feedback', case=False, na=False)
df['Impacto_Cultural'] = df['combined'].str.contains('memória|cultural|narrativa|heritage', case=False, na=False)

# Exporta a planilha processada
df.to_excel('data/processed/Planilha_Artigos_Automatizada.xlsx', index=False)