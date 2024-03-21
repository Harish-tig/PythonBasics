import random
# global declaration
suits = ("Heart","Diamond","Spade","Club")
ranks = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
value = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":11,"Queen":12,"King":13,"Ace":14}

# class card keeps note of card and its type and rank

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = value[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

# class deck holds whole deck and list in all card
# all card then gets shuffeld in shuffled function
# a = Card("Spade","Two")
# print(a.value)

class Deck():
    def __init__(self):
        self.all_card = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.all_card.append(card)

    def Shuffle(self):
        random.shuffle(self.all_card)

    def deal_one(self):
        return self.all_card.pop()

# test 1 passed.
# new_card = Deck()
# new_card.Shuffle()
# check_card = new_card.all_card[0]
# print(check_card)

# class Player should have capabilty to hold a current list of card
# player should be able to add or remove card for, thier hand i.e deck

class Player():
    def __init__(self,name):
        self.name=name
        self.all_card = []

    def remove_cards(self):
        return self.all_card.pop(0)

    def add_card(self,card):
        if type(card) == type([]):
            self.all_card.extend(card)
        else:
            self.all_card.append(card)

    def __str__(self):
        return "Player {a} has {b} cards".format(a=self.name,b=len(self.all_card))


## test 2 passed succesfully
# test = Player("harish")
# print(test)
# test.add_card(['a','a'])
# print(test)
# test.add_card("a")
# print(test)
# test.remove_cards()
# print(test)

#lets build some game logic...
#step 1 setting up the players

deck = Deck()
player_1 = Player("Player 1")
player_2 = Player("Player 2")
deck.Shuffle()

# distributing the cards
for x in range(26):
    player_1.add_card(deck.deal_one())
    player_2.add_card(deck.deal_one())

#testing loop -----> passed
# print(len(player_1.all_card))
# print(len(player_2.all_card))

# turning the game on
count = 0
game = True

while game:
    count += 1
    print(f"current round number is {count}")

    if len(player_1.all_card) == 0:
        print("Congrats! Player 2 Won the game!, Player 1 out cards")
        game = False
    elif len(player_2.all_card) == 0:
        print("Congrats! Player 1 Won the game!, Player 2 out of cards ")
        game = False
    else:
        print(player_1)
        print(player_2)
        player_1_card = []
        player_2_card = []
        player_1_card.append(player_1.remove_cards())
        player_2_card.append(player_2.remove_cards())
        # the above code is bit complicated because player_1_card is a list that is
        #   actually storing the object of cards and not card string "two of spade"
        #   so we can use .values to check out the values and compare them
        #   like below
        war = True
        while war:
            if player_1_card[-1].value > player_2_card[-1].value:
                player_1.add_card(player_2_card)
                player_1.add_card(player_1_card)
                war = False
                break

            elif player_2_card[-1].value > player_1_card[-1].value:
                player_2.add_card(player_2_card)
                player_2.add_card(player_1_card)
                war = False
                break
            else:
                print("WAR !!!")
                if len(player_1.all_card) < 5:
                    print("PLAYER 1 DOESNT HAVE ENOUGH CARD TO DECLARE A WAR! \nPLAYER 2 WINS THE GAME!!")
                    game = False
                    break
                elif len(player_2.all_card) < 5:
                    print("PLAYER 2 DOESNT HAVE ENOUGH CARD TO DECLARE A WAR! \nPLAYER 1 WINS THE GAME!!")
                    game = False
                    break
                else:
                    for x in range(5):
                        player_1_card.append(player_1.remove_cards())
                        player_2_card.append(player_2.remove_cards())
                        war = True
                        game = True
#completed
