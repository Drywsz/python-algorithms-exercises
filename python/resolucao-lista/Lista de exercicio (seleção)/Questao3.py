'''03. Construa um algoritmo que receba dois números inteiros, calcule o resto da divisão inteira
do número maior pelo número menor e mostre o valor obtido.''' 

#Entrada
num1 = int(input("Insira o primeiro numero inteiro: "))
num2 = int(input("Insira o segundo número inteiro: "))

#Processamento
if num1 > num2: 
    divisao = num1 % num2
    print (divisao)
else:
    divisao = num2 % num1
    print(divisao)

