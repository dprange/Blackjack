import random
import time
class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return '%s of %s' % (self.value, self.suit)
class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()
    def build(self):
        suits = ["spade","club","heart","diamond"]
        faces = [2,3,4,5,6,7,8,9,10,"jack","queen","king","ace"]
        for suit in suits:
            for face in faces:
                card=(Card(face, suit))
                self.cards.append(card)
        self.shuffle()
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    def add_card(self, card):
        self.cards.append(card)
    def pop_card(self, i=-1):
        return str(self.cards.pop(i))
    def move_card(self, hand, num):
        for i in range(num):
            if deck.cards == []:
                self.build()
            hand.add_card(self.pop_card())
    def shuffle(self):
        random.shuffle(self.cards)
class Hand(Deck):
    def __init__(self, label=''):
        self.label = label
        self.cards = []
    def total(self):
        rank_values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,'9':9, '1':10, 'j':10, 'q':10, 'k':10, 'a':11}
        hand_total = 0
        ace_counter = 0
        for i in range(len(self.cards)):
            cardvalue = self.cards[i][0]
            hand_total += rank_values[cardvalue]
            if cardvalue == 'a':
                ace_counter += 1
            if (ace_counter > 0 and hand_total > 21):
                hand_total -= 10
                ace_counter -= 1
        return hand_total
def display_command_bar():
    print ("Type: (d)eal | (h)it | (s)tand and press enter")
        # for loop for all the hands. (split)
deck = Deck()
display_command_bar()
while(True):
    i = input()
    if i == "d":
        print("Dealer Deals a new hand.")
        player_hand = Hand()
        dealer_hand = Hand()
        deck.move_card(player_hand, 1)
        deck.move_card(dealer_hand, 1)
        deck.move_card(player_hand, 1)
        deck.move_card(dealer_hand, 1)
        print('-Player has.', player_hand.total())
        print(player_hand)
        time.sleep(.3)
        print("-Dealer shows.")
        print(dealer_hand.cards[1])
        if player_hand.total == 21:
            print("BLACKJACK!!!")
            display_command_bar()
        if dealer_hand.cards[1][0] == 'a':
            print("Dealer is showing an Ace")
            print("but we are not betting so it does not matter.")
        #does player have doubles to split.
        #double down - take one card and stay.
    if i == "h":
        print('---Player Hits---')
        deck.move_card(player_hand, 1)
        print(player_hand) 
        print('-Player Has.', player_hand.total())
        if player_hand.total() > 21:
            print("BUST!")
            display_command_bar()
    if i == 's':
        print('-Dealer Has.', dealer_hand.total())
        while dealer_hand.total() < 17:
            print('---Dealer Hits---')
            deck.move_card(dealer_hand, 1)
            print('-Dealer Has.', dealer_hand.total())
            if dealer_hand.total() > 21:
                print("Dealer BUST!")
                print("Player Wins!")
                display_command_bar()
        print(dealer_hand)
        print("scores Player:",player_hand.total())
        print("scores Dealer:",dealer_hand.total())
        if (player_hand.total() > dealer_hand.total() or dealer_hand.total() > 21):
            print("Player Wins!")
        elif player_hand.total() == dealer_hand.total():
            print("Push!")
        else:
            print("Dealer Wins!")
        display_command_bar()


