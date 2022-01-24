

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hands = [rock, paper, scissors]
result_matrix = [["ninguém ganhou", "você perdeu.", "você ganhou!"],
                 ["você ganhou!", "ninguém ganhou", "você perdeu."],
                 ["você perdeu.", "você ganhou!", "ninguém ganhou"]]


def run():
    player_choice = int(input(("escola 1 para pedra, 2 para papel ou 3 para tesoura: ")))
    print(hands[player_choice-1])
    computer_choice = random.randint(1,3)
    print("escolha do computador:")
    print(hands[computer_choice-1])
    print(result_matrix[player_choice-1][computer_choice-1])
