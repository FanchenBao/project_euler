#! /usr/bin/env python3

import logging
logging.basicConfig(filename = 'debugLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

from time import time
s = time()

'''
Replace T, J, Q, K, A with ':', ';', '<', '=', '>', whose ascii code follows '9'. Order each hand, and then check for ranking.
If two hands have the same rank, based on the specific rank, check for other criteria.
'''

class Hands:
    def __init__(self, p1, p2):
        ''' stores the hand for player1 and player2 '''
        self.player1 = p1 # a list of strings, each representing a card. e.g ['8C', 'TS', 'KC', '9H', '4S']
        self.player2 = p2
        self.rankCountP1 = self.checkRepeatedRank(self.player1)
        self.rankCountP2 = self.checkRepeatedRank(self.player2)

    def checkRepeatedRank(self, cards):
        ''' report the number of repeats for each rank, return a sorted dict based on value as a list of tuples'''
        rankRepeats = {}
        tempCards = cards + ['@@']
        count = 0
        for i in range(5):
            if tempCards[i + 1][0] == tempCards[i][0]:
                count += 1
            else:
                rankRepeats[tempCards[i][0]] = count + 1
                count = 0
        return sorted(rankRepeats.items(), key=lambda x:x[1])
   
    def findWinner(self):
        ''' return true when player 1 wins, otherwise false'''
        rankP1, P1Value1, P1Value2, P1Value3 = self.findRank(self.player1, self.rankCountP1)
        rankP2, P2Value1, P2Value2, P2Value3 = self.findRank(self.player2, self.rankCountP2)
        if rankP1 > rankP2:
            return True
        elif rankP1 == rankP2: # royal flush impossible for equal ranking, because that would be a tie 
            if rankP1 in {0, 3, 4, 5, 6, 7, 8} and P1Value1 > P2Value1: # cover all situations except two and one pair
                return True
            elif rankP1 == 2: # two pairs
                # compare bigPair first
                if P1Value1 > P2Value1:
                    return True
                elif P1Value1 < P2Value1:
                    return False
                else: # bigPair equal
                    # compare smallPair
                    if P1Value2 > P2Value2:
                        return True
                    elif P1Value2 < P2Value2:
                        return False
                    else: # smallPair equal
                        # compare nonPair
                        if P1Value3 > P2Value3:
                            return True
                        else:
                            return False
            elif rankP1 == 1: # one pair
                # compare pair
                if P1Value1 > P2Value1:
                    return True
                elif P1Value1 < P2Value1:
                    return False
                else: # Pair equal
                    # compare maxRank
                    if P1Value2 > P2Value2:
                        return True
                    else:
                        return False
            else:
                return False
        else:
            return False

    def findRank(self, cards, rankCount):
        ''' find the rank order of given cards. Return 4 values'''
        if self.hasRoyalFlush(cards):
            return 9, False, False, False
        
        hasSF, maxRank = self.hasStraightFlush(cards)
        if hasSF:   return 8, maxRank, False, False

        has4, repeat = self.hasFourOfAKind(cards, rankCount)
        if has4:    return 7, repeat, False, False

        hasFH, repeat3 = self.hasFullHouse(cards, rankCount)
        if hasSF:   return 6, repeat3, False, False

        hasF, maxRank = self.hasFlush(cards)
        if hasF:    return 5, maxRank, False, False
        
        hasS, maxRank = self.hasStraight(cards)
        if hasS:    return 4, maxRank, False, False

        has3, repeat = self.hasThreeOfAKind(cards, rankCount)
        if has3:    return 3, repeat, False, False

        has2P, bigPair, smallPair, nonPair = self.hasTwoPairs(cards, rankCount)
        if has2P:   return 2, bigPair, smallPair, nonPair

        has1P, pair, maxRank = self.hasOnePair(cards, rankCount)
        if has1P:   return 1, pair, maxRank, False

        # high card sitation. No ranking, return 0 as rank and the maxRank
        return 0, cards[-1][0], False, False

    def hasRoyalFlush(self, cards):
        ''' return true when the cards contain royal flush, otherwise false'''
        if self.hasStraightFlush(cards)[0] and cards[0][0] == ':': return True
        else:   return False

    def hasStraightFlush(self, cards):
        ''' return true and the largest card value when the cards contain straight flush, otherwise false'''
        hasStraight, maxRank = self.hasStraight(cards)
        if hasStraight and self.hasFlush(cards)[0]:
            return True, maxRank
        else:   return False, False

    def hasFourOfAKind(self, cards, rankCount):
        ''' return true and the repeated card value when the cards contain four of a kind, otherwise false'''
        if rankCount[-1][1] == 4:
            return True, rankCount[-1][0]
        else:   return False, False

    def hasFullHouse(self, cards, rankCount):
        ''' return true and the three repeated card value when the cards contain full house, otherwise false'''
        if rankCount[-1][1] == 3 and rankCount[-2][1] == 2:
            return True, rankCount[1][0]
        else:   return False, False

    def hasFlush(self, cards):
        ''' return true and the largest ranked card value when the cards contain flush, otherwise false'''
        stdSuit = cards[0][1]
        for card in cards[1:]:
            if card[1] != stdSuit:
                return False, False
        return True, cards[-1][0]

    def hasStraight(self, cards):
        ''' return true and the largest ranked card value when the cards contain straight, otherwise false'''
        if cards[0][0] == '2' and cards[-1][0] == '>': # special situation where the hand can be A2345
            for i in range(3):
                if ord(cards[i + 1][0]) - ord(cards[i][0]) != 1:
                    return False, False
            return True, '5'
        else:
            for i in range(4):
                if ord(cards[i + 1][0]) - ord(cards[i][0]) != 1:
                    return False, False
            return True, cards[-1][0]

    def hasThreeOfAKind(self, cards, rankCount):
        ''' return true and the repeated card value when the cards contain three of a kind, otherwise false'''
        if rankCount[-1][1] == 3:
            return True, rankCount[-1][0]
        else:   return False, False

    def hasTwoPairs(self, cards, rankCount):
        ''' return true, the large paired card value, the small paired card value, and the non-paired card value when the cards contain two pairs, otherwise false'''
        if rankCount[-1][1] == 2 and rankCount[-2][1] == 2:
            if rankCount[-1][0] > rankCount[-2][0]:
                bigPair = rankCount[-1][0]
                smallPair = rankCount[-2][0]
            else:
                bigPair = rankCount[-2][0]
                smallPair = rankCount[-1][0]
            return True, bigPair, smallPair, rankCount[0][0]
        else:   return False, False, False, False

    def hasOnePair(self, cards, rankCount):
        ''' return true, the paired card value, the largest rank among non-paired values value when the cards contain one pair, otherwise false'''
        if rankCount[-1][1] == 2 and rankCount[-2][1] != 2:
            if cards[-1][0] != rankCount[-1][0]: # the paired value is NOT the highest among the cards
                highRank = cards[-1][0]
            else:
                highRank = cards[-3][0]
            return True, rankCount[-1][0], highRank
        else:   return False, False, False



# driver
with open("p054_poker.txt") as file_obj:
    contents = file_obj.readlines()

allHands = []
# generate player1 and 2 in each play in the class Hands, store all Hands in a list allHands.
for content in contents:
    player1 = sorted([card.replace('T',':').replace('J',';').replace('Q','<').replace('K','=').replace('A','>') for card in content[:14].split(' ')])
    player2 = sorted([card.replace('T',':').replace('J',';').replace('Q','<').replace('K','=').replace('A','>') for card in content[15:29].split(' ')])
    allHands.append(Hands(player1, player2))

count = 0 # record times player 1 wins
for hand in allHands:
    if hand.findWinner():
        count += 1

print(count)


# runtime = 0.04 s



print("\nTime: {}".format(time() - s))

logging.debug('End of program.\n\n\n')
