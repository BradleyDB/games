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
    '''
    This holds the player/dealers money. Allows for deposits, withrawls
    as well as the ability for a player to make a bet.
    
    '''
    
    
    def __init__(self, balance):
        
        self.balance = balance
        
    def __float__(self):
        
        return self.balance
    
    def __str__(self):
                
        return f"Account Balance: ${self.balance}"
    
    def deposit(self, new_amount):
        '''
        This allows for a deposit into the account.

        Parameters
        ----------
        new_amount : Must be int type.

        Returns
        -------
        None.

        '''
        
        self.balance += new_amount
        
        print(f"Winnings Deposited. Added ${new_amount} to your balance. Your New Balance is: ${self.balance}")
    
    def withdraw(self, take_out):
        '''
        Function withdraws funds from the account balance.

        Parameters
        ----------
        take_out : must be int type.

        Returns
        -------
        bool
            True if there were funds available and a withdrawl was made.

        '''
        
        if self.balance > take_out:
            
            self.balance -= take_out
            
            print(f"Bet of ${take_out} Accepted. Your New Balance is: ${self.balance}")
            
            return True
        
        else:
            
            print('Funds Unavailable!') #some way to make this trigger end of GAME?
            
            return False
                    
        
class Player(Account):
    '''
    This creates a player class allowing for multiple players to hold
    a 'hand' of cards. Inherets from 'account' base class.
    ''' 
    def __init__(self, name, balance):
        Account.__init__(self, balance)
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
        Controls for ace value logic of high and low aces.

        Returns
        -------
        total : Returns int type.

        '''
        num_aces = 0
        non_ace_total = 0
        
        for item in self.cards_in_hand:
            if item.rank == RANKS[-1]:
                num_aces += 1
            else:
                non_ace_total += item.value
        
        if num_aces > 0:
            if non_ace_total + 11 + (num_aces - 1)*1 <= 21:
                ace_value = 11 + (num_aces - 1)*1
            else:
                ace_value = num_aces*1
        else:
            ace_value = 0

        total = non_ace_total + ace_value
        
        return total
    
    def see_hand(self):
        '''
        Goes through the cards in a players hand and returns the card
        name, suit and total value.

        Returns
        -------
        STR

        '''
        
        
        print(f"{self.name}s Current Hand: ")
        for items in self.cards_in_hand:
            print(str(items),end ='\n')
        return '\nTotal Hand Value: ' + str(self.hand_value()) + '\n'    
    
    def __str__(self):
        '''
        Looks at the players hand and balance.

        Returns
        -------
        str
            Hand and balance.

        '''
        
        return f"{self.see_hand()} \nRemaining Balance: ${self.balance}."

            
    def make_bet(self):
        '''
        This takes a user input asking what their bet should be and tells them
        their current balance. Passed to the withdraw method if an int is
        entered.

        Returns
        -------
        take_out : int.

        '''
        
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
                else:
                    pass

    def nat_21(self):
        '''
        This checks if the hand value is a 21 or bust.

        Returns
        -------
        Returns Boolean or in a rare case a string, which is not passed to any
        arguments.

        '''
        
        
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
    '''
    Dealer class inherits from player class. This allows for slightly 
    different methods to account for modified dealer behavior.
    
    '''
    
    
    def __init__(self, name, balance):
        Player.__init__(self, name, balance)
        self.balance = balance
        self.name = name
        
        self.cards_in_hand = []
        
    def __str__(self):
        '''
        Current players hand (suit and rank) and account balance.

        Returns
        -------
        str
            
        '''
        return f"{self.see_hand()} \nRemaining Balance: ${self.balance}."
    

    def dealer_opening_hand(self): #needs to be printed
        '''
        Returns the dealers opening hand with one card hidden
        '''         

           
        return '\nDealers Opening Hand: \n' + str(self.cards_in_hand[0]) + ' and a [Hidden Card]' + '\n'






################GAME Functions################

def replay():
    '''
    Asks if the player would like to play again.
    Returns
    -------
    TYPE
        Boolean.

    '''
    
    return input('Do you want to play another round? Enter Yes or No: ').strip().lower().startswith('y')

def hit_stay():
    '''
    Asks if the player would like another card.
    Returns
    -------
    TYPE
        Boolean.

    '''
    
    
    return input('Do you want another card? Enter Yes or No: ').strip().lower().startswith('y')




######GAME LOGIC######





###GAME Logic
GAME = True
while GAME == True:
    ####GAME SET UP#######

    ROUND_ON = True
    CHOICE = True
    DEALERS_TURN = True
    MY_TURN = True

    GAME_DECK = Deck()
    GAME_DECK.shuffle()

    DEALER_PLAYER = Dealer('Dealer', 1000000000)
    HUMAN_PLAYER = Player('Joe', 1000)

    while ROUND_ON: #this is the while loop for each round
        DEALERS_TURN = True
        MY_TURN = True

        while MY_TURN:
            BET_AMOUNT = HUMAN_PLAYER.make_bet() #Player makes bet
            for x in range(2): #Initial Cards Dealt
                HUMAN_PLAYER.add_cards(GAME_DECK.deal_one())
                DEALER_PLAYER.add_cards(GAME_DECK.deal_one())
            #show hands
            print(DEALER_PLAYER.dealer_opening_hand())
            print(HUMAN_PLAYER.see_hand())
            if HUMAN_PLAYER.nat_21() == True: #checks if the player won on the draw
                HUMAN_PLAYER.deposit(BET_AMOUNT*2)    
                DEALERS_TURN = False #so you don't end up with the dealer going
                break
            else: #if player doesn't win on the deal, they can choose to hit or stay
                while CHOICE:
                    #ask if they want another card
                    #run ace check and ask if high or low
                    ASK_PLAYER = hit_stay() #if true they want another card
                    if ASK_PLAYER == True:
                        HUMAN_PLAYER.add_cards(GAME_DECK.deal_one()) #deal one card   
                        print(HUMAN_PLAYER.see_hand()) #show new hand
                        #check for ace? and ask if high or low
                        WIN_CHECK = HUMAN_PLAYER.nat_21()
                        if WIN_CHECK == True:
                            HUMAN_PLAYER.deposit(BET_AMOUNT*2)
                            MY_TURN = False
                            DEALERS_TURN = False
                            break
                        elif WIN_CHECK == False:
                            #go to dealers turn
                            MY_TURN = False
                            DEALERS_TURN = False
                            break
                        else: #starts loop over if they didn't win or bust but asked for at least one additional card
                            pass
                    else: #this else is if the player doesn't want another card
                        MY_TURN = False
                        break
                        
        while DEALERS_TURN:
            print('you made it')
            print(DEALER_PLAYER.see_hand())
            while DEALER_PLAYER.hand_value() < 17:
                #they will take another card
                DEALER_PLAYER.add_cards(GAME_DECK.deal_one())
                print(DEALER_PLAYER.see_hand())
            if DEALER_PLAYER.hand_value() == 21:
                #dealer wins
                print('Dealer Wins with a 21\n')
            elif DEALER_PLAYER.hand_value() > 21:
                #player wins
                print('Dealer Busted. You Win!\n')
                HUMAN_PLAYER.deposit(BET_AMOUNT*2)
            elif DEALER_PLAYER.hand_value() > HUMAN_PLAYER.hand_value():
                #dealer wins
                print('Dealer Wins: Closer hand to 21\n')
            else:
                #player wins
                print('You were closer to 21. You win!\n')
                HUMAN_PLAYER.deposit(BET_AMOUNT*2)
            break
            
        PLAY_MORE = replay()
        if PLAY_MORE == True: #asks if the player wants to go again
             #removes the cards in players hands
            for card in HUMAN_PLAYER.cards_in_hand[:]:
                HUMAN_PLAYER.remove_one()
            for card in DEALER_PLAYER.cards_in_hand[:]:
                DEALER_PLAYER.remove_one()
            GAME_DECK = Deck()
            GAME_DECK.shuffle()
            ROUND_ON = True
            MY_TURN = True
            DEALERS_TURN = True
        elif PLAY_MORE == False:
            GAME = False
            ROUND_ON = False
            break
