# Abertura e Carregamento de Dados (ETL - Extract, Transform, Load)

```python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

```

1. Extração de Dados:

Inicie o projeto extraindo dados de um arquivo CSV.

```python

df = pd.read_csv('INMET_MS_ITAQUIRAI_2020.CSV', delimiter=';', skiprows=8, encoding='latin1')

```

2. Inspeção Inicial:

Revise o conteúdo dos dados extraídos, observando as primeiras e últimas linhas, a forma e a descrição geral dos dados, e os tipos de dados.

```python

df.dtypes

df.shape
```

```python

# primeiras linhas

df.head()

```

```python

# ultimas linhas

df.tail()


```


```python

df = df[['Data','Hora UTC','PRECIPITAÇÃO TOTAL, HORÁRIO (mm)', 'TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)','TEMPERATURA DO PONTO DE ORVALHO (°C)','UMIDADE RELATIVA DO AR, HORARIA (%)', 'RADIACAO GLOBAL (Kj/m²)', 'VENTO, DIREÇÃO HORARIA (gr) (° (gr))' ,'VENTO, VELOCIDADE HORARIA (m/s)']]

```



3. Identificação e Tratamento de Valores Faltantes:

Identifique a presença de valores nulos e trate-os adequadamente, seja removendo, preenchendo ou substituindo esses valores.

```python

df.isnull()

```

```python
# Remove linhas com qualquer valor nulo

df_sem_nulos = df.dropna()

# Remove colunas que contenham valores nulos

df_sem_nulos_colunas = df.dropna(axis=1)

```


# Tratamento de Dados
1. Ajustes e Limpeza:

Organize e limpe os dados, removendo duplicatas e normalizando quando necessário.

```python

df_sem_duplicatas = df.drop_duplicates()

```

```python

df.head()

```

```python
df_analise = df[['Data', 'PRECIPITAÇÃO TOTAL, HORÁRIO (mm)']]
```



2.Renomeação e Ajuste de Colunas:

Renomeie colunas e ajuste os tipos de dados conforme necessário para garantir a consistência e clareza.

```python
# Renomeando colunas para facilitar o entendimento
df.rename(columns={
    'Data': 'data',
    'Hora UTC': 'hora_utc',
    'PRECIPITAÇÃO TOTAL, HORÁRIO (mm)': 'precipitacao_mm',
    'TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)': 'temp_bulbo_seco_c',
    'TEMPERATURA DO PONTO DE ORVALHO (°C)': 'temp_orvalho_c',
    'UMIDADE RELATIVA DO AR, HORARIA (%)': 'umidade_relativa',
    'RADIACAO GLOBAL (Kj/m²)': 'radiacao_global_kjm2',
    'VENTO, DIREÇÃO HORARIA (gr) (° (gr))': 'vento_direcao_gr',
    'VENTO, VELOCIDADE HORARIA (m/s)': 'vento_velocidade_ms'
}, inplace=True)

```

```python
# Ajustando o tipo de dados para as colunas
df['data'] = pd.to_datetime(df['data'], format='%Y-%m-%d')
df['precipitacao_mm'] = df['precipitacao_mm'].astype(float)
df['temp_bulbo_seco_c'] = df['temp_bulbo_seco_c'].astype(float)
df['temp_orvalho_c'] = df['temp_orvalho_c'].astype(float)
df['umidade_relativa'] = df['umidade_relativa'].astype(float)
df['radiacao_global_kjm2'] = df['radiacao_global_kjm2'].astype(float)
df['vento_direcao_gr'] = df['vento_direcao_gr'].astype(float)
df['vento_velocidade_ms'] = df['vento_velocidade_ms'].astype(float)

# Verificando as mudanças
df.dtypes

```

3.Transformações e Criação de Novas Colunas:

Realize transformações relevantes nos dados, como criar novas colunas derivadas de outras existentes.

```python

# Criando novas colunas derivadas de outras existentes, por exemplo, conversão de radiação global de Kj/m² para MJ/m²
df['radiacao_global_mjm2'] = df['radiacao_global_kjm2'] / 1000

# Criando uma coluna de mês para análise sazonal
df['mes'] = df['data'].dt.month

```

# Análise de Dados
1. Geração de Insights Estatísticos:

Utilize técnicas estatísticas para entender os dados, como calcular somas, médias e identificar valores máximos e mínimos.

```python

df.describe()

```



2.Agrupamento e Sumarização:

Agrupe os dados para identificar padrões e tendências, gerando sumarizações que permitam uma análise mais profunda.

```python

#agrupado = df_vendas.groupby('Produto').mean()
#print(agrupado)

```


# Visualização de Dados com Matplotlib

1. Criação de Gráficos Básicos:
Visualize os dados através de gráficos, como histogramas e gráficos de barras, para facilitar a compreensão das análises realizadas.

