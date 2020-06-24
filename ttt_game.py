# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 13:30:57 2020

@author: bradl
"""

row1 = {'Top Left':' ', 'Space1T':'|', 'Top Middle':' ', 'Space2T':'|','Top Right':' '}
row2 = {'Mid Left':' ', 'Space1T':'|', 'Mid Middle':' ', 'Space2T':'|','Mid Right':' '}
row3 = {'Bottom Left':' ', 'Space1T':'|', 'Bottom Middle':' ', 'Space2T':'|','Bottom Right':' '}

rows = [row1,row2,row3]
player = 'X'
game_over = False
turns = 0

def the_board():
    ''''
    Inputs: Each Row of the board.
    Outputs: Displays the current board state to the user
    
    '''
    for key, value in row1.items():
        print(value, end='')
    print('\n-----')
    for key, value in row2.items():
        print(value, end='')
    print('\n-----')
    for key, value in row3.items():
        print(value, end='')
        

def check_key():      
    #Checks to see if the input is a valid key
    selection = False
    counter = 0
    moves_counter = 0
    while selection == False:
        user_choice = input('Enter Your Move: ')
        for dict in rows:
            if user_choice in dict:
                #print('bingo') just for testing
                selection = True
                next = rows[counter]
                break
            else:
                counter +=1
            if counter > 2:
                print('Please enter a valid Option')
                counter = 0
                break
        #start of the check for an open space
        if selection == True: #need to add user input. Also need to add a way for this to start the whole function over if this fails. Could be to just exit all the way out and have that handled but a while loop that this sits under?
            if 'X' in next[user_choice] or 'O' in next[user_choice]:
                print('Please Select an Open Space')
                selection = False
                moves_counter +=1
                counter = 0
            else:
                #print('This is Open') This is for testing
                break
    return user_choice
        
def add_move(position):
    if player == 'X':
        for row in rows:
            if position in row:
                row[position] = 'X'
    elif player == 'O':
        for row in rows:
            if position in row:
                row[position] = 'O'  

def swap_player(player):
    #This alternates the placement of X and O between players
    if player == 'X':
        player = 'O' 
        return player
    elif player == 'O':
        player = 'X'
        return player


def turn(player):
    position = check_key()
    add_move(position)
    the_board()
    player = swap_player(player)
    return player


def endgame(): #takes player variable
    game_over = False
    nl ='\n'
    while game_over == False:
        #first check for horizontal
        if rows[0]['Top Left'] == player and rows[0]['Top Middle'] == player and rows[0]['Top Right'] == player:
            print(f'{nl}{player} wins!')
            game_over = True
        elif rows[1]['Mid Left'] == player and rows[1]['Mid Middle'] == player and rows[1]['Mid Right'] == player:
            print(f'{nl}{player} wins!')
            game_over = True
        elif rows[2]['Bottom Left'] == player and rows[2]['Bottom Middle'] == player and rows[2]['Bottom Right'] == player:
            print(f'{nl}{player} wins!')
            game_over = True    
        #starts check for vertical victory
        elif rows[0]['Top Left'] == player and rows[1]['Mid Left'] == player and rows[2]['Bottom Left'] == player:
            print(f'{nl}{player} wins!')
            game_over = True
        elif rows[0]['Top Middle'] == player and rows[1]['Mid Middle'] == player and rows[2]['Bottom Middle'] == player:
            print(f'{nl}{player} wins!')
            game_over = True
        elif rows[0]['Top Right'] == player and rows[1]['Mid Right'] == player and rows[2]['Bottom Right'] == player:
            print(f'{nl}{player} wins!')
            game_over = True
        #diagonal victories
        elif rows[0]['Top Left'] == player and rows[1]['Mid Middle'] == player and rows[2]['Bottom Right'] == player:
            print(f'{nl}{player} wins!')
            game_over = True
        elif rows[0]['Top Right'] == player and rows[1]['Mid Middle'] == player and rows[2]['Bottom Left'] == player:
            print(f'{nl}{player} wins!')
            game_over = True     
        else:
            #print('no') #for testing only
            break
    return game_over


#The Game    
while game_over == False:
    #Have a player take a turn
    player = turn(player)
    #if the number of turns is >4 check for the wincon
    if turns < 4:
        turns +=1
        #print(turns) #for testing only
    else:
        the_end = endgame()
        if the_end == True:
            game_over = True
        elif the_end == False and turns < 9:
            turns +=1
            #print(str(turns)+'two') #for testing only
            if turns >= 9:
                game_over = True
                print('Game is Tied')
