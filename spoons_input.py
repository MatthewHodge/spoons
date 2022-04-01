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
