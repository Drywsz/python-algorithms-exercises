lista = []
soma = 0

for i in range (1,6):
    numero = float(input("Insira os 5 numeros: "))
    lista.append(numero)
    soma = soma + numero
    

media = soma / len(lista)
print (media)
print(soma)

