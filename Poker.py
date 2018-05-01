#  File: Poker.py

#  Description: To simulate a game of Poker known as Five-Card draw, using a 52-card deck

# Student Name: Annie L. Zhang

# Student UT EID: alz373

#  Partner's Name: Vaishnavi Kashyap

#  Partner's UT EID: vmk288

# Course Name: CS 313E

# Unique Number: 51340

# Date Created: 7 February 2018

# Date Last Modified: 8 February 2018

import random

class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('C', 'D', 'H', 'S')

  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12
    
    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  def __str__ (self):
    if (self.rank == 14):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str (self.rank)
    return rank + self.suit

  def __eq__ (self, other):
    return (self.rank == other.rank)

  def __ne__ (self, other):
    return (self.rank != other.rank)

  def __lt__ (self, other):
    return (self.rank < other.rank)

  def __le__ (self, other):
    return (self.rank <= other.rank)

  def __gt__ (self, other):
    return (self.rank > other.rank)

  def __ge__ (self, other):
    return (self.rank >= other.rank)

class Deck (object):
  def __init__ (self):
    self.deck = []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        card = Card (rank, suit)
        self.deck.append (card)

  def shuffle (self):
    random.shuffle (self.deck)

  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

class Poker (object):
  def __init__ (self, num_players):
    self.deck = Deck()
    self.deck.shuffle()
    self.players = []
    numcards_in_hand = 5

    for i in range (num_players):
      hand = []
      for j in range (numcards_in_hand):
        hand.append (self.deck.deal())
      self.players.append (hand)

  def play (self):
  # sort the hands of each player and print
    for i in range (len(self.players)):
      sortedHand = sorted (self.players[i], reverse = True)
      self.players[i] = sortedHand
      hand = ''
      for card in sortedHand:
        hand = hand + str (card) + ' '
      print ('Player ' + str (i + 1) + " : " + hand)
    

    print("")


  # determine the each type of hand and print
    points_hand = []  # create list to store points for each hand
    track_hand = []

  # determine winner and print
    for i in range(len(self.players)):
      if self.is_royal(self.players[i]) != 0:
        points_hand.append(self.is_royal(self.players[i]))
        print("Player " + str(i+1) + ": " + "Royal Flush")
       

      elif self.is_straight_flush(self.players[i]) != 0:
        points_hand.append(self.is_straight_flush(self.players[i]))
        print("Player " + str(i+1) + ": " + "Straight Flush")
      

      elif self.is_four_kind(self.players[i]) != 0:
        points_hand.append(self.is_four_kind(self.players[i]))
        print("Player " + str(i+1) + ": " + "Four of a Kind")

      elif self.is_full_house(self.players[i]) != 0:
        points_hand.append(self.is_full_house(self.players[i]))
        print("Player " + str(i+1) + ": " + "Full House")

      elif self.is_flush(self.players[i]) != 0:
        points_hand.append(self.is_flush(self.players[i]))
        print("Player " + str(i+1) + ": " + "Flush")

      elif self.is_straight(self.players[i]) != 0:
        points_hand.append(self.is_straight(self.players[i]))
        print("Player " + str(i+1) + ": " + "Straight")

      elif self.is_three_kind(self.players[i]) != 0 :
        points_hand.append(self.is_three_kind(self.players[i]))
        print("Player " + str(i+1) + ": " + "Three of a Kind")

      elif self.is_two_pair(self.players[i]) != 0:
        points_hand.append(self.is_two_pair(self.players[i]))
        print("Player " + str(i+1) + ": " + "Two Pair")
  
      elif self.is_one_pair(self.players[i]) != 0:
        points_hand.append(self.is_one_pair(self.players[i]))
        print("Player " + str(i+1) + ": " + "One Pair")
        

      elif self.is_high_card(self.players[i]) != 0:
        points_hand.append(self.is_high_card(self.players[i]))
        print("Player " + str(i+1) + ": " + "High Card")
        

