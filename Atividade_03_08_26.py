import pandas as pd
import numpy as np

dados = {
    "id": [1, 2, 3, 4, 5],
    "nome":["Ana Souza", "ana souza", "Bruno Lima","Carla Dias", "Diego Alves"],
    "idade":[34, 34,np.nan,178,29],
    "cidade":["Recife","Recife","Salvado", "Curitiba", "Manaus"],
    "salario":[2500, 2500, 3200, 4100, 3800],
    "data_cadastro":["2023-01-15", "2023-01-15", "2023-02-20", "2023-03-10", "2023-04-05"],
}
df = pd.DataFrame(dados)
print(df)

print("\nValores ausentes por colunas")
# print(df.isna().sum()) # conta quantos valores ausentes existem em cada coluna
# print(df.dropna())  # remove linhas com valores ausentes
# print(df.dropna(subset=["salario"]))  # remove linhas com valores ausentes na coluna salario
# print(df.fillna(0))  # substitui valores ausentes por 0
# print(df.dropna(axis=1))  # remove colunas com valores ausentes
print(df.duplicated().sum())  # verifica se existem linhas duplicadas