import random

print('-=-=-=-=-=-=-=- BANCO -=-=-=-=-=-=-=-')
print('''[ 1 ] | CRIAR CONTA
[ 2 ] | DEPOSITAR
[ 3 ] | SACAR
[ 4 ] | TRANSFERIR
[ 5 ] | CONSULTAR SALDO
[ 6 ] | LISTAR TODAS AS CONTAS
[ 7 ] | ENCERRAR CONTA''')
print('-=-=-=-=-=-=-=- BANCO -=-=-=-=-=-=-=-')
opção = int(input('-----> Qual a sua opção? '))
while opção != 7:
    if opção == 1:
        print('-'*50)
        nome = str(input('Digite aqui seu nome completo: ')).strip()
        def pegar_cpf():
            while True:
                cpf = input('Digite o seu CPF: ').strip()
                if len(cpf) == 11 and cpf.isdigit():
                    print('--> CPF Aceito! ')
                    return cpf
                else:
                    print('--> CPF inválido!')
        def formatar_cpf(cpf_usuario):
            return f'{cpf_usuario[0:3]}.{cpf_usuario[3:6]}.{cpf_usuario[6:9]}-{cpf_usuario[9:11]}'
        cpf_usuario = pegar_cpf()
        cpf_formatado = formatar_cpf(cpf_usuario)
        gerador_numero_conta = random.randint(1000, 9999)
        print('='*45)
        print('Nome do usuário: {}'.format(nome))
        print('CPF: {}'.format(cpf_formatado))
        print('Código da conta: {}'.format(gerador_numero_conta))
        print('-'*50)
    print('-=-=-=-=-=-=-=- BANCO -=-=-=-=-=-=-=-')
    print('''    [ 1 ] | CRIAR CONTA
    [ 2 ] | DEPOSITAR
    [ 3 ] | SACAR
    [ 4 ] | TRANSFERIR
    [ 5 ] | CONSULTAR SALDO
    [ 6 ] | LISTAR TODAS AS CONTAS
    [ 7 ] | ENCERRAR CONTA''')
    print('-=-=-=-=-=-=-=- BANCO -=-=-=-=-=-=-=-')
    opção = int(input('-----> Qual a sua opção? '))



