nome = str(input("Insira o seu nome: "))
senha = str(input("Insira sua senha: "))

while nome == senha:
    print("Sua senha não pode ser igual ao seu nome! Digite outra.")
    nome = str(input("Insira o seu nome: "))
    senha = str(input("Insira uma senha diferente de seu nome: "))


