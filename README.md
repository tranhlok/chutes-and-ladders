# Chutes and Ladders 
Solving the Chutes and Ladders game using dynamic programming.
Rules of the game and the board is found here https://gathertogethergames.com/chutes-and-ladders
# The goal of this project is to solve a game. By solving a game, we mean to determine
1. the optimal strategy and
2. the ”score” you can expect to earn when playing optimally.
# Game descriptions
We will modify the game since the original version has no strategic decisions. The goal is to train an agent to play the modified game optimally. Chutes And Ladders is a childhood game in which the goal is to move your
token from Square 0 (off the bottom, left corner of the board) to Square 100. See
Figure 1 for an image of the game board. The first player to move their token
to Square 100 wins the game. Each move consists of spinning a ”spinner” which
has the numbers 1 through 6 written on it; the player moves their token ahead the
designated number of moves. If the player lands exactly on the bottom of a ladder
square (see Square 4 for example), they move immediately to the top of the ladder.
Conversely, if the player lands exactly on the top of a chute square (see Square 16
for example), the must move their token to the bottom of the chute. A player does
not need an exact spin to land on Square 100; any spin that reaches that square is
adequate for the final move (for example, a player may spin a 6 from Square 97
and win the game).
We will change the game slightly using dice instead of a spinner. As the game
is formulated, it is all luck based on the spin. Our game will introduce an element
of strategic choice. Consider that each player has four dice (specified below)1.
On each move, the player may select any one of the dice, roll that dice, and use
the result for their move. Because the dice have different numbers, players may
strategically choose a dice that has a higher probability of avoiding a chute or
reaching a ladder. The strategy is to learn which dice to play at each square on the board so as to
minimize the future number of steps. Because the game is stochastic, the ”future
number of steps” is measured as an expected value, an average future number of
steps. Notice that strategies and also expected steps-to-goal for one square are
dependent on other squares.
