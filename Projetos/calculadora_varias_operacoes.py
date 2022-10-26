print('|---------------------|')
print('|     Calculadora     |')
print('|---------------------|')

#   Entrada de dados
#   Manipulação de dos
#   Saida de dados
nome = input('Digite seu nome:     ')
senha = input('Digite sua senha:    ')
print('Seja bem vindo {}'.format(nome))
print('Escolha uma opção de calculo abaixo:')
print('|---------------------|')
print('| 1. Divisão          |')
print('| 2. Multplicação     |')
print('| 3. Subtração        |')
print('| 4. Adição           |')
print('|---------------------|')
# Opçoês de calculo
opcao = input('Digite sua opção:   ')
#      1.Divisão 
if opcao == '1' :
    valorUmA = int(input('Digite um valor:  '))
    valorDoisB = int(input('Digite um valor novamente: '))
    soma = valorUmA / valorDoisB
    print('Resultado: {}'.format(soma))
#      2.Multplicação
elif opcao == '2':
    valorUmA = int(input('Digite um valor:  '))
    valorDoisB = int(input('Digite um valor novamente: '))
    soma = valorUmA * valorDoisB
    print('Resultado: {}'.format(soma))
#      3.Subtração
elif opcao == '3':
    valorUmA = int(input('Digite um valor:  '))
    valorDoisB = int(input('Digite um valor novamente: '))
    soma = valorUmA - valorDoisB
    print('Resultado: {}'.format(soma))
#      4. Adição
elif opcao == '4':
    valorUmA = int(input('Digite um valor:  '))
    valorDoisB = int(input('Digite um valor novamente: '))
    soma = valorUmA + valorDoisB
    print('Resultado: {}'.format(soma))
