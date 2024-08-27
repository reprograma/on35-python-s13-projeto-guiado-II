# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as ptl
import datetime

# %%
pd.options.display.date_dayfirst = True
# %%
df = pd.read_csv('INMET_MS_ITAQUIRAI_2020.csv',delimiter=';',skiprows=8,encoding='latin1')  
df
# %%
df = df.replace(',','.',regex=True)
# %%
df['Data'] = df['Data'].str.replace(' ', '')
df['Data'] = df['Data'].str.replace(' ', '')
# %%
df = df[['Data','Hora UTC','PRECIPITAÇÃO TOTAL, HORÁRIO (mm)','TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)','TEMPERATURA DO PONTO DE ORVALHO (°C)','UMIDADE RELATIVA DO AR, HORARIA (%)','RADIACAO GLOBAL (Kj/m²)','VENTO, DIREÇÃO HORARIA (gr) (° (gr))','VENTO, VELOCIDADE HORARIA (m/s)']]
df
# %%
df.head()
# %%
df.shape
# %%
df.isnull().sum()
# %%
df = df.fillna(0)
# %%
df.isnull().sum()
# %%
df
# %%
coluna_objeto = df.select_dtypes(include = ['object']).columns
coluna_objeto = coluna_objeto.drop(['Data','Hora UTC'])
for coluna in coluna_objeto:
    df[coluna] = pd.to_numeric(df[coluna], errors='coerce')
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
df = df[['Data','Hora UTC','Data e Hora','PRECIPITAÇÃO TOTAL, HORÁRIO (mm)','TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)','TEMPERATURA DO PONTO DE ORVALHO (°C)','UMIDADE RELATIVA DO AR, HORARIA (%)','RADIACAO GLOBAL (Kj/m²)','VENTO, DIREÇÃO HORARIA (gr) (° (gr))','VENTO, VELOCIDADE HORARIA (m/s)']]
# %%
df
# %%
