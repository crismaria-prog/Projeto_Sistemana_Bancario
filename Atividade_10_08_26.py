# import matplotlib.pyplot as plt
# import seaborn as sns

# #DADOS --> GRAFICO DE LINHA  --- SEMANAS --- QUANTIDADE DE ALUNOS

# dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
# alunos = [12,10,10,20,25]

# # CRIAR O MEU GRAFICO DE LINHA

# sns.lineplot(x=dias, y=alunos, marker='o', color='red', linestyle='--')
# plt.title('Quantidade de Alunos por Dia da Semana')
# plt.xlabel('Dias da Semana')
# plt.ylabel('Quantidade de Alunos')
# plt.show()

# # TITULO DO GRAFICO

# plt.title('Quantidade de Alunos por Dia da Semana')

# # ROTULOS DOS EIXOS

# plt.xlabel('Dias da Semana')
# plt.ylabel('Quantidade de Alunos')

# # IMPRIMIR O GRAFICO NA TELA

# plt.show()

# --------------------- EXEMPLO 2 GRAFICO DE BARRAS ---------------------

#DADOS --> GRAFICO DE BARRAS  --- SEMANAS --- QUANTIDADE DE ALUNOS

# dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
# alunos = [12,10,10,20,25]

# # CRIAR O MEU GRAFICO DE LINHA

# sns.barplot(x=dias, y=alunos, color='red')
# plt.title('Quantidade de Alunos por Dia da Semana')
# plt.xlabel('Dias da Semana')
# plt.ylabel('Quantidade de Alunos')
# plt.show()


#------------------- EXEMPLO 3 GRAFICO DE DISPERSÃO ---------------------

# dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
# alunos = [12,10,10,20,25]

# # CRIAR O MEU GRAFICO DE DISPERSÃO

# sns.scatterplot(x=dias, y=alunos, color='red')
# plt.title('Quantidade de Alunos por Dia da Semana')
# plt.xlabel('Dias da Semana')
# plt.ylabel('Quantidade de Alunos')
# plt.show()

#----------------- ATIVIDADE APLICADA 10/08/2026 ---------------------

# vendas = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500]
# meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

# fig, ax = plt.subplots(figsize=(8, 5))
# ax.plot(meses, vendas, marker='o', color='#2ecc71', linestyle='-', label="Loja Centro")
# ax.set_title('Vendas Mensais', fontsize=16)
# ax.set_xlabel('Mês')
# ax.set_ylabel('Vendas (R$)')
# ax.legend()
# plt.savefig('vendas.png', dpi=300)


#------------- EXEMPLO COLEGA EM SALA 1----------------------

# import matplotlib.pyplot as plt
# import seaborn as sns

# meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
# vendas = [1800, 1200, 7000, 10000, 8500, 15000, 5000, 4000, 9000, 1500, 5600, 15000]

# fig, ax = plt.subplots(figsize=(8, 5))
# ax.plot(meses, vendas, color='gold', linewidth=2)
# ax.set_title("Vendas Mensais")
# ax.set_xlabel("Mes")
# ax.set_ylabel("Vendas (R$)")
# ax.legend(["Loja Centro"])
# plt.savefig("vendas_ano.png", dpi=300)

# #----------------- EXEMPLO COLEGA EM SALA 2----------------------
# import matplotlib.pyplot as plt
# import seaborn as sns

# #Grafico de Linha Semanas qtd alunos
# dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
# variacao = [12.45, 12.80, 11.90, 11.76, 12.10]

# #Criar Gráfico
# sns.lineplot(x=dias, y=variacao, marker="o", color="red")
# #sns.barplot(x=dias, y=alunos, color="red")
# #sns.scatterplot(x=dias, y=variacao, color="blue")

# plt.title("Variação de preço da ação ao longo da semana")

# plt.xlabel("Dias da Semana")
# plt.ylabel("Preço R$")
# plt.savefig("grafico_linha.png", dpi=300)

# plt.show()

#----------------- CARREGAR IMAGEM ----------------------
import matplotlib.pyplot as plt
from PIL import Image
from urllib.request import Request, urlopen

# Carregar a imagem
url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"

#Caso não consiga abrir a imagem, vc pode tentar esse caminho alternativo utilizando requests
req = Request(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

# Abrir a imagem usando PIL
imagem = Image.open(urlopen(req))
plt.imshow(imagem)
plt.show()
