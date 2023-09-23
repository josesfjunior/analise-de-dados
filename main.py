import pandas as pd
import matplotlib.pyplot as plt

# Carregue seus dados em um DataFrame
# Suponha que 'data.csv' seja o arquivo de dados
df = pd.read_csv('base.csv')

# Resumo estatístico inicial
summary = df.describe()

# 1. Como está distribuído o número de acessos de acordo com os atributos apresentados?
plt.figure(figsize=(10, 6))
plt.bar(df['nome_empresa'], df['acessos'])
plt.xlabel('Empresa')
plt.ylabel('Número de Acessos')
plt.title('Número de Acessos por Empresa')
plt.xticks(rotation=45)

# 2. Como essas características mudaram ao longo dos anos?
plt.figure(figsize=(12, 6))
for empresa in df['nome_empresa'].unique():
    empresa_data = df[df['nome_empresa'] == empresa]
    plt.plot(empresa_data['ano'], empresa_data['acessos'], label=empresa)

plt.xlabel('Ano')
plt.ylabel('Número de Acessos')
plt.title('Mudança no Número de Acessos ao Longo dos Anos por Empresa')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True)
plt.tight_layout()

# 3. Quais empresas com maior número de contratos considerando o porte da empresa?
contratos_por_porte = df.groupby('porte_empresa')['acessos'].sum().reset_index()
contratos_por_porte = contratos_por_porte.sort_values(by='acessos', ascending=False)
plt.figure(figsize=(10, 6))
plt.barh(contratos_por_porte['porte_empresa'], contratos_por_porte['acessos'], color='skyblue')
plt.xlabel('Número de Contratos')
plt.ylabel('Porte da Empresa')
plt.title('Número de Contratos por Porte da Empresa')

# 4. Como o perfil do tipo de empresa mudou ao longo dos anos? Houve crescimento ou redução em relação a um tipo de porte específico?
contratos_por_ano_porte = df.groupby(['ano', 'porte_empresa'])['acessos'].sum().reset_index()
plt.figure(figsize=(12, 6))
for porte in contratos_por_ano_porte['porte_empresa']:
    data = contratos_por_ano_porte[contratos_por_ano_porte['porte_empresa'] == porte]
    plt.plot(data['ano'], data['acessos'], label=porte)

plt.xlabel('Ano')
plt.ylabel('Número de Contratos')
plt.title('Evolução do Número de Contratos por Porte de Empresa ao Longo dos Anos')
plt.legend()
plt.grid(True)

# 5. Atualmente, usando os dados mais recentes da base, qual o perfil da distribuição de banda larga dentro do escopo escolhido?
ano_mais_recente = df['ano'].max()
dados_recentes = df[df['ano'] == ano_mais_recente]
estatisticas_descritivas = dados_recentes['acessos'].describe()

plt.figure(figsize=(10, 6))
plt.hist(dados_recentes['acessos'], bins=20, edgecolor='k')
plt.xlabel('Número de Acessos de Banda Larga')
plt.ylabel('Frequência')
plt.title('Distribuição de Acessos de Banda Larga (Ano mais recente)')
plt.grid(True)

plt.show()
