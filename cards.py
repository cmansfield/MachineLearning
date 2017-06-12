
suits = ['\u2665','\u2660','\u2666','\u2663']
suit_names = ['Hearts','Spades','Diamonds','Clubs']
value_names = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']


class Card:
    def __init__(self, suit, value):
        if(suit < 1 or suit > 4): raise ValueError('The suit must be a value 1 through 4')
        if(value < 1 or value > 13): raise ValueError('The card value must be value 1 through 13')
        self.__suit = suit
        self.__value = value

    @property
    def suit(self): return self.__suit

    @property
    def value(self): return self.__value

    def __eq__(self, other):
        return self.__value == other.value \
               and other.suit == self.__suit

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.__str__())

    def __str__(self):
        return '{} {} of {} {}'.format(
            suits[self.__suit - 1],
            value_names[self.__value - 1],
            suit_names[self.__suit - 1],
            suits[self.__suit - 1]
        )

class Hand:
    def __init__(self):
        self.__cards = set()

    @property
    def cards(self): return self.__cards

    def add_card(self, card):
        if not isinstance(card, Card): raise ValueError('Only Cards can be added to a hand')
        self.__cards.add(card)

    def reset_hand(self):
        self.__cards = set()

    def has_card(self,card):
        return card in self.__cards

    def stringify(self):
        str_simple = ''
        for card in self.__cards:
            str_simple += str(card.suit) + ',' + str(card.value) + ','
        return str_simple[:-1]

    def __str__(self):
        str_complex = ''
        for card in self.__cards:
            str_complex += card.__str__() + '\n'
        return str_complex