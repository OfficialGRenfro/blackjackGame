# Blackjack Game

# First step : Build text based blackjack game
import random
from time import sleep
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

# Generate our deck of N length
hd = deck
def getDeckSize(text):
    while True:
        try:
            value = int(input(text))
            if 1 <= value <= 8:
                return value
            else:
                print("I'm sorry, your input was outside the supported range.")
        except ValueError:
            print("Invalid data type, please enter an integer between 1 and 8.")
def doubleDeck(hitDeck, deckNum):
    hitDeck = []
    for i in range(deckNum):
        hitDeck.extend(deck)
    return hitDeck

# Draw from deck and remove the card from the deck
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
hiddenC = '2s'
#Seperate function for printing for ease simplicity
def printP():
    print(f"Your cards are: {player}\n", sep=' ')

def printD():
    print(f"Dealer's cards are: {dealer}\n", sep=' ')

#Function to handle the first deal of a game and reset the hands
def firstDeal(hd):
    global hiddenC
    hiddenC = (card(hd))
    player.append(card(hd))
    dealer.append(card(hd))
    player.append(card(hd))

    #print(f"{len(hd)} cards remain in the deck")
    print(f"Dealer: {dealer}", sep=' ')
    print(f"Player: {player}", sep=' ')

def sanitize():
    for x in range(len(dealer)):
        dealer.pop()
    for x in range(len(player)):
        player.pop()
    dealer.append('X')
    #print("Sanitize ran")

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

    if sum == 21 and len(hand) == 2:
        bj = 1
        print("\n\nBlackjack!")
    elif sum == 21:
        print("\n\n21!")
    elif sum > 21:
        bust = 1
        print("\n\nBust!")
    return [sum, bj, bust]

#Add functionality for betting
playerBalance = 500
bet = 2

def getBet():
    global bet
    print(f"Your balance is currently {playerBalance} and your bet is currently at {bet}")
    if bet > playerBalance:
        print(f"Bet is currently larger than balance, reducing bet to match balance")
        bet = playerBalance
        sleep(3)
    tempBet = ''
    while True:
        try:
            tempBet = int(input("If you would like to change your bet, please type the amount now, note it must be between 2 and 500 inclusive.\nIf you would not like to change your bet please type 1:" ))
            if tempBet == 1:
                print("Dealing Cards...")
                return 0
            elif tempBet >= 2 and tempBet <= 500 and tempBet <= playerBalance:
                bet = tempBet
                print(f"Bet changed to {bet}")
                print("Dealing Cards...")
                return 0
            elif tempBet > playerBalance:
                print(f"{tempBet} is larger than {playerBalance}, please enter a new bet")
            else:
                print(f"{tempBet} is outside of the bet range, please try again")
        except ValueError:
            print("Invalid data type, please enter an integer between 2 and 500.")

def betLoss(bet):
    global playerBalance
    playerBalance -= bet

def betWin(bet):
    global playerBalance
    playerBalance += bet
#Actual Game Logic

#Use a loop and startup text to begin game:
print("Welcome to BlackJack! Dealer hits on all 16's and stands on all 17's. Blackjack pays out 3/2.")
playGame = True
while playGame == True:
    dCount = getDeckSize("Please state the number of decks you like to use. Note there is a max of 8: ")
    hd = doubleDeck(hd, dCount)

    perHand = True
    while perHand == True:
        sanitize()
        getBet()
        sleep(1)
        dd = False
        firstDeal(hd)

        #Player's input
        pc = blackjack(player)
        val = input("Hit, Stand or Double Down?: ")
        while val != 'Stand' and val != 'stand' and val != 's' and pc[2]!= 1:
            if pc[1] == 1:
                bet = bet * 1.5
                break
            if val == 'Hit' or val == 'hit' or val == 'h':
                hitP(hd)
                pc = blackjack(player)
                printP()
                sleep(0.5)
            elif val == 'Double Down' or val == 'Double' or val == 'dd':
                if len(player) == 2 and playerBalance >= bet * 2:
                    dd = True
                    bet = bet + bet
                    hitP(hd)
                    pc = blackjack(player)
                    printP()
                    sleep(0.5)
                    break
                else:
                    print("You can only Double Down on your First Hit, or do not have the funds to cover your Double Down, you will receive a normal hit instead\n")
                    hitP(hd)
                    pc = blackjack(player)
                    printP()
                    sleep(0.5)
            else:
                print("Input not recognized")
            #Check if player busts, stands, or hits again
            if pc[0] < 21:
                val = input("Hit or Stand?: ")
            else:
                break

        #Exit loop once player stands
        if val == 'Stand' or val == 'stand' or val == 's':
            print("Player stands!\n")
        sleep(1.5)
        #Dealer's Turn
        if pc[2] != 1:
            print("Dealer's Turn!\n")
            dealer[0] = hiddenC
            dc = blackjack(dealer)
            printD()
            sleep(1.5)
            while dc[0] <= 16 and dc[1] != 1 and dc[2] != 1:
                print("Dealer draws a card.")
                hitD(hd)
                dc = blackjack(dealer)
                printD()
                sleep(1.5)
        else:
            dealer[0] = card(hd)
            dc = blackjack(dealer)
            print(f"Dealer shows {dealer}", sep=' ')
        sleep(1)
        #Calculate winner
        if pc[2] != 1:
            if dc[2] == 1:
                print(f"Player beats Dealer with a {pc[0]} against Dealer {dc[0]} (Bust!)")
                betWin(bet)
            elif pc[0] > dc [0]:
                print(f"Player beats Dealer with a {pc[0]} against Dealer {dc[0]}")
                betWin(bet)
            elif pc[0] == dc [0]:
                print(f"Player and Dealer chop with a {pc[0]}")
            else:
                print(f"Player loses to Dealer with a {pc[0]} against Dealer {dc[0]}")
                betLoss(bet)
        else:
            print(f"Player loses to Dealer with a {pc[0]} against Dealer {dc[0]}")
            betLoss(bet)
        sleep(1)
        if len(hd) <= 20: #Check if there aren't enough cards to keep the game going
            print(f"\n\nWarning! Only {len(hd)} cards remain. Reshuffle soon!")

        if playerBalance <= 0: #Kick Player out if they lose all their money
            print(f"\n\nOh no! You've lost all your money! Your balance is {playerBalance}")
            perHand = False
            playGame = False
            break
        if dd == True: #Reset Bet value after a double down or a blackjack
            bet = bet / 2
        if pc[1] == 1:
            bet = bet / 1.5
        runBack = input("\n\nWould you like to play again or get a new deck of cards? Type 1 for Play Again, 2 for a New Deck, and 3 to Exit the Application: ")
        if runBack == '1':
            #Blank Statement
            blank = 0
        elif runBack == '2':
            perHand = False
        elif runBack == '3':
            print("\n\nCome Again Soon!")
            perHand = False
            playGame = False
        else:
            print("\n\nInput not recognized, exiting application.")
            perHand = False
            playGame = False

        print("\n\n\n") #Some buffer room between hands to help with console readability

