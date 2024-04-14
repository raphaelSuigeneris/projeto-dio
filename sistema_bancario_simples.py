menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0.00

limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

operacao = list()

while True:
    opcao = input(menu)
    if opcao == "d":     
        try:
            valor_deposito = float(input("Insira um valor para depósito: R$"))
            if valor_deposito > 0:
                saldo += valor_deposito
                operacao.append(f"Depósito realizado: R${valor_deposito:.2f}")
                print (f"Você depositou R${valor_deposito:.2f}")
            else:
                print("O valor informado é inválido!")
        except:
            print("O valor informado é inválido!")
    elif opcao == "s":
        if numero_saques>=LIMITE_SAQUES:
            print("Você já executou o limite diário de saques, tente novamente amanhã.")
        else:
            try:
                valor_saque = float(input("Digite o valor a ser sacado: R$"))
                if valor_saque > saldo:
                    print("Saldo insuficiente!")
                elif valor_saque < 0 or valor_saque > limite:
                    print("O valor informado está fora dos limites!")
                else:
                    saldo -= valor_saque
                    numero_saques += 1
                    operacao.append(f"Saque realizado: R${valor_saque:.2f}")
                    print (f"Você sacou R${valor_saque:.2f}. Número de saques restantes: {LIMITE_SAQUES-numero_saques}")
            except:
                print("O valor informado é inválido!")

    elif opcao == "e":
        print("\n============== EXTRATO ==============")
        for i in range (len(operacao)):
            print(operacao[i])
        print(f"\nSeu saldo atual é de R${saldo:.2f}")
        print("=====================================")

    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")