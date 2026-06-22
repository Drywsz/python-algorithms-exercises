'''01. Construa um algoritmo que peça ao usuário um número inteiro, verifique se ele é par ou
ímpar e mostre uma mensagem com esta informação.'''

#Entrada
num1 = int(input("Insira um número inteiro: "))

#Processamento
if (num1 % 2 == 0):
    print("Par!!")
else: 
    print("Ímpar")
