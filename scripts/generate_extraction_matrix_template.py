import pandas as pd
import os

# Definir cabeçalhos da Matatriz Modular (Módulos 1 a 7)
columns = [
    'Autor', 'Ano', 'Título', 'Fonte', 'DOI/URL',
    'Localização', 'Tipo de patrimônio', 'Escopo temporal',
    'Tipo de tecnologia', 'Nível de implementação', 'Provedor/plataforma',
    'Abordagem', 'Métodos específicos', 'Ferramentas de análise',
    'Objetivos', 'Resultados quantitativos', 'Resultados qualitativos',
    'Limitações apontadas pelos autores', 'Sugestões para pesquisas futuras', 'Aplicações práticas não consolidadas',
    'Referências a Feenberg', 'Referências a Agamben', 'Referências a Soja', 'Implicações teóricas', 'Ponto de vista crítico'
]

# Exemplo de preenchimento
example = {
    'Autor': 'Silva, J.',
    'Ano': 2023,
    'Título': 'Estudo de AR em Museu X',
    'Fonte': 'Journal of Digital Heritage',
    'DOI/URL': '10.1234/jdh.2023.001',
    'Localização': 'Cidade Y, País Z',
    'Tipo de patrimônio': 'Museu de Arte',
    'Escopo temporal': '2021–2022',
    'Tipo de tecnologia': 'Realidade Aumentada',
    'Nível de implementação': 'Piloto',
    'Provedor/plataforma': 'ARPlatformX',
    'Abordagem': 'Qualitativa',
    'Métodos específicos': 'Entrevistas semiestruturadas',
    'Ferramentas de análise': 'NVivo',
    'Objetivos': 'Avaliar engajamento do visitante',
    'Resultados quantitativos': '85% de satisfação',
    'Resultados qualitativos': 'Comentários positivos sobre imersão',
    'Limitações apontadas pelos autores': 'Amostra reduzida',
    'Sugestões para pesquisas futuras': 'Estudo longitudinal',
    'Aplicações práticas não consolidadas': 'Integração com QR codes',
    'Referências a Feenberg': 'Mediação técnica',
    'Referências a Agamben': 'Dispositivo de memória',
    'Referências a Soja': 'Thirdspace',
    'Implicações teóricas': 'Reforça híbrido físico-digital',
    'Ponto de vista crítico': 'Acessibilidade pouco explorada'
}

# Criar DataFrame
df = pd.DataFrame([example], columns=columns)

# Criar diretório data/processed se não existir
output_dir = '/mnt/data/data/processed'
os.makedirs(output_dir, exist_ok=True)

# Salvar como Excel
output_path = os.path.join(output_dir, 'extraction_matrix_template.xlsx')
df.to_excel(output_path, index=False)

print(f"Template gerado em: {output_path}")
