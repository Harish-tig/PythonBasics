
**CARD GAME. <br>Let's brakedown the code**

<br>
Class Card -------->
a) The Card class is like a single playing card.
b) It has a suit, rank, and a special value.
c) When you print a card, it tells you its rank and suit, like "Ace of Hearts".
<br>
Class Deck --------->
a) The Deck class represents our deck of playing cards.
b) We make a full deck by combining different suits and ranks.
c) You can shuffle the deck to mix things up, and then deal cards one by one.
<br>
Class Player -------->
a) The Player class represents one of the players in the game.
b) They have a name and a set of cards they're holding.
c) Players can pick up or give away cards, depending on the game's rules.
<br>
Game Logic
We start by creating a deck and two players.
Then, we deal out the cards between them.
The game goes on in rounds where players compare their top cards.
If there's a tie, we enter a "war" situation, where more cards are drawn until someone wins.
The game keeps going until one player runs out of cards.
