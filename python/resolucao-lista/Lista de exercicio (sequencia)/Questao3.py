'''3. A padaria Hotpão vende uma certa quantidade de pães franceses e uma quantidade de
broas a cada dia. Cada pãozinho custa R$ 0,12 e a broa custa R$ 1,50. Ao final do dia, o dono
quer saber quanto arrecadou com a venda dos pães e broas (juntos), e quanto deve guardar
numa conta de poupança (10% do total arrecadado). Você foi contratado para fazer os
cálculos para o dono. Com base nestes fatos, faça um algoritmo para ler as quantidades de
pães e de broas, e depois calcular os dados solicitados.'''

#Constantes
pao = 0.12
broa = 1.50
poupanca = 0.1

#Entradas
qtdpao = int(input("Insira quantos pãos você vendeu: "))
qtdbroa = int(input("Insira quantas broas você vendeu: "))

#Processamento
valorp = pao * qtdpao
valorb = broa * qtdbroa
guardar = (valorp + valorb) * poupanca

#Saída
print(f"Você vendeu R${valorp:.2f} pães e R${valorb:.2f} broas, e deve guardar R${guardar:.2f}")


