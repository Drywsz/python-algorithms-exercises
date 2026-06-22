
lista = []
maior = 0

for i in range (1,6):
    numero = float(input("Insira os 5 numeros: "))
    lista.append(numero) 
    print(lista)
    if i == 1:
        maior = numero
    elif numero > maior:
        maior = numero
print (f"O maior número é {maior}")    
    
