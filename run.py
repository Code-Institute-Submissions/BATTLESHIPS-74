from random import randint

Hidden_Pattern=[[' ']*8 for x in range(8)]
Guess_Pattern=[[' ']*8 for x in range(8)]

let_to_num={'A':0,'B':1, 'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}

def print_board(board):
    print(' A B C D E F G H')
    print(' ***************')
    row_num=1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num +=1

def get_ship_location():

    row=input('Please enter a ship row 1-6 ').upper()
    while row not in '123456':
        print("Please enter a valid row ")
        row=input('Please enter a ship row 1-6 ')

    column=input('Please enter a ship column A-F ').upper()
    while column not in 'ABCDEF':
        print("Please enter a valid column ")
        column=input('Please enter a ship column A-F ')
    return int(row)-1,let_to_num[column]

def create_ships(board):
    for ship in range(5):
        ship_r, ship_cl=randint(0,7), randint(0,7)
        while board[ship_r][ship_cl] =='X':
            ship_r, ship_cl = randint(0, 7), randint(0, 7)
        board[ship_r][ship_cl] = 'X'

def count_hit_ships(board):
    count=0
    for row in board:
        for column in row:
            if column=='X':
                count+=1
    return count
