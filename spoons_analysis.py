import json
import depth_stat
import spoons_input
# generate a class that just has the 15 thing set in stone

def get_key(val):
    keyList = []
    for key, value in spockFish.items():
        if val == value:
            keyList.append(key)
    return keyList

def moveKeytoMoves(moveKey):
    moves = [] * len(moveKey)
    for i in len(moveKey):
        moves[i] = moveKey[i]
    return moves

f = open('spoons_minimax_info.json')

spockFish = json.load(f)

pot_ties = get_key(0)
act_ties = []
for i in pot_ties:
    if len(i) != depth_stat.get_depth():
        act_ties.append(i)

print(act_ties[17])


