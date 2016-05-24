import math
import copy
simpler_board = {
    "E": ["e","w","e"],
    "F": ["w","b","b"],
    "G": ["w","e","e"],
    "H": ["s","s"],
    "I": ["s","s"],
    "J": ["s"],
    "Z": ["e"]
}
def board_visual(board_list):
    mboard_update(board_list)
    print("")
    print(board_list["E"], "   ", board_list["H"], "   ", board_list["J"])
    print(board_list["F"], "   ", board_list["I"])
    print(board_list["G"])
# Checks if a piece needs to be removed
# @Returns True if a piece needs to be removed
# @Returns False if otherwise
def mrcheck(letter, position, boardlist):
    if boardlist[letter][position] != "s" and boardlist[letter][position] != "e":
        if letter in ("E", "F", "G"):
            if boardlist["E"][position] == boardlist["F"][position] == boardlist["G"][position]:
                return True
            if boardlist[letter][0] == boardlist[letter][1] == boardlist[letter][2]:
                return True
        if letter == "E":
            if position == 0:
                if boardlist["E"][0] == boardlist["E"][1] == boardlist["F"][0] == boardlist["F"][1]:
                    return True
            if position == 2:
                if boardlist["E"][1] == boardlist["E"][2] == boardlist["F"][1] == boardlist["F"][2]:
                    return True
            if position == 1:
                if boardlist["E"][0] == boardlist["E"][1] == boardlist["F"][0] == boardlist["F"][1]:
                    return True
                if boardlist["E"][1] == boardlist["E"][2] == boardlist["F"][1] == boardlist["F"][2]:
                    return True
        if letter == "F":
            if position == 0:
                if boardlist["E"][0] == boardlist["E"][1] == boardlist["F"][0] == boardlist["F"][1]:
                    return True
                if boardlist["G"][0] == boardlist["G"][1] == boardlist["F"][0] == boardlist["F"][1]:
                    return True
            if position == 2:
                if boardlist["E"][1] == boardlist["E"][2] == boardlist["F"][1] == boardlist["F"][2]:
                    return True
                if boardlist["G"][1] == boardlist["G"][2] == boardlist["F"][1] == boardlist["F"][2]:
                    return True
            if position == 1:
                if boardlist["E"][0] == boardlist["E"][1] == boardlist["F"][0] == boardlist["F"][1]:
                    return True
                if boardlist["G"][0] == boardlist["G"][1] == boardlist["F"][0] == boardlist["F"][1]:
                    return True
                if boardlist["E"][1] == boardlist["E"][2] == boardlist["F"][1] == boardlist["F"][2]:
                    return True
                if boardlist["G"][1] == boardlist["G"][2] == boardlist["F"][1] == boardlist["F"][2]:
                    return True
        if letter == "G":
            if position == 0:
                if boardlist["G"][0] == boardlist["G"][1] == boardlist["F"][0] == boardlist["F"][1]:
                    return True
            if position == 2:
                if boardlist["G"][1] == boardlist["G"][2] == boardlist["F"][1] == boardlist["F"][2]:
                    return True
            if position == 1:
                if boardlist["G"][0] == boardlist["G"][1] == boardlist["F"][0] == boardlist["F"][1]:
                    return True
                if boardlist["G"][1] == boardlist["G"][2] == boardlist["F"][1] == boardlist["F"][2]:
                    return True
        if letter in ("H", "I"):
            if boardlist["H"][0] == boardlist["H"][1] == boardlist["I"][0] == boardlist["I"][1]:
                return True
        return False
    return False

