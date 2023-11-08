
bem_vindo = """
=====================================💲💲💲💲💲💲💲💲=====================================
                                Bem vindos ao Central Bank!

Pressione [1] para prosseguir para sua conta.
Pressione [2] para fazer uma consulta rápida de saldo.
Pressione [0] para Sair.

=====================================💲💲💲💲💲💲💲💲=====================================
"""


menu = """
=====================================CENTRAL BANK=====================================
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
=====================================💲💲💲💲💲💲💲💲=====================================
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

bem_vindo = input(bem_vindo)

if bem_vindo == "1":
    while True:
        
        opcao = input(menu)

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite

            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")

            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")

            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1

            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "3":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
elif bem_vindo == "2":
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
elif bem_vindo == "0":
    quit


print("Obrigado por utilizar nossos serviços!💰💲")


# Criar a opção de fazer uma nova operação ou sair
# nova_operacao = input(("Pressione [S] para realizar uma nova operação: \nPressione [N] para sair. \n"))
#         if nova_operacao == "S":
#                 opcao = input(menu)
#         elif nova_operacao == "N":
#             break