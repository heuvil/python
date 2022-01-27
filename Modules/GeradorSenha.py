import random

minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
maiusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '+', ',','.', ';', '/', '?', 'ç', 'Ç']
senha = []

total_minuscula_incluido = 0
total_maiuscula_incluido = 0
total_numero_incluido = 0
total_simbolo_incluido = 0

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


def run():
    tamanho = int(input("Qual o tamanho da senha: "))

    if tamanho <= 10:
        print("!!! ATENÇAO - senha muito pequena, valor alterado para 10 pelo sistema - ATENÇAO")
        tamanho = 10

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
        ''.join(senha)
    print(*senha, sep='')

    # para melhorar no futuro:
    # se nao tiver ao menos 1 de cada tipo, gerar a senha novamente

    # minuscula_obrigatoria =
    # maiuscula_obrigatoria =
    # simbolo_obrigatoria =
    # numero_obrigatoria =
    #
    # senha.clear()
    #
    # for posicao in range (1, tamanho + 1):
    #
    #     tipo = random.randint(1,5)
    #
    #     if tipo == 1:
    #         aleatorio = random.choice(minusculas)
    #         total_minuscula_incluido += 1
    #     elif tipo == 2:
    #         aleatorio = random.choice(maiusculas)
    #         total_maiuscula_incluido += 1
    #     elif tipo == 3:
    #         aleatorio = random.choice(numeros)
    #         total_numero_incluido += 1
    #     else:
    #         aleatorio = random.choice(simbolos)
    #         total_simbolo_incluido += 1
    #
    #     senha.append(aleatorio)
    #     ''.join(senha)
    #
    # print(*senha, sep='')

