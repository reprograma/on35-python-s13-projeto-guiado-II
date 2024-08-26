# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as ptl
# %%
df = pd.read_csv('INMET_MS_ITAQUIRAI_2020.csv',delimiter=';',skiprows=8,encoding='latin1')  
df
# %%
df.dtypes
# %%
df.head()
# %%
df.tail()
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
# df = df.fillna(0, inplace=True)
# %%
df.isnull().sum()
# %%
df.shape
# %%
coluna_objeto = df.select_dtypes(include = ['object']).columns

for coluna in coluna_objeto:
    df[coluna] = pd.to_numeric(df[coluna], errors='coerce')
# %%
df    
# %%
df.dtypes
# %%
df.fillna(0, inplace=True)
# %%
df
# %%
