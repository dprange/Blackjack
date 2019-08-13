import sys
import random
import time

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

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
    def add_card(self, card):
        self.cards.append(card)
    def pop_card(self, i=-1):
        return str(self.cards.pop(i))
    def move_card(self, hand, num):
        for i in range(num):
            if deck.cards == []:
                self.build()
            newcard = self.pop_card()
            hand.add_card(newcard)
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
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

player_hand = Hand()
dealer_hand = Hand()
deck = Deck()
global info_i
info_i = 0


def update_info_gui(text):
    global info_i
    top.info_listbox.insert(info_i,text)
    info_i += 1

def update_player_gui():
    top.player_listbox.delete(0,100)
    top.player_hand_total_lbl.configure(text=player_hand.total())
    for i in range(len(player_hand.cards)):
        top.player_listbox.insert(i,player_hand.cards[i])

def update_dealer_gui(show):
    top.dealer_listbox.delete(0,100)
    if show == 1:
        top.dealer_hand_total_lbl.configure(text='-')
        top.dealer_listbox.insert(0,'Hidden')
        top.dealer_listbox.insert(1,dealer_hand.cards[1])
    if show == 2:
        top.dealer_hand_total_lbl.configure(text=dealer_hand.total())
        for i in range(len(dealer_hand.cards)):
            top.dealer_listbox.insert(i,dealer_hand.cards[i])

def deal_button_action():
    top.info_listbox.delete(0,100)
    info_i = 0
    update_info_gui('Dealer Deals a new hand.')
    player_hand.cards = []
    dealer_hand.cards = []
    deck.move_card(player_hand, 1)
    deck.move_card(dealer_hand, 1)
    deck.move_card(player_hand, 1)
    deck.move_card(dealer_hand, 1)
    update_player_gui()
    time.sleep(.3)
    update_dealer_gui(1)
    if player_hand.total() == 21:
        update_info_gui('BLACKJACK!!!')
    if dealer_hand.cards[1][0] == 'a':
        pass
        #print("Dealer is showing an Ace")
        #print("but we are not betting so it does not matter.")
    #does player have doubles to split.
    #double down - take one card and stay.
    sys.stdout.flush()

def hit_button_action():
    update_info_gui('---Player Hits---')
    deck.move_card(player_hand, 1)
    update_player_gui() 
    if player_hand.total() > 21:
        update_info_gui("BUST!")
    sys.stdout.flush()

def stand_button_action():
    while dealer_hand.total() < 17:
        update_info_gui("---Dealer Hits---")
        deck.move_card(dealer_hand, 1)
        update_dealer_gui(2)
        if dealer_hand.total() > 21:
            update_info_gui("Dealer BUST!")  
    update_dealer_gui(2)
    if (player_hand.total() > dealer_hand.total() or dealer_hand.total() > 21):
        update_info_gui("Player Wins!")
    elif player_hand.total() == dealer_hand.total():
        update_info_gui("Push!")
    else:
        update_info_gui("Dealer Wins!")
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    global top_level
    top_level.destroy()
    top_level = None

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root, top
    root = tk.Tk()
    top = Toplevel1 (root)
    init(root, top)
    root.mainloop()
    print(top)

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family gothic -size 15 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"
        top.geometry("352x346+2220+7")
        top.title("Blackjack")
        top.configure(highlightcolor="black")

        self.player_listbox = tk.Listbox(top)
        self.player_listbox.place(relx=0.057, rely=0.549, relheight=0.324
                , relwidth=0.352)
        self.player_listbox.configure(background="white")
        self.player_listbox.configure(font="TkFixedFont")
        self.player_listbox.configure(selectbackground="#c4c4c4")
        self.player_listbox.configure(width=124)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.028, rely=0.029, height=15, width=109)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(text='''Dealers Hand''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.028, rely=0.491, height=15, width=109)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(text='''Player Hand''')

        self.dealer_listbox = tk.Listbox(top)
        self.dealer_listbox.place(relx=0.057, rely=0.087, relheight=0.353
                , relwidth=0.352)
        self.dealer_listbox.configure(background="white")
        self.dealer_listbox.configure(font="TkFixedFont")
        self.dealer_listbox.configure(selectbackground="#c4c4c4")
        self.dealer_listbox.configure(width=124)

        self.info_listbox = tk.Listbox(top)
        self.info_listbox.place(relx=0.450, rely=0.087, relheight=0.353
                , relwidth=0.500)
        self.info_listbox.configure(background="white")
        self.info_listbox.configure(font="TkFixedFont")
        self.info_listbox.configure(selectbackground="#c4c4c4")
        self.info_listbox.configure(width=124)

        self.deal_button = tk.Button(top)
        self.deal_button.place(relx=0.057, rely=0.896, height=25, width=56)
        self.deal_button.configure(activebackground="#f9f9f9")
        self.deal_button.configure(command=deal_button_action)
        self.deal_button.configure(text='''Deal''')

        self.hit_button = tk.Button(top)
        self.hit_button.place(relx=0.199, rely=0.896, height=25, width=49)
        self.hit_button.configure(activebackground="#f9f9f9")
        self.hit_button.configure(command=hit_button_action)
        self.hit_button.configure(text='''Hit''')

        self.stand_button = tk.Button(top)
        self.stand_button.place(relx=0.313, rely=0.896, height=25, width=63)
        self.stand_button.configure(activebackground="#f9f9f9")
        self.stand_button.configure(command=stand_button_action)
        self.stand_button.configure(text='''Stand''')

        self.Button4 = tk.Button(top)
        self.Button4.place(relx=0.483, rely=0.896, height=25, width=63)
        self.Button4.configure(activebackground="#f9f9f9")
        self.Button4.configure(text='''Split''')

        self.Button5 = tk.Button(top)
        self.Button5.place(relx=0.653, rely=0.896, height=25, width=105)
        self.Button5.configure(activebackground="#f9f9f9")
        self.Button5.configure(text='''Double Down''')

        self.dealer_hand_total_lbl = tk.Label(top)
        self.dealer_hand_total_lbl.place(relx=0.313, rely=0.015, height=22
                , width=19)
        self.dealer_hand_total_lbl.configure(activebackground="#f9f9f9")
        self.dealer_hand_total_lbl.configure(font=font9)
        #self.dealer_hand_total_lbl.configure(text='''0''')

        self.player_hand_total_lbl = tk.Label(top)
        self.player_hand_total_lbl.place(relx=0.313, rely=0.477, height=22
                , width=20)
        self.player_hand_total_lbl.configure(activebackground="#f9f9f9")
        self.player_hand_total_lbl.configure(font=font9)
        self.player_hand_total_lbl.configure(text='''0''')

if __name__ == '__main__':
    vp_start_gui()