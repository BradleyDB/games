# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 13:08:46 2020

@author: bradl
"""

import random

SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 
         'Ten', 'Jack', 'Queen', 'King', 'Ace')
VALUES = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 
          'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10,
          'Ace':11}


################CLASSES################

class Card:
    '''
    Creates a card with a suit and rank. The values are assigned
    via the VALUES dictionary.
    
    STR method returns the suit and rank of the card.
    
    '''
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = VALUES[rank]
        
        
    def __str__(self):
        return self.rank + " of " + self.suit
    
    
    def __int__(self):
        return self.value
    

class Deck():
    
    '''
    This creates a deck of Card class objects. Each Card will have a suit
    and rank.
    '''
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in SUITS:
            for rank in RANKS:
                #create the card object
                created_card = Card(suit, rank)
                
                self.all_cards.append(created_card)
                
    def shuffle(self):
        '''
        Changes the order of the items in the all_cards list)

        Returns
        -------
        None.

        '''
        random.shuffle(self.all_cards)

    def deal_one(self):
        '''
        Removes an element from the all_cards list, aka the Deck.

        Returns
        -------
        Returns a string

        '''
        return self.all_cards.pop()


class Account():
    
    def __init__(self, balance):
        
        self.balance = balance
        
    def __float__(self):
        
        return self.balance
    
    def __str__(self):
                
        return f"Account Balance: ${self.balance}"
    
    def deposit(self, new_amount):
        
        self.balance  += new_amount
        
        print(f"Winnings Deposited. Added ${new_amount} to your balance. Your New Balance is: ${self.balance}")
    
    def withdraw(self, take_out):
        
        if self.balance > take_out:
            
            self.balance -= take_out
            
            print(f"Bet of ${take_out} Accepted. Your New Balance is: ${self.balance}")
            
            return True
        
        else:
            
            print('Funds Unavailable!') #some way to make this trigger end of game?
            
            return False
                    
        
class Player(Account):
    '''
    This creates a player class allowing for multiple players to hold
    a 'hand' of cards. Inherets from 'account' base class.
    ''' 
    def __init__(self, name, balance):
        self.balance = balance
        self.name = name
        
        self.cards_in_hand = []
        
    def remove_one(self):
        '''
        This removes a card from the 'hand'

        Returns
        -------
        Returns STR

        '''
        return self.cards_in_hand.pop(0)
    
    def add_cards(self, new_cards):
        '''
        This adds one or more cards to the players 'hand'

        Parameters
        ----------
        new_cards : Type is STR

        Returns
        -------
        None.

        '''
        
        if type(new_cards) == type([]):
            #if there are multiple cards added
            self.cards_in_hand.extend(new_cards)
        else:
            #if a single card is added
            self.cards_in_hand.append(new_cards)
        
    def hand_value(self):
        '''
        This loops through the current player objects hand and provides the
        value of their cards.

        Returns
        -------
        total : Returns int type.

        '''
        total = 0
        for card in self.cards_in_hand:
            total += card.value
        return total
    
    def see_hand(self):
        
        print(f"{self.name}s Current Hand: ")
        for card in self.cards_in_hand:
            print (str(card), end = '\n')
        return '\nTotal Hand Value: ' + str(self.hand_value()) + '\n'    
    
    def __str__(self):
        
        return f"{self.see_hand()} \nRemaining Balance: ${self.balance}."
    

    def ace_choice(self): #need to figure out how to get this to interact with the aces in hand, not for everyone
        new_ace_value = 0
        answer = 'wrong'
        while answer == 'wrong':
            try:
                new_ace_value = int(input('Aces High or Low? Enter 1 or 11: '))
            except ValueError:
                print("Sorry, You need to enter a '1' or '11")
            else:
                if new_ace_value not in (1,11):
                    print('Really? You have to pick a "1" or "11"') 
                else:
                    answer = 'right'
                    break                                   
        return new_ace_value
            
    def make_bet(self):
        funds_available = False
        while funds_available == False:
            try:
                take_out = (int(input(f"How much would you like to bet? You available balance is ${self.balance}:  ")))
            except ValueError:
                    print("Sorry, You need to enter a number")
            else:
                if self.withdraw(take_out):
                    funds_available = True
                    return take_out
                    break
                else:
                    pass

    def nat_21(self):
        
        do_nothing = 'do nothing'
        
        if self.hand_value() == 21:
            print('Winner!')
            return True
        elif self.hand_value() > 21:
            print('You Busted! The Dealer Wins.')
            return False
        else:
            return do_nothing

        
class Dealer(Player):
    
    def __init__(self, name, balance):
        self.balance = balance
        self.name = name
        
        self.cards_in_hand = []
        
    def __str__(self):
        
        return f"{self.see_hand()} \nRemaining Balance: ${self.balance}."
    

    def dealer_opening_hand(self): #needs to be printed
                    
            return 'Dealers Opening Hand: \n' + str(self.cards_in_hand[0]) + ' and a [Hidden Card]' + '\n'


    def ace_choice(self): #need to figure out how to get this to interact with the aces in hand, not for everyone
        new_ace_value = 0
    
        if self.hand_value() >= 17 and self.hand_value() < 22:
            new_ace_value = 11
        else:
            new_ace_value = 1          
                
        return new_ace_value

#build dealer turn into method of dealer class


################Game Functions################

def replay():
    
    return input('Do you want to play another round? Enter Yes or No: ').strip().lower().startswith('y')

def hit_stay():
    
    return input('Do you want another card? Enter Yes or No: ').strip().lower().startswith('y')






#####TODO######

#way to check if a hand has an ace, and then run ace_choice
#have ace_choice update the ace value in the hand as needed
#can play up to X rounds before needing to re-start the deck?



####TESTING BLOC#####


###END TESTING BLOCK######

######GAME LOGIC######





###Game Logic
game = True
while game == True:
    ####GAME SET UP#######

    round_on = True
    choice = True
    dealers_turn = True
    my_turn = True

    game_deck = Deck()
    game_deck.shuffle()

    dealer_player = Dealer('Dealer', 1000000000)
    human_player = Player('Joe', 1000)

    while round_on: #this is the while loop for each round
        dealers_turn = True
        my_turn = True

        while my_turn:
            bet_amount = human_player.make_bet() #Player makes bet
            for x in range(2): #Initial Cards Dealt
                human_player.add_cards(game_deck.deal_one())
                dealer_player.add_cards(game_deck.deal_one())
            #show hands
            print(dealer_player.dealer_opening_hand())
            print(human_player.see_hand())
            if human_player.nat_21() == True: #checks if the player won on the draw
                human_player.deposit(bet_amount*2)    
                dealers_turn = False #so you don't end up with the dealer going
                break
            else: #if player doesn't win on the deal, they can choose to hit or stay
                while choice:
                    #ask if they want another card
                    #run ace check and ask if high or low
                    ask_player = hit_stay() #if true they want another card
                    if ask_player == True:
                        human_player.add_cards(game_deck.deal_one()) #deal one card   
                        print(human_player.see_hand()) #show new hand
                        #check for ace? and ask if high or low
                        win_check = human_player.nat_21()
                        if win_check == True:
                           human_player.deposit(bet_amount*2)
                           my_turn = False
                           dealers_turn = False
                           break
                        elif win_check == False:
                            #go to dealers turn
                            my_turn = False
                            dealers_turn = False
                            break
                        else: #starts loop over if they didn't win or bust but asked for at least one additional card
                            pass
                    else: #this else is if the player doesn't want another card
                        my_turn = False
                        break
                        
        while dealers_turn:
            print('you made it')
            print(dealer_player.see_hand())
            while dealer_player.hand_value() < 17:
                #they will take another card
                dealer_player.add_cards(game_deck.deal_one())
                print(dealer_player.see_hand())
            if dealer_player.hand_value() == 21:
                #dealer wins
                print('Dealer Wins with a 21\n')
            elif dealer_player.hand_value() > 21:
                #player wins
                print('Dealer Busted. You Win!\n')
                human_player.deposit(bet_amount*2)
            elif dealer_player.hand_value() > human_player.hand_value():
                #dealer wins
                print('Dealer Wins: Closer hand to 21\n')
            else:
                #player wins
                print('You were closer to 21. You win!\n')
                human_player.deposit(bet_amount*2)
            break
            
        play_more = replay()
        if play_more == True: #asks if the player wants to go again
             #removes the cards in players hands
            for card in human_player.cards_in_hand[:]:
                human_player.remove_one()
            for card in dealer_player.cards_in_hand[:]:
                dealer_player.remove_one()
            game_deck.shuffle()
            round_on = True
            my_turn = True
            dealers_turn = True
        elif play_more == False:
            game = False
            round_on = False
            break