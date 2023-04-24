import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
                'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card: #Set the suit and rank of each card
    def __init__(self, suit, rank):
        
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
class Deck: #Construct the deck of cards from Card
    def __init__(self):
        
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))
        self.suffle_cards()
    
    def suffle_cards(self):
        random.shuffle(self.all_cards)
    
class Player: #set the player
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def __str__(self):
        return f'Player {self.name} has {len(self.hand)} cards.'
    
    #add cards to hand 
    def add_cards(self, cards): 
        if(type(cards) == type([])):
            self.hand.extend(cards)
        else:
            self.hand.append(cards)
    #remove a card from the hand
    def remove_one(self):
        return self.hand.pop(0)
    
    #check if the player lose
    def is_loser(self, mininum_num_cards):
        if len(self.hand) <= mininum_num_cards:
            return True
        else:
            return False

#set players
player_1 = Player("Joao")
player_2 = Player("Maria")

#start and suffle the deck
deck = Deck()

#players receive your cards, alternaly.
player_1.add_cards(deck.all_cards[::2])
player_2.add_cards(deck.all_cards[1::2])

#start the round
game_on = True
counter = 0
while game_on:
    counter += 1
    print(f"Round {counter}")
    
    #check if one of them lose
    if player_1.is_loser(0):
        print(f"Sorry {player_1.name} your lose. \nCongratulation, {player_2.name}! You WIN!!!")
        game_on = False
        break
    if player_2.is_loser(0):
        print(f"Sorry {player_2.name} your lose. \nCongratulation, {player_1.name}! You WIN!!!")
        game_on = False
        break
    
    #otherwise the game still is on!
    
    #get a card from each player hand to and put on table
    player_1_cards_on_table = []
    player_1_cards_on_table.append(player_1.remove_one())
    player_2_cards_on_table = []
    player_2_cards_on_table.append(player_2.remove_one())
    
    at_war = True
    while at_war:
        
        #check if player 1 win the round
        if player_1_cards_on_table[-1].value > player_2_cards_on_table[-1].value:
            
            player_1.add_cards(player_1_cards_on_table)
            player_1.add_cards(player_2_cards_on_table)
            at_war = False
        
        #check if player 2 win the round          
        elif player_1_cards_on_table[-1].value < player_2_cards_on_table[-1].value:
            
            player_2.add_cards(player_1_cards_on_table)
            player_2.add_cards(player_2_cards_on_table)
            at_war = False
            
        else: # case the cards are of the same level
            
            print("WARRR!")
            
            if player_1.is_loser(5): #check if the player has at least 5 cards on your hand
                
                print(f" {player_1.name} unable to play war! Game Over at War")
                print(f" {player_2.name} Wins! {player_1.name} Loses!")
                game_on = False
                break

            elif player_2.is_loser(5):#check if the player has at least 5 cards on your hand
                
                print(f" {player_2.name} unable to play war! Game Over at War")
                print(f" {player_1.name} Wins! {player_2.name} Loses!")
                game_on = False
                break
            
            # Otherwise, we're still at war, so we'll add the next cards
            else:
                for num in range(5):
                    player_1_cards_on_table.append(player_1.remove_one())
                    player_2_cards_on_table.append(player_2.remove_one())