# What the numbers do (flip if p2's turn)
# 0: set (p1_left, p1_right, p2_left, p2_right) to (1, 1, 1, 1)
# 1: hit(p1_left, p2_left)
# 2: hit(p1_left, p2_right)
# 3: hit(p1_right, p2_left)
# 4: hit(p1_right, p2_right)
# 5: conjoin(p1_left, p1_right)
# 6: split(p1_left, p1_right)
#
from xml.etree.ElementPath import find


def hit_spoons(self, opp):
    opp = opp + self
    if(opp >= 5):
        opp = 0

def split_spoons(lh, rh):
    lh = (lh + rh) / 2
    rh = lh

def conjoin_spoons(lh, rh):
    lh = lh + rh
    rh = 0



def turn_computer(self_left, self_right, opp_left, opp_right, move):
    if (move == 1):
        hit_spoons(self_left, opp_left)
    if (move == 2):
        hit_spoons(self_left, opp_right)
    if (move == 3):
        hit_spoons(self_right, opp_left)
    if (move == 4):
        hit_spoons(self_right, opp_right)
    if (move == 5):
        conjoin_spoons(self_left, self_right)
    if (move == 6):
        split_spoons(self_left, self_right)

def find_board_state(moves):
    [p1_left, p1_right, p2_left, p2_right] = [1, 1, 1, 1]
    for i in range(len(moves)):
        if (i == 0):
            continue
        if (i % 2 == 1):
            turn_computer(p1_left, p1_right, p2_left, p2_right, moves[i])
        else:
            turn_computer(p2_left, p2_right, p1_left, p1_right, moves[i])
    return [p1_left, p1_right, p2_left, p2_right]

def check_equality(board_state, turnx, boo):
    if (board_state[:] not in turnx):
        return 0
    if (turnx[:] not in board_state)





# returns a 1 if the board position is identical to a previous state (with reference to flipping users, flipped hands), else returns 0.
def cycleTest(board_state, moves):
    for i in range(len(moves) - 1):
        turnx = find_board_state([moves[0:i]])
        if (i % 2 == len(moves) % 2):
            q = check_equality(board_state, turnx, True)
        else:
            q = check_equality(board_state, turnx, False)
        if (q == 1)
            return 1
    return 0

            

def run_spoons(moves):
    board_state = find_board_state(moves)
    if(board_state[0] == 0 and board_state[1] == 0):
        #append json file moves + \n + -1 + \n
        return -1
    
    if (board_state[2] == 0 and board_state[3]):
        #append json file moves + \n + 1 + \n
        return 1
    
    c = cycleTest(moves, board_state)
    if (c == 1):
        #append json file moves + \n + 0 + \n
        return 0
    
    arr = boolTest(board_state, len(moves))
    test_case = []
    for i in range(len(arr)):
        test_case[i] = run_spoons(moves + arr[i])
        if (test_case[i] == 1 and len(moves) % 2 == 1): # currently A's turn and has the win
            return 1
        if (test_case[i] == -1 and len(moves) % 2 == 0): # B's turn, has the win
            return -1
        if (len(data) % 2 == 1):
            return max(test_case)
        else:
            return min(test_case)
    return 7










# TO DO: FIGURE OUT HOW TO DO POINTERS IN PYTHON?
# Turn 0: set to 1, 1, 1, 1
# turn 2k - 1: A turn
# turn 2k:     B Turn




    




        





