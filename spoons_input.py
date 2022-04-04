def hit_spoons(self, opp):
    opp1 = opp + self
    if(opp1 >= 5):
        opp1 = 0
    return opp1

def split_spoons(lh, rh):
    return [int((lh + rh) / 2), int((lh + rh) / 2)]

def conjoin_spoons(lh, rh):
    return lh + rh

def turn_computer(self_left, self_right, opp_left, opp_right, move):
    if (move == 1):
        opp_left = hit_spoons(self_left, opp_left)
    if (move == 2):
        opp_right = hit_spoons(self_left, opp_right)
    if (move == 3):
        opp_left = hit_spoons(self_right, opp_left)
    if (move == 4):
        opp_right = hit_spoons(self_right, opp_right)
    if (move == 5):
        self_left = conjoin_spoons(self_left, self_right)
        self_right = 0
    if (move == 6):
        [self_left, self_right] = split_spoons(self_left, self_right)
    return [self_left, self_right, opp_left, opp_right]

def find_board_state(moves):
    [p1_left, p1_right, p2_left, p2_right] = [1, 1, 1, 1]
    for i in range(len(moves)):
        if (i == 0):
            continue
        if (i % 2 == 1):
            [p1_left, p1_right, p2_left, p2_right] = turn_computer(p1_left, p1_right, p2_left, p2_right, moves[i])
        else:
            [p2_left, p2_right, p1_left, p1_right] = turn_computer(p2_left, p2_right, p1_left, p1_right, moves[i])
    return [p1_left, p1_right, p2_left, p2_right]