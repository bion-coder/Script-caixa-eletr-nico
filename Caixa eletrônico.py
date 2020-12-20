import time
saldo = 500
while True:
    print("BEM VINDO AO CAIXA ELETRÔNICO")
    print('1 - Depósito')
    print("2 - Saque")
    print("3 - Área restrita")
    print("4 - Visualizar saldo")
    acaoDesejada = int(input('Digite a opção desejada: '))
    cedulaAtual = 50
    totalCedulas = 0

    if acaoDesejada == 1:
        valorDepositado = int(input("Digite o valor que você deseja depositar: "))  #### Funcionamento para valores múltiplos de 10
        saldo = valorDepositado + saldo
        print(f'Obrigado, seu novo saldo é de R$ {saldo} reais')

    elif acaoDesejada == 2:
        valorSaque = int(input("Deseja sacar quantos reais da conta?"))    ## Funcionamento para valores múltiplos de 10
        saldoposSaque = saldo - valorSaque
        if valorSaque <= saldo:
            saldo = saldo - valorSaque
            print('Obrigado, seu novo saldo é R$ {} reais'.format(saldoposSaque))

            while True:
                if valorSaque >= cedulaAtual:
                    valorSaque -= cedulaAtual
                    totalCedulas += 1
                else:
                    if totalCedulas > 0:
                        print(f'Você está sacando {totalCedulas} notas de {cedulaAtual} reais')
                    if cedulaAtual == 100:
                        cedulaAtual = 50
                    elif cedulaAtual == 50:
                        cedulaAtual = 20
                    elif cedulaAtual == 20:
                        cedulaAtual = 10
                    totalCedulas = 0
                    if valorSaque == 0:
                        break
        else:
            print('Você não possui saldo suficiente')
            time.sleep(2)
    elif acaoDesejada == 3:
        print("Sem acesso! Você será direcionado para aba inicial")
        time. sleep(2)
    elif acaoDesejada == 4:
        print(f'Você possui o valor de R$ {saldo} reais em sua conta')
        time. sleep(2)
    else:
        print("Número incorreto, tente novamente")

    time.sleep(3)


