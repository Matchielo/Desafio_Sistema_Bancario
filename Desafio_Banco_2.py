import datetime

d = datetime.datetime.now()
mascara = '%d/%m/%Y %H:%M'


ap = ' Seja Bem Vindo ao nosso Sistema! '

print('')
print(f'{ap:^50}')
print('')


def menu():
    print('')
    print('{:-^50}'.format(' Sistema Bancário '))
    menu = '''

Digite o valor desejado: 

    [0] - Exit:
    [1] - Depositar:
    [2] - Sacar: 
    [3] - Extrato:

    [NC] - Nova  Conta:
    [LC] - Listar Contas:
    [NU] - Novo Usuário:
    
>>>    
'''
    return input(menu)


def depositar(saldo, valor, extrato, /):  # Está inserindo chaves por posição
    if valor > 0:  # Se valor for maior que zero
        saldo += valor  # Adiciona valores a saldo
        # Insere os valores na variável extrato
        extrato += f' Depósito: R${valor:.2f} - {d.strftime(mascara)}'

        print('')
        print('{:-^50}'.format(' Depósito '))
        print('''
              
    Depósito realizado com sucesso!

              ''')

    else:
        print('')
        print('{:-^50}'.format(' Erro '))
        print('''
              
    Valor inválido. 
    Favor digitar um valor indicado pelo sistema!

              ''')

    return saldo, extrato

# Está inserindo chaver nomeadas


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    # Depois do caracter '*' tudo é nomeado

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    # Padronização das mensagens

    if excedeu_saldo:
        print('')
        print('{:-^50}'.format(' Erro '))
        print('''
              
    Operação Falhou! 
    Saldo insuficiente!
              
              ''')

    elif excedeu_limite:  # caso o limite ultrapassar o valor indicado
        print('')
        print('{:-^50}'.format(' Erro '))
        print('''
              
    Operação Falhou! 
    O valor do saque excedeu o limite!
              
              ''')

    elif excedeu_saques:  # caso o limite de saques ultrapassar o valor indicado
        print('')
        print('{:-^50}'.format(' Erro '))
        print('''
              
    Operação Falhou! 
    O numero de saques excedeu o limite!
              
              ''')

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f} - {d.strftime(mascara)}'
        numero_saques += 1
        print('')
        print('{:-^50}'.format(' Saque '))
        print(f'''

    Saque realizado com sucesso!
    Saldo atual: R$ {saldo:.2f}

                ''')

    else:
        print('')
        print('{:-^50}'.format(' Erro '))
        print('''
              
    Operação Falhou! 
    O valor informado é inválido!
              
              ''')

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print('{:-^50}'.format(' Extrato '))
    print('''
              
    Não foram realizados movimentações.
              
        ''' if not extrato else extrato)
    print(f'''

    Saldo: R$ {saldo:.2f}

        ''')


def criar_usuarios(usuarios):
    print('')
    print('{:-^50}'.format(' Cadastro '))
    print('')

    cpf = input('Informe o número de CPF (Somente numeros): ')
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:  # Se o usuario já existe

        print('''
              
    Já existe usuário com esse CPF.
              
        ''')
        return

    nome = input('Informe o nome completo: ')
    print('')
    data_nascimento = input('Informe  a data de nascimento (dd/mm/aaaa): ')
    print('')
    telefone = input('Informe o número de telefone: ')
    print('')
    email = input('Informe o e-mail: ')
    print('')

    # Adiciona as informações recebidas como dicionário
    usuarios.append({"nome": nome, 'data_nascimento': data_nascimento,
                     "cpf": cpf, 'telefone': telefone, 'email': email})

    print('')
    print('{:-^50}'.format(' Cadastro '))
    print(f'''

    Usuário cadastrado com sucesso!
    {nome} foi adicionado ao sistema.

    ''')


def filtrar_usuarios(cpf, usuarios):
    # Compressão de lista
    usuarios_filtrados = [
        usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
    # vai verificar se existe uma lista vazia


def listar_contas(contas):
    for conta in contas:
        linha = f'''

    Agencia: {conta['agencia']}
    C/C: {conta['numero_conta']}
    Titular: {conta['usuario']['nome']}

        '''
    print('{:-^50}'.format(' Listar Contas '))
    print(linha)


def criar_contas(agencia, numero_conta, usuarios):
    print('')
    print('{:-^50}'.format(' Criar Conta '))

    print('')
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print('')
        print('{:-^50}'.format(' Criar contas '))
        print(''' 

    Conta Criada com sucesso!

        ''')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}

    print('')
    print('{:-^50}'.format(' Erro '))
    print(''' 
          
    Usuário não encontrado.
    Fluxo de Criação de conta encerrada.
          
         ''')


def main():
    LIMITE_SAQUES = 10
    AGENCIA = '0001'

    saldo = 0  # Variável para saque
    limite = 500
    extrato = ""
    numero_saques = 0  # Cria uma variável para o número de saques onde será incrementado quando for feito cada saque
    usuarios = []  # Cria uma lista para usuários vazia
    contas = []  # Cria uma lista para contas vazia

    while True:

        opcao = menu()  # Chama a função "def menu" para apresentar os valores botões de acesso

        if opcao == '1':   # Se a opção escolhida for 1, chama a função "def criar
            print('')
            print('{:-^50}'.format(' Depósito '))
            print('''  
                  
    Digite o valor para depósito: 
    
            ''')
            valor = float(input('R$: '))
            print('')

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":   # Se a opção escolhida for 2, chama a função "def criar
            print('')
            print('{:-^50}'.format(' Saque '))
            print(f'''

    Saldo Disponível em conta: R$ {saldo}

    Digite o valor para saque:

            ''')
            valor = float(input('R$: '))

            # Retorna duas funções - Passagem de argumentos
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":  # Função para exibir o extrato
            exibir_extrato(saldo, extrato=extrato)   # Passagem de argumentos

        elif opcao == 'NU':
            # Chama a função "def criar_usuarios" para criar usuários
            criar_usuarios(usuarios)

        elif opcao == "NC":
            # Cria uma variável para o número da conta
            numero_conta = len(contas + 1)
            # Chama a função "def criar_contas" para criar contas
            conta = criar_contas(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 'LC':
            listar_contas(contas)

        elif opcao == '0':
            print('')
            print('{:-^50}'.format(' Sistema Encerrado '))

            print('''
                  
    Saindo...
                  
                  ''')
            break

        else:   # Caso o usuário digite uma opção inválida
            print('')
            print('{:-^50}'.format(' Erro '))
            print('''
                  
    Operação Inválida!
    Favor Selecionar novamente um operação válida
                  
            ''')


main()
