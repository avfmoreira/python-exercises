'''
a black jack simple game version

a computer dealer
a human player

TO-DO: 
- check result message
- check ace variation
- limit hit dealer
- ask about play again  
'''

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
#best_ace = {'1': 1, '11': 11}
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

class Dealer(Player): #create dealer

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
    
'''
## Game Play
To play a hand of Blackjack the following steps must be followed:



9. If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
10. If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
11. Determine the winner and adjust the Player's chips accordingly
12. Ask the Player if they'd like to play again
'''
def show_results(winner_obj, loser_obj):
    print(f'Congratulations {winner_obj.name}, YOU WIN!')
    print(f'Your cards sum was {winner_obj.check_chips()}')
    print(f'{loser_obj} cards sum was {loser_obj.check_chips()}')

dealer = Dealer()
player = Player("Andre")

i = 0
while i < 2:
    
    player.add_card_hand(dealer.get_new_card())
    dealer.add_card_hand(dealer.get_new_card())
    i += 1

playing = True
while playing:
    print(f'Your cards are:')
    [print(card) for card in player.hand]
    print()
    print(f'The Dealer has {len(dealer.hand)} and one of them is {dealer.hand[-1]}')
    print()
    
    if(player.is_winner()):
        show_results(player, dealer)
        break
        
    if(dealer.is_winner()):
        show_results(dealer, player)
        break
    
    if(player.is_loser()):
        show_results(dealer, player)
        break
      
    if(dealer.is_loser()):
        show_results(player, dealer)
        break
    
    
    if dealer.ask_for_bet():
        player.add_card_hand(dealer.get_new_card())
        dealer.add_card_hand(dealer.get_new_card())
    else:
        playing = False
