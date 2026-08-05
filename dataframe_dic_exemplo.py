import pandas as pd

# Criando um DataFrame a partir de um dicionário
# Cada chave do dicionário vira uma coluna do DataFrame
dados = {
    "nome": ["Ana", "Bruno", "Carla", "Diego"],
    "salario": [3200, 4100, 2800, 5300],
    "cargo": ["Analista", "Gerente", "Analista", "Diretor"],
}

df = pd.DataFrame(dados)

print(df)
print()
print(df["salario"])          # acesso a uma coluna
print()
print(df.loc[1])              # acesso a uma linha pelo índice
print()
print(df["salario"].mean())   # média da coluna salario