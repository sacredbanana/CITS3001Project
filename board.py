# Board level: 0
def board_level0():
    print("Level: 0")
    for i in A:
        print("|",end="")
        print(i, end="")
    print("|")
    for i in B:
        print("|",end="")
        print(i, end="")
    print("|")
    for i in C:
        print("|",end="")
        print(i, end="")
    print("|")
    for i in D:
        print("|",end="")
        print(i, end="")
    print("|\n")

# Board level: 1
def board_level1():
    print("Level: 1")
    for i in E:
        print("|",end="")
        print(i, end="")
    print("|")
    for i in F:
        print("|",end="")
        print(i, end="")
    print("|")
    for i in G:
        print("|",end="")
        print(i, end="")
    print("|\n")

# Board level: 2
def board_level2():
    print("Level: 2")
    for i in H:
        print("|",end="")
        print(i, end="")
    print("|")
    for i in I:
        print("|",end="")
        print(i, end="")
    print("|\n")

# Board level: 3
def board_level3():
    print("Level: 3")
    for i in J:
        print("|",end="")
        print(i, end="")
    print("|\n")

def board_visual():
    #prints out the board visually
    board_level0()
    board_level1()
    board_level2()
    board_level3()
    print("------------------------------------")

def placeA(position, piece):
    if A[position] == "e":
        A[position] = piece
    else:
        print("position not empty.")
    board_visual()

def placeB(position, piece):
    if B[position] == "e":
        B[position] = piece
    else:
        print("Position not empty.")
    board_visual()

def updateBoard():
    # update level 1
    for i,j in A[:2], B[:2]:
        if i != "e" and j != "e":
            print(i)

def main():
    print("------------------------------------")
    board_visual()
    #play game
    placeA(0, "b")
    placeA(1, "b")
    placeA(2, "b")
    placeB(0, "w")
    placeB(1, "w")
    placeB(2, "w")
    board_visual()
    updateBoard()

# Creates the board at its clean state
# 0 = Empty
# Level 0:
A = ["e","e","e","e"]
B = ["e","e","e","e"]
C = ["e","e","e","e"]
D = ["e","e","e","e"]

# Level 1:
E = ["s","s","s"]
F = ["s","s","s"]
G = ["s","s","s"]

# Level 2:
H = ["s","s"]
I = ["s","s"]

# Level 3, top level:
J = ["s"]

main()
