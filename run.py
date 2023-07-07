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

    row=input('Please choose hit zone! (1-6) ').upper()
    while row not in '123456':
        print("That's not the right choice... ")
        row=input('Please enter a ship row 1-6 ')

    column=input('Please enter a ship zone (A-F) ').upper()
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

create_ships(Hidden_Pattern)
turns = 10
while turns > 0:
    print('Welcome to Battleships!')
    print_board(Guess_Pattern)
    row,column =get_ship_location()
    if Guess_Pattern[row][column] == '-':
        print(' Zone already nuetralized!')
    elif Hidden_Pattern[row][column] =='X':
        print(' THATS A HT SOLDIER!')
        Guess_Pattern[row][column] = 'X'
        turns -= 1
    else:
        print('MISS! Shoot again!')
        Guess_Pattern[row][column] = '-'
        turns -= 1
    if  count_hit_ships(Guess_Pattern) == 5:
        print("All enemies neutralized!")
        break
        print(' You have ' +str(turns) + 'turns remaining')
    if turns == 0:
        print('Game Over')
        break
