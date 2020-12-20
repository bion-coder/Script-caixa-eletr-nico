import time
saldo = 500
while True:
    print("BEM VINDO AO CAIXA ELETRÔNICO")
    print('1 - Depósito')
    print("2 - Saque")
    print("3 - Sair")
    print("4 - Visualizar saldo")
    açaoDesejada = int(input('Digite a opção desejada: '))
    cédulaAtual = 50
    totalCédulas = 0

    if açaoDesejada == 1:
        valorDepositado = int(input("Digite o valor que você deseja depositar: "))  #### Funcionamento para valores múltiplos de 10
        saldo = valorDepositado + saldo
        print(f'Obrigado, seu novo saldo é de R$ {saldo} reais')

    elif açaoDesejada == 2:
        valorSaque = int(input("Deseja sacar quantos reais da conta?"))    ## Funcionamento para valores múltiplos de 10
        saldopósSaque = saldo - valorSaque
        if valorSaque <= saldo:
            saldo = saldo - valorSaque
            print('Obrigado, seu novo saldo é R$ {} reais'.format(saldopósSaque))

            while True:
                if valorSaque >= cédulaAtual:
                    valorSaque -= cédulaAtual
                    totalCédulas += 1
                else:
                    if totalCédulas > 0:
                        print(f'Você está sacando {totalCédulas} notas de {cédulaAtual} reais')
                    if cédulaAtual == 100:
                        cédulaAtual = 50
                    elif cédulaAtual == 50:
                        cédulaAtual = 20
                    elif cédulaAtual == 20:
                        cédulaAtual = 10
                    totalCédulas = 0
                    if valorSaque == 0:
                        break
        else:
            print('Você não possui saldo suficiente')
            time.sleep(2)
    elif açaoDesejada == 3:
        print("Obrigado, volte sempre!")
        time. sleep(2)
    elif açaoDesejada == 4:
        print(f'Você possui o valor de R$ {saldo} reais em sua conta')
        time. sleep(2)
    else:
        print("Número incorreto, tente novamente")

    time.sleep(3)


