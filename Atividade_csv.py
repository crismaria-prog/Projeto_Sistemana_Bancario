import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
df = pd.read_csv("clientes.csv")

# Remover linhas duplicadas
df = df.drop_duplicates()

# Tratar salários ausentes com a mediana
df["salario"] = df["salario"].fillna(df["salario"].median())

# Remover idades inválidas e valores ausentes
df = df[df["idade"].between(0, 100)]

# Criar faixas salariais
df["faixa_salarial"] = pd.cut(
    df["salario"],
    bins=[0, 2000, 5000, 10000, np.inf],
    labels=["Baixa", "Média", "Alta", "Muito Alta"],
    include_lowest=True
)

# Salvar os dados tratados em um novo arquivo CSV
df.to_csv("clientes_tratados.csv", index=False)

print("Arquivo 'clientes_tratados.csv' criado com sucesso!")
print(df)