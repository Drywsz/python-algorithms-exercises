'''4. Escreva um algoritmo para ler o nome e a idade de uma pessoa, e exibir quantos dias de
vida ela possui. Considere sempre anos completos, e que um ano possui 365 dias. Ex: uma
pessoa com 19 anos possui 6935 dias de vida; veja um exemplo de saída: MARIA, VOCÊ JÁ
VIVEU 6935 DIAS.'''

#Constantes
dias = 365

#Entradas
nome = str(input("Insira o seu nome: "))
idade = int(input("Insira sua idade: "))

#Processamento
vida = idade * dias

#Saída
print(f"{nome.upper()}, você ja viveu {vida} dias")