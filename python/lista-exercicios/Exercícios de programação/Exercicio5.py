inicio = int(input("Insira quantos nímeros devem ser exibidos:  "))
limite = int(input("Insira o limite: "))

valor1 = 0
valor2 = 1
formula = 0

for inicio in range (limite):
    print(f"A sequencia fica {valor1} + {valor2} = {formula}")
    valor1, valor2 = valor2, valor1 + valor2
    formula = valor1
    

    
    
    
