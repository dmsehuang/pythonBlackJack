# Xitan Qiang & Huijing Huang
import random  # needed for shuffling a Deck

class Card(object):
    """ Card class store the rank and suit of a typical card"""
    #the card has a suit - 's','c','h', 'd'
    # the card has a rank
    
    def __init__(self, r, s):
        """ constructor"""
        #implement
        #where r is the rank, s is suit
        self.r = r
        self.s = s
        #return NotImplementedError

    def __str__(self):
        """ overload str() method"""
        return str(self.r) + self.s

    def get_rank(self):
        """ get the rank of the card"""
        if(self.r == 'A'):
            return 1
        elif (self.r == 'J' or self.r == 'Q' or self.r == 'K'):
            return 10
        else:
            return int(self.r)
        
    def get_suit(self):
        """ get the suit of the card"""
        return self.s

class Deck(object):
    """Deck calss denotes a deck to play cards with"""
    
    def __init__(self):
        """Initialize deck as a list of all 52 cards:
           13 cards in each of 4 suits"""
        #correct the code below  --corrected
        self.__deck = []
        suits = ['s','c','h','d']
        ranks = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
        for suit in suits:
            for rank in ranks:
                self.__deck.append(Card(rank,suit))

    def shuffle(self):
        """Shuffle the deck"""
        random.shuffle(self.__deck)

    def get_deck(self):
        """return member __deck"""
        if len(self.__deck) != 52:
            print 'illegal deck with number of' + len(self.__deck)
        else:
            return self.__deck

    def deal(self):
        """ deal a card, return the top card in deck"""
        # get the last card in the deck
        # simulates a pile of cards and getting the top one
        topCard = self.__deck[0]
        self.__deck.remove(topCard)
        # formatting the deal card
        print '\t\t' + '======================'
        print '\t\t' + '|| Current Card is: ||'
        print '\t\t' + '||        ' + str(topCard) + '        ||'
        print '\t\t' + '======================'
        return topCard
    
    def __str__(self):
        """Represent the whole deck as a string for printing -- very useful during code development"""
       #the deck is a list of cards
       #this function just calls str(card) for each card in list
       # put a '\n' between them
        cardList = ''
        for card in self.__deck:
            cardList += str(card) + '\n'
        return cardList
            
