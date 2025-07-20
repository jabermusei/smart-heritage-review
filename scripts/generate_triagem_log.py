import pandas as pd
import os

# 1. Caminho de entrada: CSV exportado do Zotero
zotero_path = 'data/raw/SMART HERITAGE.csv'
df = pd.read_csv(zotero_path)

# 2. Funções para extrair decisão e critério das tags manuais
def map_decisao(tags):
    if pd.isna(tags):
        return ''
    t_list = [t.strip().upper() for t in tags.split(';')]
    return 'Incluído' if 'INCLUIR' in t_list else 'Excluído'

def map_criterio(tags):
    if pd.isna(tags):
        return ''
    t_list = [t.strip() for t in tags.split(';')]
    crits = [t for t in t_list if t.upper() != 'INCLUIR']
    return '; '.join(crits)

# 3. Montar DataFrame de triagem
triagem_df = pd.DataFrame({
    'Study_ID':        df['Key'],
    'Título':          df['Title'],
    'Etapa':           '',  # Preencha manualmente se desejar
    'Critério aplicado': df['Manual Tags'].apply(map_criterio),
    'Decisão':         df['Manual Tags'].apply(map_decisao),
    'Justificativa':   '',
    'Timestamp':       df['Date Modified']
})

# 4. Garantir que a pasta exista e salvar
output_dir  = 'data/logs'
output_path = os.path.join(output_dir, 'triagem_log.csv')
os.makedirs(output_dir, exist_ok=True)
triagem_df.to_csv(output_path, index=False)

print(f"Arquivo de triagem gerado em: {output_path}")
