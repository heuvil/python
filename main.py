from Modules import Bissexto, PedraPapelTesoura

print("1 - Ano Bissexto")
print("2 - Pedra, Papel ou Tesoura?")

escolha = int(input("faça uma escolha: "))

if escolha == 1:
    Bissexto.run()
elif escolha == 2:
    PedraPapelTesoura.run()
else:
    print("Escolha invalida")