# Blackjack Game

# First step : Build text based blackjack game
import random

# Build Deck Array
# s = spades, d = diamonds, c = clubs, h = hearts
deck = [
    'As', 'Ad', 'Ac', 'Ah', '2s', '2d', '2c', '2h',
    '3s', '3d', '3c', '3h', '4s', '4d', '4c', '4h',
    '5s', '5d', '5c', '5h', '6s', '6d', '6c', '6h',
    '7s', '7d', '7c', '7h', '8s', '8d', '8c', '8h',
    '9s', '9d', '9c', '9h', '10s', '10d', '10c', '10h',
    'Js', 'Jd', 'Jc', 'Jh', 'Qs', 'Qd', 'Qc', 'Qh',
    'Ks', 'Kd', 'Kc', 'Kh'
]

# Draw from deck and remove the card from the deck
hd = deck
def card(hit_deck):
    if not hit_deck:
        return None
    index = random.randint(0, len(hit_deck) - 1)
    card = hit_deck.pop(index)
    return card

def hitP(hit_deck):
    new_card = card(hit_deck)
    player.append(new_card)

def hitD(hit_deck):
    new_card = card(hit_deck)
    dealer.append(new_card)

#Use arrays to represent the player and the dealer's hands, player bust will be tracked in a later array
dealer = ['X']
player = []
bustD = 0

#Seperate function for printing for ease simplicity
def printP():
    print(f"Your cards are: {player}", sep=' ')

def printD():
    print(f"Dealer's cards are: {dealer}", sep=' ')

#Function to handle the first deal of a game
def firstDeal(hd):
    new_card = card(hd)
    player.append(new_card)

    new_card = card(hd)
    dealer.append(new_card)

    new_card = card(hd)
    player.append(new_card)

    print(f"Dealer: {dealer}", sep=' ')
    print(f"Player: {player}", sep=' ')

#Determine the value of a hand
def blackjack(hand):
    valueMap = {
        'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
        '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10
    }

    def value(cd):
        return valueMap[cd[:-1]]

    sum = 0
    aces = 0
    bj = 0
    bust = 0

    for c in hand:
        i = value(c)
        sum += i
        if i == 11:
            aces += 1

    while sum > 21 and aces > 0:
        sum -= 10
        aces -= 1

    #Use a Dictionary to Define the Result to prevent extra print statements

    if sum == 21 and len(hand) == 2:
        bj = 1
        print("Blackjack!")
    elif sum == 21:
        print("21!")
    elif sum > 21:
        bust = 1
        print("Bust! You lose!")
    return [sum, bj, bust]
#Actual Game Logic
firstDeal(hd)

#Player's input
pc = blackjack(player)
val = input("Hit or Stand?: ")
while val != 'Stand' and val != 'stand' and val != 's' and pc[2]!= 1:
    if val == 'Hit' or val == 'hit' or val == 'h':
        hitP(hd)
        pc = blackjack(player)
        printP()
    else:
        print("Input not recognized")
    #Check if player busts, stands, or hits again
    if pc[0] <= 20:
        val = input("Hit or Stand?: ")
    else:
        break

#Exit loop once player stands
if val == 'Stand' or val == 'stand' or val == 's':
    print("Player stands!")

#Dealer's Turn
if pc[2] != 1:
    print("Dealer's Turn!")
    dealer[0] = card(hd)
    dc = blackjack(dealer)
    printD()
    while dc[0] <= 16 and dc[1] != 1 and dc[2] != 1:
        print("Dealer draws a card.")
        hitD(hd)
        dc = blackjack(dealer)
        printD()
else:
    dealer[0] = card(hd)
    dc = blackjack(dealer)
    print(f"Dealer shows {dealer}", sep=' ')

#Calculate winner
if pc[2] != 1:
    if dc[2] == 1:
        print(f"Player beats Dealer with a {pc[0]} against Dealer {dc[0]} (Bust!)")
    elif pc[0] > dc [0]:
        print(f"Player beats Dealer with a {pc[0]} against Dealer {dc[0]}")
    elif pc[0] == dc [0]:
        print(f"Player and Dealer chop with a {pc[0]}")
    else:
        print(f"Player loses to Dealer with a {pc[0]} against Dealer {dc[0]}")
else:
    print(f"Player loses to Dealer with a {pc[0]} against Dealer {dc[0]}")

