'''
a blackjack  game 

a computer dealer
a human player

TO-DO: 
- ask about play again  
'''

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
          'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace': 11}

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

class Player():
    def __init__(self, name):

        self.name = name
        self.hand = []
    
    def __str__(self):
        return f'Player {self.name} has {len(self.hand)} cards.'
    
    def add_card_hand(self, new_card):
        self.hand.append(new_card)
        return True
    
    def check_chips(self):
        counter_cards_values = 0
        for card in self.hand:
            counter_cards_values += card.value
        return counter_cards_values
    
    def is_winner(self):
       
        if self.check_chips() == 21:
            return True
        return False
    
    def is_loser(self):
        if self.check_chips() > 21:
            return True
        return False

class Dealer(Player): #set dealer

    def __init__(self):
        self.name = 'Dealer'
        self.deck = Deck().all_cards
        self.hand =[]

    def __str__(self):
        return f'The Dealer has {len(self.hand)} cards.'

    def ask_for_bet(self):
        answer = input('Do you want a new card? Type Y for yes or any key for no: ')
        print()
        if "Y" == answer.upper():
            return True
        return False

    def get_new_card(self):
        return self.deck.pop()
    
def show_results(winner_obj, loser_obj):
    print(f'Congratulations {winner_obj.name}, YOU WIN!')
    print('Your cars were: ')
    [print(f'- {card}') for card in winner_obj.hand]
    print(f'Total sum was: {winner_obj.check_chips()}')
    
    print('----------------')
    
    print(f'{loser_obj.name} LOSE.')
    print('Your cars were: ')
    [print(f'- {card}') for card in loser_obj.hand]
    print(f'Total sum was: {loser_obj.check_chips()}')

dealer = Dealer()
player = Player("Andre")

i = 0
while i < 2:
    #add two card for each of them
    player.add_card_hand(dealer.get_new_card())
    dealer.add_card_hand(dealer.get_new_card())
    i += 1

print(f'Your cards are:')
[print(f'- {card}') for card in player.hand]
print()
print(f'The Dealer has {len(dealer.hand)} and one of them is {dealer.hand[-1]}')
print()

playing = True
endgame = False
while playing:
    
    if player.is_winner() or dealer.is_loser(): #check if player wins
        show_results(player, dealer)
        break
    
    elif player.is_loser() or dealer.is_winner(): #check if player lose
        show_results(dealer, player)
        break
    elif endgame: #if player denied pick more cards and dealer has at least 17 chips
        if dealer.check_chips() >= player.check_chips():
            show_results(dealer, player)
        else:
            show_results(player, dealer)
        break
        #TO-DO ask about play again
    else:
        if dealer.ask_for_bet():
            player.add_card_hand(dealer.get_new_card())
            print(f'{player.name}, your new card is: {player.hand[-1]}')
            print()
        else:
            if(dealer.check_chips() >= 17):
                dealer.add_card_hand(dealer.get_new_card())
            else:
                endgame=True
