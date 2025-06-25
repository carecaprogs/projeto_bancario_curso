menu = '''
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao =='1':
        valor =float(input("Informe o valor de depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n '
        else:
            print("Operação falhou! O valor informado é invalido.\U0001F622")

    elif opcao == '2':
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saques:
            print("Operação falho ! Você execedou o limite de saques diarios \U0001F622")

        elif excedeu_saldo:
            print(f'''Operação Falhou ! Você não tem Saldo disponivel \U0001F622
                  Seu saldo atual é: {saldo}''' )

        elif excedeu_limite:
            print(f'Operação falhou! O valor do saque excede o limite.\U0001F622\n', 
                f'Valor Maximo por saque é de : {limite}')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1

        else:
            print('Operação falhou ! Valor informado é invalido \U0001F622')

    elif opcao == '3':
        print("\n===================== EXTRATO =====================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("====================================================")
   
    elif opcao == "0":
     print("\U0001F600 Obrigado por utilizar nossos serviços \U0001F600")
     break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada. \U0001F622")