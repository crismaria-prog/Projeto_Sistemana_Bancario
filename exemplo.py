import pandas as pd

salarios = pd.Series(
    [3200, 4100, 2800, 5300],
    index=["Ana", "Bruno", "Carla", "Diego"],
    name="salario",
)

print(salarios)
print(salarios["Carla"])  # acesso por rótulo
print(salarios.iloc[0])   # acesso por posição
print(salarios.mean())
