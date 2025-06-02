import random
from operator import index
from time import sleep

lista_nome = []
lista_cpf = []
lista_código = []
lista_saldo_conta = []
print('-=-=-=-=-=-=-=- BANCO -=-=-=-=-=-=-=-')
print('''[ 1 ] ⭢ CRIAR CONTA
[ 2 ] ⭢ DEPOSITAR
[ 3 ] ⭢ SACAR
[ 4 ] ⭢ TRANSFERIR
[ 5 ] ⭢ CONSULTAR SALDO
[ 6 ] ⭢ LISTAR TODAS AS CONTAS
[ 7 ] ⭢ ENCERRAR CONTA''')
print('-=-=-=-=-=-=-=- BANCO -=-=-=-=-=-=-=-')
opção = int(input('➥ Qual a sua opção? '))
while opção != 7:
    if opção == 1:
        def cadrasto_conta():
            print('-'*50)
            nome = str(input('Digite aqui seu nome completo: ')).strip()
            def pegar_cpf():
                while True:
                    cpf = input('Digite o seu CPF: ').strip()
                    if len(cpf) == 11 and cpf.isdigit():
                        print('➥ CPF Aceito! ')
                        return cpf
                    else:
                        print('⚠️ CPF inválido!')
            def formatar_cpf(cpf_usuario):
                return f'{cpf_usuario[0:3]}.{cpf_usuario[3:6]}.{cpf_usuario[6:9]}-{cpf_usuario[9:11]}'
            cpf_usuario = pegar_cpf()
            cpf_formatado = formatar_cpf(cpf_usuario)
            gerador_numero_conta = random.randint(1000, 9999)
            saldo_conta = float(0)
            print('Criando conta...')
            sleep(2)
            print('='*45)
            print('➥ Conta criada!')
            sleep(1.2)
            print('Nome do usuário: {}'.format(nome))
            print('CPF: {}'.format(cpf_formatado))
            print('Código da conta: {}'.format(gerador_numero_conta))
            print('Seu saldo: R${:.2f}'.format(saldo_conta))
            print('-'*50)
            lista_nome.append(nome)
            lista_cpf.append(cpf_formatado)
            lista_código.append(gerador_numero_conta)
            lista_saldo_conta.append(saldo_conta)
        cadrasto_conta()
    elif opção == 2:
        def deposito_conta():
            print('-'*45)
            inspecionar_código_conta = int(input('➥ Informe o número da conta:'))
            print('Procurando...')
            sleep(1.5)
            if inspecionar_código_conta in lista_código:
                index = lista_código.index(inspecionar_código_conta)
                print('Olá, {}!'.format(lista_nome[index]))
                valor = float(input('Qual o valor do deposito?: R$'))
                lista_saldo_conta[index] += valor
                print('Depositando...')
                sleep(2)
                print('Valor depositado com sucesso!')
            else:
                print('⚠️ Conta inexistente.')
                print('-'*45)
        deposito_conta()
    elif opção == 3:
        def saque_conta():
            print('-'*45)
            inspecionar_código_conta = int(input('➥ Informe o número da conta:'))
            print('Procurando...')
            sleep(1.5)
            if inspecionar_código_conta in lista_código:
                index = lista_código.index(inspecionar_código_conta)
                print('Olá, {}!'.format(lista_nome[index]))
                valor = float(input('Qual o valor do saque?: R$'))
                if valor > lista_saldo_conta[index]:
                    print('⚠️ Valor indísponivel')
                else:
                    lista_saldo_conta[index] -= valor
                    print('Sacando dinheiro...')
                    sleep(2)
                    print('Valor sacado com sucesso!')
            else:
                print('⚠️ Conta inexistente.')
            print('-'*45)
        saque_conta()
    elif opção == 4:
        inspecinar_codigo_conta_atual = int(input('➥ Informe o número da conta que será usada: '))
        print('Procurando...')
        sleep(2)
        if inspecinar_codigo_conta_atual in lista_código:
            index_atual = lista_código.index(inspecinar_codigo_conta_atual)
            print('Olá, {}!'.format(lista_nome[index_atual]))
            inspecinar_codigo_conta_remetente = int(input('➥ Informe o número da conta remetente: '))
            print('Procurando...')
            sleep(2)
            if inspecinar_codigo_conta_remetente in lista_código:
                index_remetente = lista_código.index(inspecinar_codigo_conta_remetente)
                print('A conta pra quem você deseja enviar está no nome de "{}".'.format(lista_nome[index_remetente]))
                valor_transferencia_conta = float(input('➥ Qual o valor da transferencia? R$'))
                if valor_transferencia_conta > lista_saldo_conta[index_atual]:
                    print('⚠️ Valor indisponivel.')
                    print('Encerrando programa...')
                    sleep(1.5)
                else:
                    confirmação_transferencia = str(input('➥ Deseja enviar a transferencia de dinheiro? s/n: ')).upper().strip()[0:3]
                    if confirmação_transferencia == 'S' or confirmação_transferencia == 'SIM':
                        lista_saldo_conta[index_remetente] += valor_transferencia_conta
                        lista_saldo_conta[index_atual] -= valor_transferencia_conta
                        print('Enviando a transferencia pro destinatário...')
                        sleep(2)
                        print('Transferencia realizada!')
                    elif confirmação_transferencia == 'N' or confirmação_transferencia == 'NAO':
                        print('⚠️ Transferencia recusada.')
                        print('Encerrando programa...')
                        sleep(1.5)
            elif inspecinar_codigo_conta_remetente not in lista_código:
                print('⚠️ Conta destinatária não encontrada!')
                print('Encerrando programa...')
                sleep(1.5)
        elif inspecinar_codigo_conta_atual not in lista_código:
            print('⚠️ Conta atual não encontrada!')
            print('Encerrando programa...')
            sleep(1.5)
    print('-=-=-=-=-=-=-=- BANCO -=-=-=-=-=-=-=-')
    print('''    [ 1 ] ⭢ CRIAR CONTA
    [ 2 ] ⭢ DEPOSITAR
    [ 3 ] ⭢ SACAR
    [ 4 ] ⭢ TRANSFERIR
    [ 5 ] ⭢ CONSULTAR SALDO
    [ 6 ] ⭢ LISTAR TODAS AS CONTAS
    [ 7 ] ⭢ ENCERRAR CONTA''')
    print('-=-=-=-=-=-=-=- BANCO -=-=-=-=-=-=-=-')
    opção = int(input('➥ Qual a sua opção? '))