def evaluate(boardlist, letter, position, prevscore):
    score = prevscore
    if letter == "J":
        score = math.inf
        return score
    if mrcheck(letter, position, boardlist):
        score += 10
    elif letter == "E":
        if position == 0:
            if boardlist["E"][0] == boardlist["E"][1]:
                score += 3
                if boardlist["E"][1] == boardlist["F"][1]:
                    score += 3
                    return score
            if boardlist["E"][0] == boardlist["F"][0]:
                score += 3
                if boardlist["F"][0] == boardlist["F"][1]:
                    score += 3
                    return score
        elif position == 1:
            score += 1
            if boardlist["E"][1] == boardlist["F"][1]:
                score += 3
                if boardlist["F"][1] == boardlist["F"][0]:
                    score += 3
                    return score
                if boardlist["F"][1] == boardlist["F"][2]:
                    score += 3
                    return score
            if boardlist["E"][1] == boardlist["E"][0]:
                score += 3
                if boardlist["E"][0] == boardlist["F"][1]:
                    score += 3
                    return score
            elif boardlist["E"][1] == boardlist["E"][2]:
                score += 3
                if boardlist["E"][2] == boardlist["F"][2]:
                    score += 3
                    return score
        elif position == 2:
            if boardlist["E"][2] == boardlist["E"][1]:
                score += 3
                if boardlist["E"][1] == boardlist["F"][1]:
                    score += 3
                    return score
            if boardlist["E"][2] == boardlist["F"][2]:
                score += 3
                if boardlist["F"][2] == boardlist["F"][1]:
                    score =+ 3
                    return score
    elif letter == "F":
        score += 1
        if position == 0:
            if boardlist["F"][0] == boardlist["F"][1]:
                score += 3
                if boardlist["F"][1] == boardlist["E"][1]:
                    score += 3
                    return score
                if boardlist["F"][1] == boardlist["G"][1]:
                    return score
            if boardlist["F"][0] == boardlist["E"][0]:
                score += 3
                if boardlist["E"][0] == boardlist["E"][1]:
                    score += 3
                    return score
            elif boardlist["F"][0] == boardlist["G"][0]:
                score += 3
                if boardlist["G"][0] == boardlist["G"][1]:
                    score += 3
                    return score
        elif position == 1:
            score += 1
            if boardlist["F"][1] == boardlist["F"][0]:
                score += 3
                if boardlist["F"][0] == boardlist["E"][0]:
                    score += 3
                    return score
                if boardlist["F"][0] == boardlist["G"][0]:
                    score += 3
                    return score
            elif boardlist["F"][1] == boardlist["F"][2]:
                score += 3
                if boardlist["F"][2] == boardlist["E"][2]:
                    score += 3
                    return score
                if boardlist["F"][2] == boardlist["G"][2]:
                    score += 3
                    return score
            if boardlist["F"][1] == boardlist["E"][1]:
                score += 3
                if boardlist["E"][1] == boardlist["E"][0]:
                    score += 3
                    return score
                if boardlist["E"][1] == boardlist["E"][2]:
                    score += 3
                    return score
            elif boardlist["F"][1] == boardlist["G"][1]:
                score += 3
                if boardlist["G"][1] == boardlist["G"][0]:
                    score += 3
                    return score
                if boardlist["G"][1] == boardlist["G"][2]:
                    score += 3
                    return score
        elif position == 2:
            if boardlist["F"][2] == boardlist["F"][1]:
                score += 3
                if boardlist["F"][1] == boardlist["E"][1]:
                    score += 3
                    return score
                if boardlist["F"][1] == boardlist["G"][1]:
                    score += 3
                    return score
            if boardlist["F"][2] == boardlist["E"][2]:
                score += 3
                if boardlist["E"][2] == boardlist["E"][1]:
                    score += 3
                    return score
            elif boardlist["F"][2] == boardlist["G"][2]:
                score += 3
                if boardlist["G"][2] == boardlist["G"][1]:
                    score += 3
                    return score
    elif letter == "G":
        if position == 0:
            if boardlist["G"][0] == boardlist["G"][1]:
                score += 3
                if boardlist["G"][1] == boardlist["F"][1]:
                    score += 3
                    return score
            if boardlist["G"][0] == boardlist["F"][0]:
                score += 3
                if boardlist["F"][0] == boardlist["F"][1]:
                    score += 3
                    return score
        elif position == 1:
            score += 1
            if boardlist["G"][1] == boardlist["F"][1]:
                score += 3
                if boardlist["F"][1] == boardlist["F"][0]:
                    score += 3
                    return score
                if boardlist["F"][1] == boardlist["F"][2]:
                    score += 3
                    return score
            if boardlist["G"][1] == boardlist["G"][0]:
                score += 3
                if boardlist["G"][0] == boardlist["F"][0]:
                    score += 3
                    return score
            elif boardlist["G"][1] == boardlist["G"][2]:
                score += 3
                if boardlist["G"][2] == boardlist["F"][2]:
                    score += 3
                    return score
        elif position == 2:
            if boardlist["G"][2] == boardlist["F"][2]:
                score += 3
                if boardlist["F"][2] == boardlist["F"][1]:
                    score += 3
                    return score
            if boardlist["G"][2] == boardlist["G"][1]:
                score += 3
                if boardlist["G"][1] == boardlist["F"][1]:
                    score += 3
                    return score
    elif letter in ("H", "I"):
        score += 1

    return score

