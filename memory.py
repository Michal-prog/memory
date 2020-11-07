import os 
import sys 
from random import randint
import random
import string
os.system("cls || clear")

board = []

def random_letter_1():
    alphabet = string.ascii_letters
    random_letter = random.choice(alphabet).lower()
    return random_letter

def init_board(random_letter):
    for x in range(10):
        random_letter = random_letter_1()
        board.append(random_letter)
    return board


def print_board(board):
    for row in board:
        print((" ").join(row))

def input_shooting():
    row_letter = input("choose row")
    row = ord(row_letter) - 97 
    col = int(input("choose column")) -1
    return row, col

def input_shooting2():
    row_letter = input("choose row")
    row2 = ord(row_letter) - 97 
    col2 = int(input("choose column")) -1
    return row2, col2

def shooting_placement(row,col,row2, col2, board_O, board_finish):
    board_O[row][col] = board_finish[row][col]
    print(board_O)
    print(board_O[1][1])
    if board_finish[row][col] == board_finish[row2][col2]:
        board_O[row][col] = board_finish[row2][col2]
        print(board_O)
    elif board_finish[row][col] != board_finish[row2][col2]:
        board_O[row][col] = "O"
    return board_O


def main():
    random_letter = random_letter_1()
    board = init_board(random_letter)
    board_1 = board[0:10] + board[0:10]
    random.shuffle(board_1)
    board_finish = [board_1[0:5],board_1[5:10],board_1[10:15],board_1[15:20]]
    print(board_finish[0])
    print(board_finish[1])
    print(board_finish[2])
    print(board_finish[3])

    board_O = []

    for x in range(4):
        board_O.append(["O"] * 5)
    row, col = input_shooting()
    row2, col2 = input_shooting2()
    
    shooting_placement(row,col,row2,col2,board_O, board_finish)
   

main()