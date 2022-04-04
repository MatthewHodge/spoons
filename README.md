# spoons
Spoons - A Minimax Problem
By Eric Conor Lutts

Hello future employers!
The following is meant to be proof that yes, I can indeed code in Python.  I could probably reproduce this series of programs in any of the coding languages I'm familiar with (those being MATLAB, C++, and Java).
It also intends to show my tentative knowledge of Game Theory / Machine Learning by using decision trees and a Minimax algorithm.

The following project took ~10 hours with:
- 2 hours dedicated to planning (coding via paper)
- 3 hours dedicated to coding the initial product
- 5 hours to bug-testing + actually getting the thing to output what I wanted

This document is split into three parts:
- What is Spoons (Lines 20 - 40)
- How I coded it (Lines 41 - 64)
- Running an Algorithm over it / Saving the Minimax results (Lines 65 - 100)


1.) What is Spoons?

Spoons is a modified version of the game 'Chopsticks' (Wikipedia Link: https://en.wikipedia.org/wiki/Chopsticks_(hand_game)).  The rules of which (from Wikipedia) are as follows:
    - A hand is live if it has at least one finger, and this is indicated by raising at least one finger. If a hand has zero fingers, the hand is dead, and this is indicated by raising zero fingers (i.e. a closed fist).
    - If any hand of any player reaches exactly five fingers, then the hand is dead.
    - Each player begins with one finger raised on each hand. After the first player turns proceed clockwise.
    - On a player's turn, they must either attack or split. There are two types of splits, transfers and divisions.
    - To attack, a player uses one of their live hands to strike an opponent's live hand. The number of fingers on the opponent's struck hand will increase by the number of fingers on the hand used to strike.
    - To transfer, a player strikes their own two hands together, and transfers raised fingers from one hand to the other as desired. However, a player cannot transfer fingers to make a hand have more than 4 fingers.
    - If a player has a dead hand, the player can divide the fingers between the other hand and the dead hand by transferring fingers from the other hand to the dead hand.
    - A player with two dead hands is eliminated from the game.
    - A player wins once all opponents are eliminated.

The main differences are as follows:
    - The terms 'attack', 'transfer', and 'division' are referred to as 'hit', 'split', and 'conjoin'
    - Hands are declared dead if the hand is at or exceeds five, rather than needing to be exactly five.
    - Splits can only divide evenly (if a player has four fingers up in total, then a split divides it into two fingers per hand.  This makes dividing when there is only 1, 3, 5, or 7 fingers up impossible)
    - For the purposes of code simplicity, conjoins trend toward the left hand (a hand of 2, 1 will become 3, 0)

If I were to redo this project (spoons2 presumably), I would aim to include the original ruleset.  It would presumably also require me to learn machine learning, as the amount of options increases from my initial 6 to an over-double 14 (though only 5 are available at any given board state).

2.) How I Coded It
This can largely be seen in spoons_input.py.
One would input the series of moves that had taken place on the board thus far as numerical values between 0 and 6, each corresponding to a specific action:

(also for purposes of explaining we are assuming that this is player 1's turn)

0: Initial Board State              [p1_lh, p1_rh, p2_lh, p2_rh] = [1, 1, 1, 1]
1: Left Hand attacks Left Hand:     p2_lh += p1_lh
2: Left Hand attacks Right Hand:    p2_rh += p1_lh
3: Right Hand attacks Left Hand:    p2_lh += p1_rh
4: Right Hand attacks Right Hand:   p2_rh += p1_rh
5: Conjoin                          [p1_lh, p1_rh] = [p1_lh + p1_rh, 0]
6: Split                            [p1_lh, p1_rh] = [int((p1_lh + p1_rh) / 2), int((p1_lh + p1_rh) / 2)]

In terms of files:
find_board_state reads in the moves that have been taken up until this point.  It then passes each move (as well as who's turn it is) into:
    turn_computer, which then determines which of the seven moves is occurring, and calls the relevant function:
        hit_spoons: performs the attack action, checks to see if the hand is >= 5, returns opp's new hand value
        conjoin_spoons: performs a conjoin, returns pX_lh + pX_rh
        split_spoons: returns int((p1_lh + p1_rh) / 2)
    turn_computer then sets these to the relevent values given who's turn it is, returns [p1_lh, p1_rh, p2_lh, p2_rh]
find_board_state updates and repeats until all moves are calculated, returns the current board state.


3.) Putting an Algorithm on top of that

For reference, look at: spoons_minimax.py

In brief, the objective was to test every single option possible to create an algorithm that will play the best spoons ever conceived.  It starts by running depth_stat.getdepth() moves from the initial state (set to 20 for the purposes of this project, but could easily be expanded), until that depth is reached, one player wins, or a cycle occurs.

We define a cycle as any time where the board is an arbitrary permutation of a previous state, or in terms of acting player vs. non-acting player (meaning who's turn it is):
(relevant functions: cycleTest, check_equality)
- If both the acting player and non-acting player have the same fingers up in each hand, isomorphic to left-right.
For example, if it is player 1's turn at present, and the board state looks like:
p1_lh = 1
p1_rh = 2
p2_lh = 3
p2_rh = 4

This would be considered equivalent to, a prior state where it was player 2's turn, and the board state was:
p1_lh = 4
p1_rh = 3
p2_lh = 2
p2_rh = 1

Despite none of those values being directly equivalent, player 1 now has the same options as player 2 had, there is no point in continuing this loop

This would return a value of 0 from run_spoons(moves, depth)

run_spoons is the main recursive function, comprised of the following:
- Check to see if one of the two players has been eliminated, a cycle has occurred, or turn limit has been reached
    - if so, record moves and endresult to a dictionary
    - return endresult
- If not, figure out which moves [1, 2, 3, 4, 5, 6] are possible, with respect to identical moves
    - if acting player's hands are equivalent, then only test attacks done with the left hand (ignore cases 3 and 4)
    - Similarly, if the non-acting player's hands are equivalent, then only test attacks done to the left hand (ignore cases 2 and 4)
- Then run run_spoons but with the parameters run_spoons(moves + [one of the potential moves])
    - returning 1 or -1 if player 1 can make a move that guarantees them the win, or player 2 can make a move that guarantees them the win, respectively (player 1's turn, one of the test cases returns a 1, vice versa)
    - else return the maximum value of all possible moves if it is player 1's turn, or return the minimum value of all possible moves if it is player 2's turn.

Then, once complete, a dictionary containing all possible move endings is then created and outputted to
spoons_minimax_info.json
