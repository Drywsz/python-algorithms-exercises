'''02. Construa um algoritmo que peça ao usuário três números inteiros, determine o maior deles
e o mostre.'''

#Entrada
n1 = float(input("Insira o primeiro número: "))
n2 = float(input("Insira o segundo número: "))
n3 = float(input("Insira o terceiro número: "))

#Constante
menor = n1

#Processamento
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

#Saída
print(menor)