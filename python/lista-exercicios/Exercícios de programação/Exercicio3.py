nome = str(input("Insira o seu nome: "))

while len(nome) <= 3:
    print("O nome deve conter mais de 3 caracteres")
    nome = str(input("Insira o seu nome: "))

idade = int(input("Insira sua idade (Deve estar entre 0 até 150): "))

while (idade < 0 or idade > 150):
    print("Insira uma idade de 0 até 150")
    idade= int(input("Insira sua idade: "))

salario = float(input("Insira o valor de seu salário (Deve ser maior que 0!): "))

while (salario <= 0):
    print("O salário deve ser maior que 0")
    salario = float(input("Insira o valor de se salário (Deve ser maior que 0!): "))

estadoc = str(input("Insira seu estado civil (Solteiro 's', Casado 'c', Viúvo 'v', Divórciado 'd': )")).lower()

while (estadoc != 's' and estadoc != 'c' and estadoc != 'v' and estadoc != 'd'):
    print ("Insira seu estado civíl! (s, c, v ou d)")
    estadoc = str(input("Insira seu estado civil (Solteiro 's', Casado 'c', Viúvo 'v', Divórciado 'd':")).lower()

print (nome, idade, salario, estadoc)



