# TDD  Xitan Qiang & Huijing Huang
import unittest
from soloBlackJack import *
from cards import *

class TestBlackJack(unittest.TestCase):
##### Test Card #######
    def testCard(self):
        """ test card __init__ , get_rank(), get_suit() methods"""
        # test1
        cardObj1 = Card('A','d')
        self.assertEquals(1,cardObj1.get_rank())
        self.assertEquals('d',cardObj1.get_suit())
        # test2
        cardObj2 = Card('J','d')
        self.assertEquals(10,cardObj2.get_rank())
        # test3
        cardObj3 = Card(5,'d')
        self.assertEquals(5,cardObj3.get_rank())

    def testCardStr(self):
        """ test card str overload method"""
        cardObj = Card('A','d')
        self.assertEquals('Ad',str(cardObj))

##### Test Deck #######
    def testDeckStr(self):
        """test str overload method"""
        deckObj = Deck()
        tmpStr = 'As\n2s\n3s\n4s\n5s\n6s\n7s\n8s\n9s\n10s\nJs\nQs\nKs\n\
Ac\n2c\n3c\n4c\n5c\n6c\n7c\n8c\n9c\n10c\nJc\nQc\nKc\nAh\n\
2h\n3h\n4h\n5h\n6h\n7h\n8h\n9h\n10h\nJh\nQh\nKh\n\
Ad\n2d\n3d\n4d\n5d\n6d\n7d\n8d\n9d\n10d\nJd\nQd\nKd\n'
        self.assertEquals(tmpStr,str(deckObj))

    def testDeckInit(self):
        """ test Deck class __init__  and getter method"""
        # Test Deck getter and itialization
        cardObj = Card('5','s')
        deckObj = Deck()
        deck = deckObj.get_deck()
        self.assertEquals(str(cardObj), str(deck[4]))

    def testDeckDeal(self):
        """test Deck class deal() method"""
        deckObj = Deck()
        self.assertEquals('As',str(deckObj.deal()))
        self.assertEquals('2s',str(deckObj.deal()))
        
##### Test BlackJack #######
    def testErrorChecking(self):
        """ test BlackJack class errorChecking() method"""
        discardLs = [17,18,19,20]
        table = {'row1':[1,2,3,4,5],'row2':[6,7,'7s',9,10],'row3':[11,12,13],'row4':[14,15,16]}
        blackJackObj = BlackJack()
        ## Overload Constructor
        blackJackObj.overloadConstructor(table, discardLs)
        self.assertEquals(True,blackJackObj.errorChecking('10')) # empty pos
        self.assertEquals(False,blackJackObj.errorChecking('8')) # taken pos
        self.assertEquals(False,blackJackObj.errorChecking('A')) # invalid input
        self.assertEquals(False,blackJackObj.errorChecking('21')) # out of range

    def testUpdateTableAndDiscardLs(self):
        """ test updateTableAndDiscardLs() method"""
        ## Initialize
        blackJackObj = BlackJack()
        ## update table
        card1 = Card('5','h')
        blackJackObj.updateTableAndDiscardLs('12', card1)
        table = {'row1':[1,2,3,4,5],'row2':[6,7,8,9,10],'row3':[11,card1,13],'row4':[14,15,16]}
        self.assertEquals(table, blackJackObj.table)
        ## update discardLs
        card2 = Card('6','b')
        blackJackObj.updateTableAndDiscardLs('1', card2)
        table = {'row1':[card2,2,3,4,5],'row2':[6,7,8,9,10],'row3':[11,card1,13],'row4':[14,15,16]}
        self.assertEquals(table, blackJackObj.table)

    def testScoreGame(self):
        """test scoreGame() method"""
        blackJackObj = BlackJack()
        ## test1 Arvind instance
        row1 = [Card('K', 'd'), Card(7, 'h'), Card(2, 'd'), Card(6, 's'), Card('J', 'h')]
        row2 = [Card('J', 'c'), Card(9, 's'), Card('Q','h'), Card(4, 'c'), Card(10,'d')]
        row3 = [Card(10,'s'), Card(5, 's'), Card(6, 'c')]
        row4 = [Card(4, 's'), Card('K', 's'), Card(5, 'c')]
        table = {'row1': row1, 'row2': row2, 'row3': row3, 'row4': row4}
        blackJackObj.table = table
        self.assertEquals(28, blackJackObj.scoreGame())
        ## test2  with Blaok-Jack
        row1 = [Card('A', 'd'), Card(7, 'h'), Card(2, 'd'), Card(6, 's'), Card('A', 'h')]
        row2 = [Card('J', 'c'), Card(9, 's'), Card('Q','h'), Card(4, 'c'), Card('A','d')]
        row3 = [Card(10,'s'), Card(5, 's'), Card(6, 'c')]
        row4 = [Card(4, 's'), Card('K', 's'), Card(5, 'c')]
        table = {'row1': row1, 'row2': row2, 'row3': row3, 'row4': row4}
        blackJackObj.table = table
        self.assertEquals(31, blackJackObj.scoreGame())
        ## test3
        row1 = [Card(10, 'h'), Card('A', 'h'), Card(3, 'd'), Card(3, 'c'), Card(4, 'd')]
        row2 = [Card('A', 'd'), Card(5, 'h'), Card(4,'c'), Card(6, 'd'), Card(5,'d')]
        row3 = [Card(7,'d'), Card('J', 'h'), Card(2, 's')]
        row4 = [Card(6, 's'), Card(4, 'h'), Card(9, 's')]
        table = {'row1': row1, 'row2': row2, 'row3': row3, 'row4': row4}
        blackJackObj.table = table
        self.assertEquals(49, blackJackObj.scoreGame())
        ## test4
        row1 = [Card(10, 'c'), Card(2, 'h'), Card(6, 'c'), Card('J', 's'), Card('A', 'h')]
        row2 = [Card('A', 's'), Card(4, 'h'), Card('A','d'), Card(8, 's'), Card('Q','c')]
        row3 = [Card(6,'s'), Card(4, 's'), Card('Q', 'd')]
        row4 = [Card(8, 'd'), Card(10, 'd'), Card(3, 'd')]
        table = {'row1': row1, 'row2': row2, 'row3': row3, 'row4': row4}
        blackJackObj.table = table
        self.assertEquals(44, blackJackObj.scoreGame())
        ## test5
        row1 = [Card('J', 'd'), Card('A', 'h'), Card(3, 'h'), Card(2, 'h'), Card('Q', 'c')]
        row2 = [Card('Q', 'd'), Card(5, 's'), Card(2,'d'), Card(5, 'c'), Card(6,'d')]
        row3 = [Card(7,'c'), Card(7, 'd'), Card(6, 'h')]
        row4 = [Card(10, 'h'), Card('K', 'h'), Card('Q', 's')]
        table = {'row1': row1, 'row2': row2, 'row3': row3, 'row4': row4}
        blackJackObj.table = table
        self.assertEquals(11, blackJackObj.scoreGame())
unittest.main()
