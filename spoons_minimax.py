# What the numbers do (flip if p2's turn)
# 0: set (p1_left, p1_right, p2_left, p2_right) to (1, 1, 1, 1)
# 1: hit(p1_left, p2_left)
# 2: hit(p1_left, p2_right)
# 3: hit(p1_right, p2_left)
# 4: hit(p1_right, p2_right)
# 5: conjoin(p1_left, p1_right)
# 6: split(p1_left, p1_right)
#
import json
import spoons_input

def find_board_state(moves):
    [p1_left, p1_right, p2_left, p2_right] = [1, 1, 1, 1]
    for i in range(len(moves)):
        if (i == 0):
            continue
        if (i % 2 == 1):
            spoons_input.turn_computer(p1_left, p1_right, p2_left, p2_right, moves[i])
        else:
            spoons_input.turn_computer(p2_left, p2_right, p1_left, p1_right, moves[i])
    return [p1_left, p1_right, p2_left, p2_right]

def check_equality(board_state, turnx, boo):
    # has to be a permutation, including repeats
    # should return true if
    # (a, b, b, c) (a, b, b, d)
    sorted_bs = board_state
    sorted_bs.sort()
    sorted_tx = turnx
    sorted_tx.sort()
    if sorted_bs != sorted_tx:
        return 0
    
    if (boo):
        self = turnx[0:2]
        opp = turnx[2:4]
    else:
        self = turnx[2:4]
        opp = turnx[0:2]
    
    self_same = (board_state[0:2] == self) or (board_state[0] == self[1] and board_state[1] == self[0])
    opp_same = (board_state[2:4] == opp) or (board_state[2] == opp[1] and board_state[3] == opp[0])

    if (self_same and opp_same):
        return 1
    
    return 0

def boolTest(board_state, turn_num):
    boo = (turn_num % 2 == 0)
    if (boo):
        self = board_state[0:2]
        opp = board_state[2:4]
    else:
        self = board_state[2:4]
        opp = board_state[0:2]
    
    toBeReturned = []
    
    for i in range(4):
        if (self[int(i / 2)] != 0 and opp[i % 2] != 0):
            toBeReturned.append(i)

    if (sum(self) < 5):
        toBeReturned.append(5)
    if (sum(self) % 2 == 0 and self[0] != self[1]):
        toBeReturned.append(6)

    return toBeReturned






# returns a 1 if the board position is identical to a previous state (with reference to flipping users, flipped hands), else returns 0.
def cycleTest(board_state, moves):
    for i in range(len(moves) - 1):
        turnx = find_board_state([moves[0:i]])
        if (i % 2 == len(moves) % 2):
            q = check_equality(board_state, turnx, True)
        else:
            q = check_equality(board_state, turnx, False)
        if (q == 1):
            return 1
    return 0

            

def run_spoons(moves):
    board_state = find_board_state(moves)
    if(board_state[0] == 0 and board_state[1] == 0):
        # with open("spoons_minimax_info.json", "w") as write_file:
        #    json.dump(moves, write_file)
        #    json.dump(-1 "\\n", write_file)
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
        test_case[i] = run_spoons(moves + [arr[i]])
        if (test_case[i] == 1 and len(moves) % 2 == 1): # currently A's turn and has the win
            return 1
        if (test_case[i] == -1 and len(moves) % 2 == 0): # B's turn, has the win
            return -1
        if (len(test_case) % 2 == 1):
            return max(test_case)
        else:
            return min(test_case)
    return 7

with open("spoons_minimax_info.json", "w") as write_file:
    write_file.write(str(0))
    write_file.write("\n")
    write_file.write(str(0))

run_spoons([0, 1, 1, 1, 2, 3, 4])









    




        





