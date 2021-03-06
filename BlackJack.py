from random import shuffle

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                card = Card(rank, suit)
                self.all_cards.append(card)

    def __str__(self):
        return f"{len(self.all_cards)} in Total."

    def draw_card(self):
        return self.all_cards.pop()

    def shuffle_cards(self):
        shuffle(self.all_cards)

class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.account = 500.0
        self.points = 0

    def __str__(self):
        return f"{self.name.title()} currently with: ${self.account}"

    def win_bet(self, bet):
        self.account += bet

    def lose_bet(self, bet):
        self.account -= bet
