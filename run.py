from random import randint

Hidden_Pattern=[[' ']*6 for x in range(6)]
Guess_Pattern=[[' ']*6 for x in range(6)]

let_to_num={'A':0,'B':1, 'C':2,'D':3,'E':4,'F':5}

def print_board(board):
    print(' A B C D E F ')
    print(' ***********')
    row_num=1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num +=1

print_board(Guess_Pattern)