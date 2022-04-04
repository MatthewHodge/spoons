# spoons
Code the game of spoons + make an algorithm to solve the game of spoons

WHAT IS SPOONS:
Spoons is a children's game (maybe) where the objective of the game is to overload both your opponent's hands with numbers.
On your turn, you may either:
- Split (creating two hands of equal value)
- Conjoin (adding the two hands' sums together)
- Hit (with either left hand or right hand, on opponent's left or right hand)
    This essentially adds your hand total to your opponent's hand total.  If you have 3 fingers on your left hand, and your opponent has 1 finger up on his right hand, if your left hand slaps his right hand, now your opponent has 1 + 3 (4) fingers up.

If you have 5 or more fingers up at any time, set that hand to 0.
    
Game ends when one player has both hands set to 0.

ROUGH OUTLINE:
2 players - Player 1 and Player 2
Player 1 goes first

BAREBONES:
Ask for input:
- 1: Split
- 2: Conjoin
- 3: LH hits LH
- 4: LH hits RH
- 5: RH hits LH
- 6: RH hits RH

PROJECT UPDATE 1:
I'm too lazy to read what I wrote but, here's the basic task now:
We're essentially about to run a minimax problem, gathering every feasible move state, terminating a branch if there exists a winning combination or if it's repeated (for example if there exists a state where one player has the exact same position as a prior move)
Then we append every tree ending to a .json file, blargh.


PROJECT UPDATE 2:
Okay so, the problem is I'm running into a slight overflow error,
by that I mean I'm calling one function at 