```python

# Criando um gráfico de barras para visualizar a precipitação total por mês
df.groupby('mes')['precipitacao_total_mm'].sum().plot(kind='bar', color='blue')
plt.title('Precipitação Total por Mês')
plt.xlabel('Mês')
plt.ylabel('Precipitação Total (mm)')
plt.show()

```


2. Customização de Gráficos:

Personalize os gráficos, adicionando títulos, legendas e ajustando as cores para torná-los mais informativos.

```python
# Personalizando um gráfico de linha para a temperatura do ar ao longo do tempo
plt.plot(df['data'], df['temp_ar_bulbo_seco_c'], color='orange', label='Temperatura do Ar (°C)')
plt.title('Variação da Temperatura ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

```

# Persistência dos Resultados no SQLite

1.Criação do Banco de Dados:

Estabeleça um banco de dados SQLite para armazenar os resultados das análises.

```python

import sqlite3

conn = sqlite3.connect('clima.db')

cursor = conn.cursor()

```


```python
# persistindo o DataFrame no banco de dados

df.to_sql('clima', conn, if_exists='replace')

```


2. Salvamento dos Dados Tratados:

Salve os dados tratados e os resultados das análises em tabelas dentro do banco de dados.

```python
cursor = conn.cursor()
cursor.execute('SELECT * FROM clima')

col_names = [description[0] for description in cursor.description]

```


```python
df_db = pd.DataFrame(cursor.fetchall(), columns=col_names)

df_db

```


# Finalização do Projeto

Perguntas para Reflexão: Ao final do projeto, as alunas devem refletir sobre as seguintes questões baseadas nos dados analisados:

Qual foi a média de valores de uma coluna específica?

```Python
# Média da coluna de precipitação total
media_precipitacao = df['precipitacao_total_mm'].mean()
print(f"Média de Precipitação: {media_precipitacao:.2f} mm")
```

Qual o total de registros após a limpeza dos dados?

```Python
# Número de registros após a limpeza de nulos e duplicados
total_registros_limpos = df_sem_duplicatas.shape[0]
print(f"Total de registros após a limpeza: {total_registros_limpos}")
```

Quais foram os valores máximos e mínimos identificados?

```python
# Valores máximos e mínimos para a temperatura do ar
temp_max = df['temp_ar_bulbo_seco_c'].max()
temp_min = df['temp_ar_bulbo_seco_c'].min()
print(f"Temperatura máxima: {temp_max} °C, Temperatura mínima: {temp_min} °C")


```

Quantos registros tinham valores nulos antes do tratamento?


```python

# Contagem de valores nulos por coluna
valores_nulos = df.isnull().sum()
print(f"Valores nulos por coluna:\n{valores_nulos}")

```

Qual foi o impacto da normalização de uma coluna específica?

```python
# Normalização da radiação global para MJ/m²
df['radiacao_global_normalizada'] = df['radiacao_global_kjm2'] / df['radiacao_global_kjm2'].max()

print(f"Radiação global normalizada (primeiras linhas):\n{df[['radiacao_global_kjm2', 'radiacao_global_normalizada']].head()}")


```
Que padrões emergiram após a análise dos dados?

```python
# Agrupamento por mês para identificar padrões de precipitação
padrao_precipitacao = df.groupby('mes')['precipitacao_total_mm'].mean()
print(f"Média de precipitação por mês:\n{padrao_precipitacao}")


```
Como os dados foram agrupados e quais insights foram gerados?

```python

# Agrupando dados por mês e calculando a média da temperatura do ar
agrupamento_mes = df.groupby('mes')['temp_ar_bulbo_seco_c'].mean()
print(f"Média de temperatura por mês:\n{agrupamento_mes}")

```
Quais visualizações forneceram as informações mais valiosas?

```python
# Gráfico de barras da precipitação total por mês
df.groupby('mes')['precipitacao_total_mm'].sum().plot(kind='bar', color='blue')
plt.title('Precipitação Total por Mês')
plt.xlabel('Mês')
plt.ylabel('Precipitação Total (mm)')
plt.show()


```
Como o uso de SQL contribuiu para a organização dos resultados?

```python
# Consulta SQL para verificar os dados armazenados no banco de dados
cursor.execute('SELECT COUNT(*) FROM clima')
total_registros_db = cursor.fetchone()[0]
print(f"Total de registros no banco de dados: {total_registros_db}")


```
De que forma os gráficos ajudaram na compreensão dos dados?

```python
# Gráfico de linha para visualizar a variação da temperatura ao longo do tempo
plt.plot(df['data'], df['temp_ar_bulbo_seco_c'], color='orange', label='Temperatura do Ar (°C)')
plt.title('Variação da Temperatura ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


```
