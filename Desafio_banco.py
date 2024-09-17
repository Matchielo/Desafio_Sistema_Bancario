saldo = 2000
saque_diario = 3
extrato = ''
opcao = -1

print('{:-^30}'.format('Sistema Bancário'))

while True:
    print('''
    [1] - Sacar valores 
    [2] - Extrato 
    [3] - Depositar 
    [0] - Sair 
          ''')

    opcao = int(input(' Digite um valor: '))
    print('')
    print('-'*30)
    print('')

    if opcao == 1:
        print('{:-^30}'.format(' Sistema de Saque '))
        print('')

        if saque_diario == 0:
            print("A quantidade de saque diária atingiu o limite!")
            print('')
            print('-'*30)

        elif saque_diario > 0:
            print('Digite o valor para saque: ')
            sacar = float(input('R$ '))
            print('')
            print('-'*30)
            print('')

            if sacar <= 0:
                print('{:-^30}'.format(' Sistema de Saque '))
                print('')
                print('Valor invalido')
                print('')
                print('-'*30)

            elif sacar > 500:
                print('{:-^30}'.format(' Sistema de Saque '))
                print('')
                print('Valor de saque maior que limite definido!')
                print('')
                print('-'*30)

            else:
                if sacar <= saldo:
                    saldo -= sacar
                    saque_diario -= 1
                    extrato += f'Saque: R$: {sacar:.2f}\n'
                    print('{:-^30}'.format(' Sistema de Saque '))
                    print('')
                    print('Saque realizado com sucesso!')
                    print(f'Seu saldo Atual é : R${saldo:.2f}')
                    print(f'saque limites diários: {saque_diario}')
                    print('')
                    print('-'*30)
                    print('')

                else:
                    print('{:-^30}'.format(' Sistema de Saque '))
                    print('')
                    print('Saldo insuficiente para saque!')
                    print('')
                    print('-'*30)
                    print('')

    elif opcao == 2:
        print('{:-^30}'.format(' Extrato '))
        print('')
        print('Não foram realizado movimentações!' if not extrato else extrato)
        print('')
        print(f'Saldo R$: {saldo:.2f}')
        print('')
        print('-'*30)
        print('')

    elif opcao == 3:
        print('{:-^30}'.format(' Sistema de Depósito '))
        print('')
        print('Digite o valor para depósito:')
        print('')
        print(f' Saldo: R$ {saldo}')
        depositar = float(input('R$:'))
        print('')
        print('-'*30)
        print('')

        if depositar <= 0:
            print('{:-^30}'.format(' Sistema de Depósito '))
            print('')
            print('Valor invalido, favor digitar um valor válido')
            print('')
            print('-'*30)
            print('')
        else:
            saldo += depositar
            print('{:-^30}'.format(' Sistema de Depósito '))
            extrato += f'Depósito: R$ {depositar:.2f}\n'
            print('')
            print('Depósito realizado com sucesso!')
            print('')
            print('-'*30)
            print('')

    elif opcao == 0:
        print('Obrigado por usar o nosso sistema!')
        print('')
        print('-'*30)
        print('')
        break

    else:
        print('Valor inválido. \nFavor digitar um valor indicado pelo sistema!')
        print('')
        print('-'*30)
        print('')
