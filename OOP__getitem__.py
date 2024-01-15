'''exercise from Luciano Ramalho: Fluent Python, chapter 1
https://github.com/fluentpython/example-code-2e/blob/master/01-data-model/data-model.ipynb'''

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards) # delegating len to a list object: self._cards

    def __getitem__(self, position):
        return self._cards[position] # delegating [] to a list object: self._cards

    # objects of this class are immutable, because we have not definded __setitem__

deck = FrenchDeck()


# has len(), because of __len__
print(len(deck))
# 52

# suscriptable AND iterable because of __getitem__, that provides `[]`
print(deck[8])
# Card(rank='10', suit='spades')

# --> If a class defines a method named __getitem__(), and x is an instance of
# --> this class, then x[i] is roughly equivalent to type(x).__getitem__(x, i).

# type is from the defined class (not list), since __init__ only returns None (results in error otherwise)
print(type(deck))
# <class '__main__.FrenchDeck'>

# we can use tools from standard library on it
import random
print(random.choice(deck))
# Card(rank='5', suit='hearts')

# get only aces (by accessing card.rank from the Card type)
ace_list = [card for card in deck if card.rank == 'A']
print(ace_list)
# [Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]

# get only aces (with slicing)
print(deck[12::13])
# [Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]

# "in" operator works, because class Deck is iterable
print(Card('K', 'spades') in deck)
# True

# sorting cards (unnecessarily costly)
sorted_cards = []
for i in reversed(deck.ranks):
    for j in ["spades", "hearts", "diamonds", "clubs"]:
        for card in deck:
            if card.rank == i and card.suit == j:
                sorted_cards.append(card)

print(sorted_cards)

# sorting cards as given by the book
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):  # we can only use "sorted", because we defined our class to be iterable
    print(card)                             # "sorted" builds a new sorted list from an iterable, while "sort" would sort a list in place
