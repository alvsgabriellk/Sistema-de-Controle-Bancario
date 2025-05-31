import random

print('-=-=-=-=-= BANCO -=-=-=-=-=')
print('''[ 1 ] | CRIAR CONTA
[ 2 ] | DEPOSITAR
[ 3 ] | SACAR
[ 4 ] | TRANSFERIR
[ 5 ] | CONSULTAR SALDO
[ 6 ] | LISTAR TODAS AS CONTAS
[ 7 ] | ENCERRAR CONTA''')
print('-=-=-=-=-= BANCO -=-=-=-=-=')
opção = int(input('Qual a sua opção?'))
while opção != 7:
    if opção == 1:
        nome = str(input('Digite aqui seu nome completo:')).strip()
        def pegar_cpf():
            while True:
                cpf = str(input('Digite o seu CPF:'))
                if len(cpf) == 11 and cpf.isdigit():
                    print('CPF Aceito!')
                    return cpf
                else:
                    print('CPF inválido!, tem que ter exatamente 11 digitos.')
            cpf_usuario = cpf
        pegar_cpf()
        def formatar_cpf(cpf_usuario = pegar_cpf()):
            return f'{cpf_usuario[0:3]}.{cpf_usuario[3:6]}.{cpf_usuario[6:9]}-{cpf_usuario[9:11]}'
        cpf_formatado = cpf_formatado(cpf_usuario)
        formatar_cpf()
        gerador_numero_conta = random.randint(1000, 7000)

y



