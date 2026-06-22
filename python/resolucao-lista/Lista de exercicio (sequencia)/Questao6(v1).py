'''O restaurante a quilo Bem-Bão cobra R$12,00 por cada quilo de refeição. Escreva um
algoritmo que leia o peso do prato montado pelo cliente (em quilos) e imprima o valor a pagar.
Assuma que a balança já desconte o peso do prato.'''


#Constantes
valordokg = 12

#Entradas
kilosdacomida = (float(input("insira quantos kg de comida você colocou em seu prato (ex: 0.5): ")))

#Processamento
valorfinal = kilosdacomida * valordokg

#Saída

print (f"A conta de seu prato é de R${valorfinal:.2f}")