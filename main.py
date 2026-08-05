import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



saldo = 100
extrato = []
historico_saldos = [saldo]
rotulos_movimentacoes = ["Saldo inicial"]

PASTA_DO_SCRIPT = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_CSV = os.path.join(PASTA_DO_SCRIPT, "extrato_movimentacao.csv")

def criar_arquivo_csv():
    if not os.path.exists(ARQUIVO_CSV):
        with open(ARQUIVO_CSV, mode="w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["Data e hora", "Tipo", "Valor", "Saldo"])

        print(f"\nArquivo CSV criado em: {ARQUIVO_CSV}")

def salvar_no_csv(tipo, valor):
    with open(ARQUIVO_CSV, mode="a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([datetime.now().strftime("%d/%m/%Y %H:%M:%S"), tipo, f"{valor:.2f}", f"{saldo:.2f}"])

def exibir_banco():
    print("\n===== CAIXA ELETRONICO =====")
    print("1- Consultar Saldo")
    print("2- Depositar Dinheiro")
    print("3- Sacar Dinheiro")
    print("4- Ver Extrato")
    print("5- Ver Movimentacao")
    print("6- Relatório Avançado")
    print("7- Sair")

def consultar_saldo():
    print(f"\nSeu saldo atual é: R$ {saldo}")
    pass

def depositar_dinheiro():
    global saldo
    valor = float(input("\nDigite o valor a ser depositado R$ "))
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        historico_saldos.append(saldo)
        rotulos_movimentacoes.append(f"Depósito: R$ {valor:.2f}")
        salvar_no_csv("Depósito", valor)
        print(f"\nDeposito de R$ {valor} realizado com sucesso.")

    else:
        print("\nValor inválido.")
    pass

def sacar_dinheiro():
    global saldo
    valor = float(input("\nDigite o valor a ser sacado R$ "))
    if valor > 0 and valor <= saldo:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        historico_saldos.append(saldo)
        rotulos_movimentacoes.append(f"Saque: R$ {valor:.2f}")
        salvar_no_csv("Saque", valor)
        print(f"\nSaque de R$ {valor} realizado com sucesso.")
    else:
        print("\nSaldo insuficiente ou valor inválido.")
    pass

def ver_extrato():
    print("\n===== EXTRATO =====")
    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        for movimentacao in extrato:
            print(movimentacao)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    pass


def movimentacao():
    if len(historico_saldos) < 2:
        print("\nNenhuma movimentação registrada para mostrar.")
        return

    x = list(range(1, len(historico_saldos) + 1))
    y = historico_saldos

    plt.plot(x, y, color="blue", linestyle="--", marker="o")

    plt.title("Movimentações bancárias")
    plt.xlabel("Número da movimentação")
    plt.ylabel("Saldo em R$")
    plt.grid(True)
    plt.show()


def relatorio_avancado():
    print("\n===== RELATÓRIO AVANÇADO =====")

    # --- Parte 1: Pandas -> ler o CSV e organizar como tabela (DataFrame) ---
    # Repare a diferença: em vez de um "for" lendo linha por linha, o pandas
    # carrega o arquivo inteiro em uma tabela e já sabemos manipular colunas.
    colunas = ["Data e hora", "Tipo", "Valor", "Saldo"]
    try:
        df = pd.read_csv(ARQUIVO_CSV, names=colunas)
    except FileNotFoundError:
        print("Nenhuma movimentação registrada ainda.")
        return

    if df.empty:
        print("Nenhuma movimentação registrada ainda.")
        return

    df["Data e hora"] = pd.to_datetime(df["Data e hora"], format="%d/%m/%Y %H:%M:%S", errors="coerce")
    df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce")
    df["Saldo"] = pd.to_numeric(df["Saldo"], errors="coerce")

    print("\n-- Tabela de movimentações (pandas.DataFrame) --")
    print(df.to_string(index=False))

    # groupby: soma os valores agrupando por tipo de movimentação
    print("\n-- Total por tipo (df.groupby) --")
    print(df.groupby("Tipo")["Valor"].sum())

    # describe: estatística descritiva pronta (contagem, média, min, max...)
    print("\n-- Estatística dos valores (df['Valor'].describe()) --")
    print(df["Valor"].describe())

    hoje = df[df["Data e hora"].dt.date == datetime.now().date()]
    print(f"\n-- Movimentações de hoje: {len(hoje)} --")

    # --- Parte 2: NumPy -> cálculos sobre o histórico de saldo ---
    # Toda coluna do pandas já é, por baixo dos panos, um array NumPy.
    # Aqui pegamos essa coluna "pura" para fazer contas em todos os números
    # de uma vez, sem precisar escrever um "for".
    saldos = df["Saldo"].to_numpy()

    print("\n-- Estatísticas do saldo (numpy) --")
    print(f"Saldo médio: R$ {np.mean(saldos):.2f}")
    print(f"Maior saldo: R$ {np.max(saldos):.2f}")
    print(f"Menor saldo: R$ {np.min(saldos):.2f}")
    print(f"Desvio padrão: R$ {np.std(saldos):.2f}")

    # diff: a diferença entre cada saldo e o saldo anterior, tudo de uma vez
    variacoes = np.diff(saldos)
    print("\n-- Variação entre movimentações (numpy.diff) --")
    print(variacoes)


def main():
    criar_arquivo_csv()
    while True:
        exibir_banco()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            consultar_saldo()
        elif opcao == "2":
            depositar_dinheiro()
        elif opcao == "3":
            sacar_dinheiro()
        elif opcao == "4":
            ver_extrato()
        elif opcao == "5":
            movimentacao()
        elif opcao == "6":
            relatorio_avancado()
        elif opcao == "7":
            print("\nSaindo do sistema. Obrigado por utilizar o Caixa Eletrônico.")
            break
        else:
            print("\nOpção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()