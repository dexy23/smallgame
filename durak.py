# -*- coding: utf-8 -*-
import random
CLUBS = 1
DIAMONDS = 2
HEARTS = 3
SPADES = 4
suits = (CLUBS, DIAMONDS, HEARTS, SPADES)
SUITS_SYMBOLS = {
        CLUBS: "♣",
        DIAMONDS: "♦",
        HEARTS: "♥",
        SPADES: "♠",
        }
 
 
Jack = 11
Queen = 12
King = 13
Ace = 14
ranks = (6,7,8,9,10,Jack,Queen,King,Ace)
ranks_symbols = {
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: '10',
        Jack: 'J',
        Queen: 'Q',
        King: 'K',
        Ace: 'A',
        }
cards = []
cards = [r+s for r in ranks for s in suits]
 
 
class Card(object):
     
    def __init__(self, suit, rank, trump = None):
        self.suit = suit
        self.rank = rank
        self.trump = trump
 
    def create_card(self, suit, rank):
        return Card(suit, rank)
 
    def is_trump(self):
        return self.suit == self.trump
       
    def value(self):
        if self.is_trump():
            return self.rank + 12
        return self.rank
 
    def beats(self, other):
        if self.suit == other.suit:
            return self.value() > other.value()
        return self.is_trump()
     
    def is_ace(self):
        return False
     
    def __str__(self):
        return '%s%s' % (
                SUITS_SYMBOLS[self.suit],
                RANKS_SYMBOLS.get(self.rank, self.rank))
 
 
class Deck(object):
    def __init__(self):
        self.cards = cards
                
    def draw(self):
        return self.cards.pop()
 
    def shuffle(self):
        random.shuffle(self.cards)
 
    def add(self, card):
        self.cards.append(card)
 
    def is_empty(self):
        return not len(self.cards)
 
    def create_card(self, suit, rank):
        return Card(suit, rank, self.powersuit)
 
    def power_card(self, rank):
        return Card(self.trump, rank, self.trump)
 
    def normal_card(self, rank):
        for suit in suits:
            if suit != self.trump:
                break
        return Card(suit, rank, self.trump)
 
    def other_normal_card(self, other, rank):
        for suit in suits:
            if suit != self.trump and suit != other.suit:
                break
        return Card(suit, rank, self.trump)
 
 
class Hand(object):
    def __init__(self):
         
        self.cards = []
 
    def add_card(self, card):
        self.cards.append(card)
 
    def beats(self, hand):
        return self.value() > hand.value()
     
    def valid_moves(self, attack_card):
        def beats(card):
            return card.beats(attack_card)
        return filter(beats, self.cards)
 
    def __str__(self):
        if len(self.cards):
            return '%s' % ', '.join([str(x) for x in self.cards])
        else:
            return 'EMPTY'
         
class Game(object):
    def __init__(self, players=[]):
        self.players = players
        self.hands = {}
        self.started = False
        self.over = False
 
    def create_deck(self):
        return Deck()
 
    def create_hand(self):
        return Hand()
 
    def start(self):
        self.deck = self.create_deck()
        for player in self.players:
            self.hands[player] = self.create_hand()
            player.set_hand(self.create_hand())
        self.started = True
    
    def getplayorder(player1, player2, trump):
    """
    Returns a tuple of (attacker, defender). The first player to attack is the
    player with the lowest ranking trump card in their hand. Used at the very
    beginning of a game of Durak.
    """
        player1trumps = filter(lambda c: c.suit == trump, player1.hand)
        player2trumps = filter(lambda c: c.suit == trump, player2.hand)
         
        if len(player1trumps) == 0 and len(player2trumps) == 0:
            return player1, player2
        elif len(player1trumps) == 0:
            return player2, player1
        elif len(player2trumps) == 0:
            return player1, player2
        elif player1trump[0].rank < player2trump[0].rank:
            return player1, player2
        else:
                return player2, player1
 
 
    def is_over(self):
        return self.over
 
    def play(self):
        self.over = True
 
 
class Player(object):
    def print_msg(self, message):
        print ('*', message)
 
    def set_hand(self, hand):
        self.hand = hand
        self.print_msg('%s received hand: %s' % (self, hand))
 
    def add_card(self, card):
        self.hand.add_card(card)
        self.print_msg('%s: received card: %s' % (self, card))
 
    def print_status(self):
        self.print_msg('%s: value: %s, hand: %s' % (
            self, self.hand.value(), self.hand))
player1 = Player()
player2 = Player()
players = [player1, player2]
game = Game()
game.start()