from Modules import Bissexto, PedraPapelTesoura, GeradorSenha

print("1 - Ano Bissexto")
print("2 - Pedra, Papel ou Tesoura?")
print("3 - Gerador de senha?")

escolha = int(input("faça uma escolha: "))

if escolha == 1:
    Bissexto.run()
elif escolha == 2:
    PedraPapelTesoura.run()
elif escolha == 3:
    GeradorSenha.run()
else:
    print("Escolha invalida")