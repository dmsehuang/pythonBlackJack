# Xitan Qiang & Huijing Huang
from cards import *
import re  # for regular expression on input string error checking

class BlackJack(object):
    """ This class is the main game class, deal with the logic of the game"""
    def __init__(self):
        """ Initialize the game"""
        # Initialize
        # initialize game
        self.discardLs = [17,18,19,20]
        self.table = {'row1':[1,2,3,4,5],'row2':[6,7,8,9,10],'row3':[11,12,13],'row4':[14,15,16]}

    ### This overload constructor is used for unittest only,
    ### since python does not support overloading constructor
    ### not used in the game...
    def overloadConstructor(self, table, discardLs):
        """This overload constructor is used for unittest only"""
        self.discardLs = discardLs
        self.table = table

    def displayGame(self):
        """ Display both current table and discard list"""
        # row1 & row2 longer, row3 & row4 shorter, proper indented below
        print 'current table:'
        for key in ['row1','row2']:
            rowLs = self.table[key]
            string = ''
            for ele in rowLs:
                tmpStr = str(ele) + '\t'
                string += tmpStr
            print string
        for key in ['row3','row4']:
            string = '\t'
            rowLs = self.table[key]
            for ele in rowLs:
                tmpStr = str(ele) + '\t'
                string += tmpStr
            print string       
        print 'discardList:'
        print self.discardLs[0],'\t',self.discardLs[1],'\n',self.discardLs[2],'\t',self.discardLs[3]

    def errorChecking(self, position):
        """ check for valid input(number, taken or not, range)"""
        # regex check input to be a valid number
        if not re.match("[0-9]+", position):
            print 'invalid input, please input a number [1-20]'
            return False
        if int(position) >= 1 and int(position) <= 20:
            # check position in table taken or not
            for subLs in self.table.values():  
                if int(position) in subLs:
                    return True
            # check position in discardLs taken or not
            if int(position) in self.discardLs:
                return True
            print 'position not empty, already taken, please input another position'
            return False
        else:
            print 'Input out of range!'
            return False
            
    def updateTableAndDiscardLs(self,position,card):
        """ Update new legal card into table or discard list """
        intPos = int(position)
        # update table
        for rowKey in self.table:
            valueLs = self.table[rowKey]
            if intPos in valueLs:
                index = valueLs.index(intPos)  # find index of intPos
                valueLs[index] = card
                return
        # update discard list
        index = self.discardLs.index(intPos)
        self.discardLs[index] = card
                    
    def checkGameComplete(self):
        """Check the termination of game"""
        for rowKey in self.table:
            for ele in self.table[rowKey]:
                if type(ele) == int:
                    return False  # means not complete
        return True

    def sumHandReturnPoints(self, valueLs): # card is the element in valueLs
        """ Calculate points except for two-card column"""
        #Ace is dealt with here, assume Ace to be 11 initially, decreasing by 10 per Ace if sum > 21
        rowSum = 0
        AceCount = 0
        for ele in valueLs:
            rank = ele.get_rank()
            if rank == 1:
                rank = 11
                AceCount += 1 # serve as flag
            rowSum += rank
        while(AceCount!=0):
            if rowSum > 21:
                rowSum -= 10
            AceCount -= 1
        points = self.countPoints(rowSum)
        return points

    def twoCardReturnPoints(self, valueLs):
        """ Calculate points for two-card column"""
        colSum = 0
        colSum += valueLs[0]
        colSum += valueLs[1]
        if valueLs[0] == 1 and valueLs[1] == 1:  # two Aces
            colSum = 12
        elif (valueLs[0] == 1 or valueLs[1] == 1): # one Ace
            colSum += 10
            # count actual points
        if colSum == 21:  # black jack 
            points = 10
        else:
            points = self.countPoints(colSum)
        return points
    
    def scoreGame(self):
        """ Parent function to calculate game points"""
        # create valueLs[card1,card2,...], pass it to sumHandReturnPoints(valueLs) or twoCardReturnPoints(valueLs)
        scoreLs = []
        ### Score of row
        for rowKey in self.table:
            valueLs = self.table[rowKey]
            points = self.sumHandReturnPoints(valueLs)
            scoreLs.append(points)

        ### Score of 4-card column
        for offset in range(0,3):  # 0,1,2
            tmpLs = []
            for rowKey in self.table:
                valueLs = self.table[rowKey]
                if len(valueLs) == 5:
                    iterStart = 1
                else:
                    iterStart = 0
                card = valueLs[iterStart+offset]
                tmpLs.append(card)
            points = self.sumHandReturnPoints(tmpLs)
            scoreLs.append(points)    

        ### Score of 2-card column
            #(1) 1st column
        valueLs1 = self.table['row1']
        valueLs2 = self.table['row2']
        tmpLs = []
        tmpLs.append(valueLs1[0].get_rank())
        tmpLs.append(valueLs2[0].get_rank())
        points = self.twoCardReturnPoints(tmpLs)
        scoreLs.append(points)
            #(2) 5th column
        valueLs3 = self.table['row1']
        valueLs4 = self.table['row2']
        tmpLs = []
        tmpLs.append(valueLs3[-1].get_rank())
        tmpLs.append(valueLs4[-1].get_rank())
        points = self.twoCardReturnPoints(tmpLs)
        scoreLs.append(points)        

        ### Add up scoreLs
        sumPoints = 0
        for points in scoreLs:
           sumPoints += points
        return sumPoints      

    def countPoints(self,sumation):
        """Scoring rule without Blackjack, which is taken care of in twoCardReturnPoints(valueLs)"""
        if sumation == 21:
            points = 7
        elif sumation == 20:
            points = 5
        elif sumation == 19:
            points = 4
        elif sumation == 18:
            points = 3
        elif sumation == 17:
            points = 2
        elif sumation <=16:
            points = 1
        else:
            points = 0
        return points
        
    def run(self):
        """Driver function for the whole game"""
        print "Welcome to the BlackJack game ......" # print help function if needed
        deckObj = Deck()
        deckObj.shuffle()
        while(not self.checkGameComplete()):
            self.displayGame()
            card = deckObj.deal()
            # ask user for move
            position = raw_input('Please input a number [1-16] for table, or [17-20] for discard list\n')
            isPass = self.errorChecking(position)
            while(not isPass):
                position = raw_input('Please input a number [1-16] for table, or [17-20] for discard list\n')
                isPass = self.errorChecking(position)
            # update table
            self.updateTableAndDiscardLs(position,card)
        ### Score Game
        self.displayGame()
        score = self.scoreGame()
        print 'Congratulations! Your final score is:'
        print score
        print 'Game is done... Thank you!'
               
def main():
    blackObj = BlackJack()
    blackObj.run()
    return

main()
