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

#For display only
show_row1 = {'Top Left    |':' ', '  Top Middle   |':' ',' Top Right':' '}
show_row2 = {'Mid Left    |':' ', '  Mid Middle   |':' ',' Mid Right':' '}
show_row3 = {'Bottom Left |':' ',' Bottom Middle |':' ',' Bottom Right':' '}

show_rows = [row1,row2,row3]



def welcome():
    '''
    This is just to display at the start of the game so the user knows how to
    play it.

    Returns
    -------
    None.

    '''
    
    nl = '\n'
    print(f'''
    Welcome to tic tac toe!{nl}
This is a two human player game.Player X goes first.{nl}
When you see 'Enter Your Move:', {nl}type in the space you want to place your marker,{nl}using the key below as a reference.{nl}      
    ''')
    the_board_help()
    print(f'''{nl}
Have Fun!  
    ''')

def the_board_help():
    ''''
    Inputs: Each Row of the initial display board.
    Outputs: Displays the keys to the user so they know what to type to place their marks
    
    '''
    for key, value in show_row1.items():
        print(key, end='')
    print('\n------------------------------------------')
    for key, value in show_row2.items():
        print(key, end='')
    print('\n------------------------------------------')
    for key, value in show_row3.items():
        print(key, end='')





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
    '''
    Function asks the user for input for their move on the board. The function
    verifies that the input is a valid dict key and then verifies that
    there is not already an X or O value for that key

    Returns
    -------
    user_choice : This is the user input that corresponds to a position on
    the_board where the player wants to make their move

    '''
    #Checks to see if the input is a valid key
    selection = False
    counter = 0
    moves_counter = 0
    while selection == False:
        #this section checks for a valid dict key
        choice = input('Enter Your Move: ')
        user_choice = choice.title() #makes user input more forgiving
        for dict in rows:
            if user_choice in dict:
                #print('bingo') just for testing
                selection = True
                next = rows[counter]
                break
            else:
                counter +=1
            if counter > 2: #this block catches the final loop through the rows
                print('Please enter a valid Option')
                counter = 0
                break
        #start of the check for an open space
        if selection == True:
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
    '''
    This function adds an X or O to the board depending on the current player.

    Parameters
    ----------
    position : this is essentially user_choice and is set in the turn function.
    It passes the position the user chose in check_key and adds their X or O
    to the board.

    Returns
    -------
    None.

    '''
    if player == 'X':
        for row in rows:
            if position in row:
                row[position] = 'X'
    elif player == 'O':
        for row in rows:
            if position in row:
                row[position] = 'O'  


def swap_player(player):
    '''
    This alternates the placement of X and O between players

    Parameters
    ----------
    player : This is player at the end of the last turn.

    Returns
    -------
    player : This will be the player at the start of the next turn.

    '''    
    if player == 'X':
        player = 'O' 
        return player
    elif player == 'O':
        player = 'X'
        return player


def turn(player):
    '''
    This steps through a turn.
    1) User supplies input and is validated
    2) Input is passed and added to the board
    3) Board is shown to the user

    Parameters
    ----------
    player : Accepts the current player.

    Returns
    -------
    player : Returns the current player.

    '''
    position = check_key()
    add_move(position)
    the_board()
    return player


def endgame(): #takes player variable
    '''
    This checks the possible game win conditions in order
    1) 3 in a row horizontally
    2) 
    
    This doesn't loop through the dicts, due to the spacers in the rows.
    This could be cleaned up by changing the board print and removing the
    spacers from the rows.
    
    Returns
    -------
    game_over : Returns True to trigger the end of the game if True
    
    '''
    game_over = False
    nl ='\n'
    while game_over == False:
        #first check for horizontal
        if rows[0]['Top Left'] == player and rows[0]['Top Middle'] == player and rows[0]['Top Right'] == player:
            print(f'{nl}{nl}{player} wins!')
            game_over = True
        elif rows[1]['Mid Left'] == player and rows[1]['Mid Middle'] == player and rows[1]['Mid Right'] == player:
            print(f'{nl}{nl}{player} wins!')
            game_over = True
        elif rows[2]['Bottom Left'] == player and rows[2]['Bottom Middle'] == player and rows[2]['Bottom Right'] == player:
            print(f'{nl}{nl}{player} wins!')
            game_over = True    
        #starts check for vertical victory
        elif rows[0]['Top Left'] == player and rows[1]['Mid Left'] == player and rows[2]['Bottom Left'] == player:
            print(f'{nl}{nl}{player} wins!')
            game_over = True
        elif rows[0]['Top Middle'] == player and rows[1]['Mid Middle'] == player and rows[2]['Bottom Middle'] == player:
            print(f'{nl}{nl}{player} wins!')
            game_over = True
        elif rows[0]['Top Right'] == player and rows[1]['Mid Right'] == player and rows[2]['Bottom Right'] == player:
            print(f'{nl}{nl}{player} wins!')
            game_over = True
        #diagonal victories
        elif rows[0]['Top Left'] == player and rows[1]['Mid Middle'] == player and rows[2]['Bottom Right'] == player:
            print(f'{nl}{nl}{player} wins!')
            game_over = True
        elif rows[0]['Top Right'] == player and rows[1]['Mid Middle'] == player and rows[2]['Bottom Left'] == player:
            print(f'{nl}{nl}{player} wins!')
            game_over = True     
        else:
            #print('no') #for testing only
            break
    return game_over


#The Game itself    
welcome() #tells the players what's what
while game_over == False:
    #Have a player take a turn
    player = turn(player)
    #if the number of turns is >4 check for the wincon. Can't win before turn 4
    if turns < 4:
        turns +=1
        player = swap_player(player)
    else:
        the_end = endgame()
        if the_end == True:
            game_over = True
        elif the_end == False and turns < 9:
            turns +=1
            player = swap_player(player)
            if turns >= 9: #once the board is full and there is no win the game ends in a tie
                game_over = True
                print('Game is Tied')
