paisA = 80000
paisB = 200000
aumentoA = 1.03
aumentoB = 1.015
anos = 0

while (paisA < paisB):
    paisA = paisA * aumentoA
    paisB = paisB * aumentoB
    anos += 1
    print (paisA)
    print (paisB)

print(f"Serão necessário {anos} para o país A ultrapassar o país B")