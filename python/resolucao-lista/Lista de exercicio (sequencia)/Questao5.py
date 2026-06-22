'''5. Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um algoritmo para
ler o preço do litro da gasolina e o valor do pagamento, e exibir quantos litros ele conseguiu
colocar no tanque.'''

#Entradas
precog = float(input("insira o preço do litro da gasolina: "))
qtdgasolina = float(input("insira quantos reais de gasolina você quer colocar: "))

#Processamento

litro = qtdgasolina / precog

#Saída
print(f"você conseguiu colocar {litro:.2f} litros de gasolina no tanque")

