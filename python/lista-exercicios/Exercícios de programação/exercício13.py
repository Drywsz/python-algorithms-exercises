num1 = int(input("Insira um valor inteiro: "))
multiplicador = 0
for i in range (0,10):
    multiplicador = multiplicador + 1
    resultado = num1 * multiplicador
    print(f"{num1} X {multiplicador} = {resultado}")