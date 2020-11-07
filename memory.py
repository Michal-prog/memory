import os 
import sys 
from random import randint
import random
import string
os.system("cls || clear")

number_col = 4
number_row = 5 


def tab_game(number_col, number_row):
    board = []
    board_finish = []



    for k in range(number_row):
        for i in range(int(number_col)):
            alphabet = string.ascii_letters
            random_letter = random.choice(alphabet).lower()
            board.append(random_letter)

    board_finish.append(board)
    
    return board_finish

    



def main():
    board_finish = tab_game(number_col, number_row)
   
    print(board_finish)


main()