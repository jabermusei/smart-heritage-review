import os
import pandas as pd

# Define diretório base do repositório (atual)
base_dir = os.getcwd()
# Cria o diretório de apêndices se não existir
appendices_dir = os.path.join(base_dir, 'appendices')
os.makedirs(appendices_dir, exist_ok=True)

# 1. Gerar Apêndice A em Markdown
apendice_a_md = os.path.join(appendices_dir, 'apendice_a_protocolo.md')
with open(apendice_a_md, 'w', encoding='utf-8') as f:
    f.write('# Apêndice A: Protocolo PRISMA-ScR & PRISMA-P\n\n')
    f.write('## 1. Objetivo\n')
    f.write('Mapear estudos que mencionam “smart heritage” articulando museus em contextos de cidades inteligentes e Destinos Turísticos Inteligentes.\n\n')
    f.write('## 2. Bases de Dados e Estratégias de Busca\n')
    f.write('- Scopus, Web of Science, Scite\n')
    f.write('- Strings de busca principais:\n')
    f.write('  ("smart heritage" OR "smart cultural heritage") AND ("smart city" OR "cidades inteligentes" OR "smart destination" OR "Destino Turístico Inteligente")\n')
    f.write('- Período: 2020–2025\n')
    f.write('- Idiomas: Inglês, Espanhol, Português\n\n')
    f.write('## 3. Critérios de Elegibilidade (PICO/PECO)\n')
    f.write('- **População (P)**: Museus ou acervos museológicos\n')
    f.write('- **Intervenção/Exposição (I/E)**: Tecnologias digitais (IoT, AR/VR, BIM, Digital Twin, Big Data, IA)\n')
    f.write('- **Contexto (C)**: Projetos de cidades inteligentes ou Destinos Turísticos Inteligentes\n')
    f.write('- **Outcomes (O)**: Aplicações práticas e impactos institucionais, no visitante e culturais\n')
    f.write('- **Exclusões**: Duplicatas; texto não acessível; publicações fora de 2020–2025; estudos irrelevantes\n\n')
    f.write('## 4. Processo PRISMA\n')
    f.write('1. Identificação: 1 137 registros\n')
    f.write('2. Triagem: 780 avaliados em título–resumo (357 duplicatas removidas)\n')
    f.write('3. Elegibilidade: 271 texto completo (104 excluídos)\n')
    f.write('4. Inclusão: 167 estudos incluídos na síntese\n\n')
    f.write('## 5. Fluxograma PRISMA\n')
    f.write('Insira aqui o diagrama PRISMA (arquivo protocol/prisma_diagrama.png).\n')
print(f"Apêndice A gerado em: {apendice_a_md}")

# 2. Gerar Apêndice B: Matriz de Extração
columns = [
    'Autor', 'Ano', 'Título', 'Fonte', 'DOI/URL',
    'Localização', 'Tipo de patrimônio', 'Escopo temporal',
    'Tipo de tecnologia', 'Nível de implementação', 'Provedor/plataforma',
    'Abordagem', 'Métodos específicos', 'Ferramentas de análise',
    'Objetivos', 'Resultados quantitativos', 'Resultados qualitativos',
    'Limitações apontadas pelos autores', 'Sugestões para pesquisas futuras', 'Aplicações práticas não consolidadas',
    'Referências a Feenberg', 'Referências a Agamben', 'Referências a Soja', 'Implicações teóricas', 'Ponto de vista crítico'
]
example = {
    'Autor': 'Silva, J.', 'Ano': 2023, 'Título': 'Estudo de AR em Museu X',
    'Fonte': 'Journal of Digital Heritage', 'DOI/URL': '10.1234/jdh.2023.001',
    'Localização': 'Cidade Y, País Z', 'Tipo de patrimônio': 'Museu de Arte',
    'Escopo temporal': '2021–2022', 'Tipo de tecnologia': 'Realidade Aumentada',
    'Nível de implementação': 'Piloto', 'Provedor/plataforma': 'ARPlatformX',
    'Abordagem': 'Qualitativa', 'Métodos específicos': 'Entrevistas semiestruturadas',
    'Ferramentas de análise': 'NVivo', 'Objetivos': 'Avaliar engajamento do visitante',
    'Resultados quantitativos': '85% de satisfação', 'Resultados qualitativos': 'Comentários positivos sobre imersão',
    'Limitações apontadas pelos autores': 'Amostra reduzida', 'Sugestões para pesquisas futuras': 'Estudo longitudinal',
    'Aplicações práticas não consolidadas': 'Integração com QR codes',
    'Referências a Feenberg': 'Mediação técnica integrada',
    'Referências a Agamben': 'Dispositivo de memória digital',
    'Referências a Soja': 'Espaço híbrido descrito',
    'Implicações teóricas': 'Novas fronteiras conceituais', 'Ponto de vista crítico': 'Acessibilidade limitada'
}
df_template = pd.DataFrame([example], columns=columns)
append_b_xlsx = os.path.join(appendices_dir, 'apendice_b_planilha_extract.xlsx')
append_b_csv  = os.path.join(appendices_dir, 'apendice_b_planilha_extract.csv')
# Tentar salvar como Excel usando xlsxwriter
try:
    df_template.to_excel(append_b_xlsx, index=False, engine='xlsxwriter')
    print(f"Apêndice B gerado em: {append_b_xlsx}")
except Exception:
    df_template.to_csv(append_b_csv, index=False)
    print(f"Fallback CSV gerado em: {append_b_csv}")
