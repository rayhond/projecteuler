#!/usr/bin/env python2
import pandas as pd
import numpy as np


def checkStraightFlush(cards):
    card_values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    sorted_cards = sorted([card_values[i[0]] for i in cards])
    flush = checkFlush(cards)
    straight = checkStraight(cards)
    if flush and straight:
        low_card = straight[1]
        return (8,low_card)
    if flush:
        return tuple(np.concatenate(([5], sorted_cards[::-1] )))
    if straight:
        return (4, straight[1])

def checkFlush(cards):
    for suit in cards:
        if suit[1] != cards[0][1]:
            return False
    return True

def checkStraight(cards):
    card_values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    sorted_cards = sorted([card_values[i[0]] for i in cards])
    for i in xrange(len(sorted_cards)-1):
        if sorted_cards[i+1]-sorted_cards[i] != 1:
            return False
    return True, sorted_cards[0]

def findPairs(cards):
    card_values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    card_numbers = sorted([card_values[i[0]] for i in cards])
    card_counts = []
    i = 0
    while i<5:
        count = card_numbers.count(card_numbers[i])
        card_counts.append((card_numbers[i],count))
        i = i+count
    card_counts = np.array(card_counts)

    max_hand = max(card_counts[:,1])
    if max_hand==4:
        #4 of a kind
        big_card = np.where(card_counts[:,1]==max_hand)[0]
        kicker = 1-big_card
        return (7, card_counts[big_card,0], card_counts[kicker,0] )
    
    if max_hand==3:
        big_card = np.where(card_counts[:,1]==max_hand)[0]
        #full house
        if np.where(card_counts[:,1]==2)[0]:
            return (6, card_counts[big_card][0][0], card_counts[1-big_card][0][0])
        #3 of a kind
        else:
            non_matches = np.where(card_counts[:,1]!=max_hand)[0]
            return (3, card_counts[big_card][0][0], card_counts[non_matches,0][1],card_counts[non_matches,0][0])

    if max_hand==2:
        #1 pair
        if len(np.where(card_counts[:,1]==2)[0])==1:
            non_matches = np.where(card_counts[:,1]!=max_hand)[0]
            return tuple(np.concatenate((np.array([1]), card_counts[np.where(card_counts[:,1]==max_hand)[0],0],card_counts[non_matches,0][::-1])))
        else:
            #2 pair
            return (2,card_counts[np.where(card_counts[:,1]==2)[0]][1,0] ,card_counts[np.where(card_counts[:,1]==2)[0]][0,0], card_counts[np.where(card_counts[:,1]!=2)[0]][0,0])
    #high card
    return tuple(np.concatenate(([0],card_counts[:,0][::-1])))
        

class Hand:
    def __init__(player_hand, cards, outcome=-1):
        player_hand.cards = cards


hands = pd.read_csv('p054_poker.txt', header=None, delim_whitespace=True).values
number_of_hands = hands.shape[0]

counter = 0

for i in xrange(number_of_hands):
    player1_hand = Hand(hands[i,:5])
    player2_hand = Hand(hands[i,5:])

    player1_hand.outcome = max(findPairs(player1_hand.cards), checkStraightFlush(player1_hand.cards) )
    player2_hand.outcome = max(findPairs(player2_hand.cards), checkStraightFlush(player2_hand.cards) )

    print i, player1_hand.outcome, player2_hand.outcome, player1_hand.cards, player2_hand.cards, player1_hand.outcome > player2_hand.outcome
    if player1_hand.outcome > player2_hand.outcome:
        counter = counter + 1

print counter
