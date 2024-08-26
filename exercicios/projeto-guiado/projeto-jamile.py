# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as ptl
# %%
df = pd.read_csv('INMET_MS_ITAQUIRAI_2020.csv',delimiter=';',skiprows=8,encoding='latin1',skipinitialspace = True)  
df
# %%
df.dtypes
# %%
df.head()
# %%
df.tail()
# %%
df = df[['Data','Hora UTC','PRECIPITAÇÃO TOTAL, HORÁRIO (mm)','TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)','TEMPERATURA DO PONTO DE ORVALHO (°C)','UMIDADE RELATIVA DO AR, HORARIA (%)','RADIACAO GLOBAL (Kj/m²)','VENTO, DIREÇÃO HORARIA (gr) (° (gr))','VENTO, VELOCIDADE HORARIA (m/s)']]
# %%
df = df.replace(',', '.', regex=True)
# %%
df
# %%
coluna_objeto = df.select_dtypes(include=['object']).columns
coluna_objeto = coluna_objeto.drop(['Data', 'Hora UTC'])
for coluna in coluna_objeto:
    df[coluna] = pd.to_numeric(df[coluna],errors='coerce')
print(df.dtypes)
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

# %%
# df['PRECIPITAÇÃO TOTAL, HORÁRIO (mm)'] = pd.to_numeric(df['PRECIPITAÇÃO TOTAL, HORÁRIO (mm)'], errors='coerce')
# df['TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)'] = pd.to_numeric(df['TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)'], errors='coerce')
# df['TEMPERATURA DO PONTO DE ORVALHO (°C)'] = pd.to_numeric(df['TEMPERATURA DO PONTO DE ORVALHO (°C)'], errors='coerce')
# df['RADIACAO GLOBAL (Kj/m²)'] = pd.to_numeric(df['RADIACAO GLOBAL (Kj/m²)'], errors='coerce')
# df['VENTO, VELOCIDADE HORARIA (m/s)'] = pd.to_numeric(df['VENTO, VELOCIDADE HORARIA (m/s)'], errors='coerce')
# %%

# %%
df    
# %%
df.dtypes
# %%
df.fillna(0, inplace=True)
# %%
df
# %%
