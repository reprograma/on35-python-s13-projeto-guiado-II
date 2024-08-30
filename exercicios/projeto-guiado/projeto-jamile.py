# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlite3 as sql
# %%
<<<<<<< HEAD
df = pd.read_csv('INMET_MS_ITAQUIRAI_2020.csv',delimiter=';',skiprows=8,encoding='latin1',skip_blank_lines=True,skipinitialspace=False)  
=======
df = pd.read_csv('INMET_MS_ITAQUIRAI_2020.csv',delimiter=';',skiprows=8,encoding='latin1',skipinitialspace = True)  
>>>>>>> 46582a74ec1a9d9c924c6e4e178c6641778bee56
df
# %%
df = df.replace(',','.',regex=True)
# %%
df['Data'] = df['Data'].str.replace(' ', '')
# %%
df = df[['Data','Hora UTC','PRECIPITAÇÃO TOTAL, HORÁRIO (mm)','TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)','TEMPERATURA DO PONTO DE ORVALHO (°C)','UMIDADE RELATIVA DO AR, HORARIA (%)','RADIACAO GLOBAL (Kj/m²)','VENTO, DIREÇÃO HORARIA (gr) (° (gr))','VENTO, VELOCIDADE HORARIA (m/s)']]
# %%
df = df.replace(',', '.', regex=True)
# %%
df
# %%
<<<<<<< HEAD
df.isnull().sum()
=======
coluna_objeto = df.select_dtypes(include=['object']).columns
coluna_objeto = coluna_objeto.drop(['Data', 'Hora UTC'])
for coluna in coluna_objeto:
    df[coluna] = pd.to_numeric(df[coluna],errors='coerce')
print(df.dtypes)
# %%
df.head()
>>>>>>> 46582a74ec1a9d9c924c6e4e178c6641778bee56
# %%
df = df.fillna(0)
# %%
df.isnull().sum()
# %%
df
# %%
<<<<<<< HEAD
coluna_objeto = df.select_dtypes(include = ['object']).columns
coluna_objeto = coluna_objeto.drop(['Data','Hora UTC'])
for coluna in coluna_objeto:
    df[coluna] = pd.to_numeric(df[coluna], errors='coerce')
=======

# %%
# df['PRECIPITAÇÃO TOTAL, HORÁRIO (mm)'] = pd.to_numeric(df['PRECIPITAÇÃO TOTAL, HORÁRIO (mm)'], errors='coerce')
# df['TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)'] = pd.to_numeric(df['TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)'], errors='coerce')
# df['TEMPERATURA DO PONTO DE ORVALHO (°C)'] = pd.to_numeric(df['TEMPERATURA DO PONTO DE ORVALHO (°C)'], errors='coerce')
# df['RADIACAO GLOBAL (Kj/m²)'] = pd.to_numeric(df['RADIACAO GLOBAL (Kj/m²)'], errors='coerce')
# df['VENTO, VELOCIDADE HORARIA (m/s)'] = pd.to_numeric(df['VENTO, VELOCIDADE HORARIA (m/s)'], errors='coerce')
# %%

>>>>>>> 46582a74ec1a9d9c924c6e4e178c6641778bee56
# %%
df    
# %%
df.dtypes
# %%
df['UMIDADE RELATIVA DO AR, HORARIA (%)'] = (df['UMIDADE RELATIVA DO AR, HORARIA (%)'] - df['UMIDADE RELATIVA DO AR, HORARIA (%)'].min()) / (df['UMIDADE RELATIVA DO AR, HORARIA (%)'].max() - df['UMIDADE RELATIVA DO AR, HORARIA (%)'].min())
# %%
df
# %%
df_data=pd.to_datetime(df['Data'])
# %%
df_data
# %%
df['Data'] = df_data.dt.strftime('%d/%m/%Y')
# %%
df.dtypes
# %%
df['Hora UTC'] = pd.to_datetime(df['Hora UTC'], format='%H%M UTC', errors='coerce').dt.strftime('%H:%M')
# %%
df
# %%
df['Data e Hora'] = df['Data'] + ' ' + df['Hora UTC']
# %%
df['Data e Hora'] = pd.to_datetime(df['Data e Hora'],errors='coerce')
# %%
df['Data e Hora BR'] = df['Data e Hora'].dt.tz_localize('UTC').dt.tz_convert('America/Sao_Paulo').dt.strftime('%d/%m/%Y %H:%M')
# %%
df = df[['Data','Hora UTC','Data e Hora','Data e Hora BR','PRECIPITAÇÃO TOTAL, HORÁRIO (mm)','TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)','TEMPERATURA DO PONTO DE ORVALHO (°C)','UMIDADE RELATIVA DO AR, HORARIA (%)','RADIACAO GLOBAL (Kj/m²)','VENTO, DIREÇÃO HORARIA (gr) (° (gr))','VENTO, VELOCIDADE HORARIA (m/s)']]
# %%
df.head()
# %%
df.dtypes
# %%
df.set_index('Data e Hora')
# %%
df.head()
# %%
df[['PRECIPITAÇÃO TOTAL, HORÁRIO (mm)', 'TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)',
    'UMIDADE RELATIVA DO AR, HORARIA (%)']].plot(subplots=True)
plt.suptitle('Séries Temporais das Variáveis')
plt.show()
# %%
df.head()
# %%
plt.scatter(df['Data e Hora'] ,df['TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)'],
            c=df['UMIDADE RELATIVA DO AR, HORARIA (%)'],  
            cmap='viridis',  
            alpha=0.7,  
            edgecolors='w')
plt.colorbar(label='Umidade Relativa do Ar (%)')

plt.title('Temperatura do Ar x Umidade Relativa do Ar')
plt.xlabel('Hora e Data')
plt.ylabel('TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)')
plt.show()
# %%
correlacao = df.corr
correlacao
# %%
correlacao2 = df[['UMIDADE RELATIVA DO AR, HORARIA (%)','TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)']].corr
correlacao2
# %%
conn = sql.connect('clima.db')

# persistindo o DataFrame no banco de dados
df.to_sql('clima', conn, if_exists='replace')
# %%
cursor = conn.cursor()
cursor.execute('SELECT * FROM clima')

col_names = [description[0] for description in cursor.description]

# for row in col_names:
#     print(row)

df_db = pd.DataFrame(cursor.fetchall(), columns=col_names)

df_db
# %%