# initializing winner variables and printing winner 
    m = max(points_hand)
    turn = 0
    win = 0
    winner1 = 0   
    winner2 = 0
        
    for i in range(len(points_hand)):
      turn = turn + 1

      if points_hand[i] == m:  
        win = win + 1
        winner2 = i
        if winner1 < winner2:
          winner1 = winner2
      if win > 1:
        print("Player", int(winner1) + 1, "ties.")
        print()
        Print("Player", int(winner2) + 1, "ties.")
        break
      elif (win == 1) and turn == len(points_hand):
        print("Player", int(winner1) + 1, "wins.")
        break


  # determine if a hand is a royal flush
  def is_royal (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return False

    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == 14 - i)
    
    if (same_suit and rank_order):
      c1 = hand[0].rank
      c2 = hand[1].rank
      c3 = hand[2].rank
      c4 = hand[3].rank
      c5 = hand[4].rank
      h = 10
      total_points = h * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5  
      return total_points
    else:
      return False 

  def is_straight_flush (self, hand):
    same_suit = True
    for i in range (len(hand)-1):
      same_suit = same_suit and (hand[i].suit == hand[i+1].suit)
    if (not same_suit):
      return False
            
    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank + 1 == hand[i+1].rank)
    
    if (same_suit and rank_order):
      c1 = hand[0].rank
      c2 = hand[1].rank
      c3 = hand[2].rank
      c4 = hand[3].rank
      c5 = hand[4].rank
      h = 9
      total_points = h * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5  
      return total_points
    else:
      return False 
        

  def is_four_kind (self, hand):
    same_rank = True
    count = 0
    quad = 0
    for i in range (len(hand)-1):
      if hand[i].rank == hand[i+1].rank:
        quad+=1
        t=hand[i].rank
      else:
        d =  hand[i].rank

    if quad == 4: 
      c1 = t
      c2 = t
      c3 = t
      c4 = t
      c5 = d
      h = 8
      total_points = h * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5  
      return total_points
    else: 
      return False


  def is_full_house (self, hand):
    triple = 0 
    dist = 0
    for i in range(len(hand) - 1):
      if hand[i].rank == hand[i+1].rank:
        triple = triple + 1
        t = hand[i].rank
      else:
        d = hand[i].rank
        dist = dist + 1
                
    if (triple == 3 and dist == 1):
      c1 = t
      c2 = t
      c3 = t
      c4 = d
      c5 = d
      h = 7
      total_points = h * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5  
      return total_points
    else: 
      return False

  def is_flush (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if same_suit == True:
      c1 = hand[0].rank
      c2 = hand[1].rank
      c3 = hand[2].rank
      c4 = hand[3].rank
      c5 = hand[4].rank
      h = 6
      total_points = h * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5  
      return total_points
    else: 
      return False

  def is_straight (self, hand):
    rank_order = True
    for i in range (len(hand) - 1):
      rank_order = rank_order and (hand[i].rank + 1 == hand[i+1].rank)
        
    if rank_order == True:
      c1 = hand[0].rank
      c2 = hand[1].rank
      c3 = hand[2].rank
      c4 = hand[3].rank
      c5 = hand[4].rank
      h = 5
      total_points = h * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5  
      return total_points
    else:
      return False

  def is_three_kind (self, hand):
    same_rank = True
    count = 0
    a4=0
    dist=0

    for i in range (len(hand)-1): 
      if (hand[i].rank == hand[i+1].rank):
        count+=1
        if count == 3:
          d = hand[i].rank
      else:
        count=0
        dist+=1
        a1=hand[i].rank
        if a4<a1:
          a4=a1

    if count == 3: 
      c1 = d
      c2 = d
      c3 = d
      c4 = a4
      c5 = a1
      h = 4
      total_points = h * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5  
      return total_points
    else: 
      return False      


  def is_two_pair (self, hand):
    a = 0
    a1 = 0
    a2 = 0
    double = 0
    for i in range(len(hand) - 1):
      if hand[i].rank == hand[i+1].rank:
        double = double + 1
        a1 = hand[i].rank
        if a2 <= a1:
          a2 = a1
    for i in range(len(hand)):
      if hand[i].rank != a1 and hand[i].rank != a2:
        a = hand[i].rank
        break
        
    if (double == 2 and a2 != a1):
      c1 = a2
      c2 = a2
      c3 = a1
      c4 = a1
      c5 = a
      h = 3
      total_points = h * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5  
      return total_points
    else: 
      return False


  # determine if a hand is one pair
  def is_one_pair (self, hand):
    a = 0
    a1 = 0
    a2 = 0
    a3 = 0
    for i in range (len(hand) - 1):

      if (hand[i].rank == hand[i + 1].rank):
        a = hand[i].rank
      else: 
        a1 = hand[i].rank
        if a2 <= a1: 
          a2 = a1
          if a3 <= a2: 
            a3 = a2

    if a != 0:
      c1 = a
      c2 = a
      c3 = a3
      c4 = a2
      c5 = a1
      h = 2
      total_points = h * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5  
      return total_points
    else:
      return False

  def is_high_card (self, hand):
    high_card = 0
    for i in range(len(hand)):
      if high_card <= hand[i].rank: 
        high_card = hand[i].rank
        
    c1 = hand[0].rank
    c2 = hand[1].rank
    c3 = hand[2].rank
    c4 = hand[3].rank
    c5 = hand[4].rank
    h = 1
    total_points = h * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5  
    return total_points

def main():
  # prompt user to enter the number of players
  num_players = int (input ('Enter number of players: '))
  while ((num_players < 2) or (num_players > 6)):
    num_players = int (input ('Enter number of players: '))

  # create the Poker object
  game = Poker (num_players)

  # play the game (poker)
  game.play()

main()
