paisA = float(input("Insira o numero da população A: "))
paisB = float(input("Insira o numero da população B: "))
por1 = float(input("Insira o valor do aumento em % de A: "))
por2 = float(input("Insira o valor do aumento em % de B: "))


anos = 0

while (paisA < paisB):
    aumentoA = paisA * (por1 / 100)
    aumentoB = paisB * (por2 / 100)
    paisA += aumentoA
    paisB += aumentoB
    anos += 1
    print (paisA)
    print (paisB)

print(f"Serão necessário {anos} anos para o país A ultrapassar o país B")