def mboard_update(boardlist):
    # Unseals J[0]
    if boardlist["J"][0] == "s":
        boardlist["J"][0] = "e"
    for v, w in boardlist["H"], boardlist["I"]:
        if v == "e" or w == "e" or v == "s" or w == "s":
            boardlist["J"][0] = "s"
    # Unseals H[0]
    if boardlist["H"][0] == "s":
        boardlist["H"][0] = "e"
    for v, w in boardlist["E"][:2], boardlist["F"][:2]:
        if v == "e" or w == "e" or v == "s" or w == "s":
            boardlist["H"][0] = "s"
    # Unseals H[1]
    if boardlist["H"][1] == "s":
        boardlist["H"][1] = "e"
    for v, w in boardlist["E"][1:3], boardlist["F"][1:3]:
        if v == "e" or w == "e" or v == "s" or w == "s":
            boardlist["H"][1] = "s"
    # Unseals I[0]
    if boardlist["I"][0] == "s":
        boardlist["I"][0] = "e"
    for v, w in boardlist["F"][:2], boardlist["G"][:2]:
        if v == "e" or w == "e" or v == "s" or w == "s":
            boardlist["I"][0] = "s"
    # Unseals I[1]
    if boardlist["I"][1] == "s":
        boardlist["I"][1] = "e"
    for v, w in boardlist["F"][1:3], boardlist["G"][1:3]:
        if v == "e" or w == "e" or v == "s" or w == "s":
            boardlist["I"][1] = "s"
# Places piece on position
# @returns True if successful
# @returns False if otherwise
def mplace(letter, position, piece, boardlist):
    try:
        if boardlist[letter][position] == "e":
            boardlist[letter][position] = piece
            mboard_update(boardlist)
            return True
        else:
            print("Position is not empty.1")
            print(letter)
            print(position)
            print(boardlist[letter][position])
            return False
    except:
        print("Invalid input, please check your input is correct.111")
        return False

def moveList(boardlist):
    count = []
    for i, x in enumerate(boardlist["E"]):
        if x == "e":
            count.append(["E", i])
    for i, x in enumerate(boardlist["F"]):
        if x == "e":
            count.append(["F", i])
    for i, x in enumerate(boardlist["G"]):
        if x == "e":
            count.append(["G", i])
    for i, x in enumerate(boardlist["H"]):
        if x == "e":
            count.append(["H", i])
    for i, x in enumerate(boardlist["I"]):
        if x == "e":
            count.append(["I", i])
    for i, x in enumerate(boardlist["J"]):
        if x == "e":
            count.append(["J", i])
    return count


board_visual(simpler_board)
movelist = moveList(simpler_board)
print(movelist)
for i in movelist:
    simpboard = copy.deepcopy(simpler_board)
    mplace(i[0], i[1], "b", simpboard)
    print("Move: ", end="")
    print(i, end=" ")
    print("Score: ", end="")
    print(evaluate(simpboard, i[0], i[1], 0))
    board_visual(simpboard)