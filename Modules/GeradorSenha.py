import random

minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
maiusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '+', ',','.', ';', '/', '?', 'ç', 'Ç']
senha = []

# total_minuscula_incluido = 0
# total_maiuscula_incluido = 0
# total_numero_incluido = 0
# total_simbolo_incluido = 0

def run():

    maiuscula_obrigatoria = input("Maiuscula obrigatoria? (S/N): ")
    simbolo_obrigatoria = input("Simbolo obrigatorio? (S/N): ")
    numero_obrigatoria = input("Numero obrigatorio? (S/N): ")

    tamanho = int(input("Qual o tamanho da senha: "))

    if tamanho <= 10:
        print("!!! ATENÇAO - senha muito pequena, valor alterado para 10 pelo sistema - ATENÇAO")
        tamanho = 10

    senha.clear()

    if maiuscula_obrigatoria == "S" or maiuscula_obrigatoria == "s":
        aleatorio = random.choice(maiusculas)
        senha.append(aleatorio)
        tamanho -= 1
    if simbolo_obrigatoria == "S" or simbolo_obrigatoria == "s":
        aleatorio = random.choice(simbolos)
        senha.append(aleatorio)
        tamanho -= 1
    if numero_obrigatoria == "S" or numero_obrigatoria == "s":
        aleatorio = random.choice(numeros)
        senha.append(aleatorio)
        tamanho -= 1

    aleatorio = random.choice(minusculas)
    senha.append(aleatorio)

    for posicao in range (1, tamanho + 1):

        tipo = random.randint(1,5)

        if tipo == 1:
            aleatorio = random.choice(minusculas)
        elif tipo == 2:
            aleatorio = random.choice(maiusculas)
        elif tipo == 3:
            aleatorio = random.choice(numeros)
        else:
            aleatorio = random.choice(simbolos)

        senha.append(aleatorio)

    random.shuffle(senha)
    print(*senha, sep='')

