#------------------------------------------------------------------#
# CITS3001 AI PROJECT 2016                                         #
# GAME: PYLOS                                                      #
# AUTHOR: SIMING ZHANG (21147006) and CAMERON ARMSTRONG (21194619) #
#------------------------------------------------------------------#
import copy
import math
import time

#######################################
############ Class: Board  ############
#######################################
class Board(object):

    def __init__(self, player1, player2):  # player1 begins the game, player1 is white
        self.whitepieces = 15
        self.blackpieces = 15
        self.white = player1  # white
        self.black = player2  # black

        # Creates the board at its clean state
        # "e" = empty
        # "s" = sealed
        global actual_board
        actual_board = {
            "A": ["e","e","e","e"],
            "B": ["e","e","e","e"],
            "C": ["e","e","e","e"],
            "D": ["e","e","e","e"],
            "E": ["s","s","s"],
            "F": ["s","s","s"],
            "G": ["s","s","s"],
            "H": ["s","s"],
            "I": ["s","s"],
            "J": ["s"],
            "Z": ["e"]
        }
        global actual_board_test
        actual_board_test = {
            "A": ["e","e","e","e"],
            "B": ["e","b","e","e"],
            "C": ["e","b","b","e"],
            "D": ["b","w","w","w"],
            "E": ["s","s","s"],
            "F": ["s","s","s"],
            "G": ["s","w","s"],
            "H": ["s","s"],
            "I": ["s","s"],
            "J": ["s"],
            "Z": ["e"]
        }
        global simple_board
        simple_board = {
            "E": ["e","e","e"],
            "F": ["e","e","e"],
            "G": ["e","e","e"],
            "H": ["s","s"],
            "I": ["s","s"],
            "J": ["s"],
            "Z": ["e"]
        }

        global simpler_board
        simpler_board = {
            "E": ["w","w","e"],
            "F": ["b","w","b"],
            "G": ["b","b","w"],
            "H": ["s","s"],
            "I": ["s","s"],
            "J": ["s"],
            "Z": ["e"]
        }

        global board_list
        board_list = actual_board

        global last_move
        last_move = ["Z", 0]

    # Visualises the board by printing out the values
    def board_visual(self):
        self.board_update()
        print("")
        print("   0  1  2  3       0  1  2       0  1       0")
        print("A:", end="")
        for i in board_list["A"]:
            print("[", end="")
            if i == "e":
                print(" ]", end="")
            else:
                print(i, end="]")
        print("   E:", end="")
        for i in board_list["E"]:
            print("[", end="")
            if i == "e":
                print(" ]", end="")
            elif i == "s":
                print("X]", end="")
            else:
                print(i, end="]")
        print("   H:", end="")
        for i in board_list["H"]:
            print("[", end="")
            if i == "e":
                print(" ]", end="")
            elif i == "s":
                print("X]", end="")
            else:
                print(i, end="]")
        print("   J:", end="")
        for i in board_list["J"]:
            print("[", end="")
            if i == "e":
                print(" ]", end="")
            elif i == "s":
                print("X]", end="")
            else:
                print(i, end="]")
        print("")
        #-------------------------------#
        print("B:", end="")
        for i in board_list["B"]:
            print("[", end="")
            if i == "e":
                print(" ]", end="")
            else:
                print(i, end="]")
        print("   F:", end="")
        for i in board_list["F"]:
            print("[", end="")
            if i == "e":
                print(" ]", end="")
            elif i == "s":
                print("X]", end="")
            else:
                print(i, end="]")
        print("   I:", end="")
        for i in board_list["I"]:
            print("[", end="")
            if i == "e":
                print(" ]", end="")
            elif i == "s":
                print("X]", end="")
            else:
                print(i, end="]")
        print("")
        #-------------------------------#
        print("C:", end="")
        for i in board_list["C"]:
            print("[", end="")
            if i == "e":
                print(" ]", end="")
            else:
                print(i, end="]")
        print("   G:", end="")
        for i in board_list["G"]:
            print("[", end="")
            if i == "e":
                print(" ]", end="")
            elif i == "s":
                print("X]", end="")
            else:
                print(i, end="]")
        print("")
        #-------------------------------#
        print("D:", end="")
        for i in board_list["D"]:
            print("[", end="")
            if i == "e":
                print(" ]", end="")
            else:
                print(i, end="]")
        print("")
        print("|-------------------------------------------------------------|")
        '''
        print("")
        print(board_list["A"], "   ", board_list["E"], "   ", board_list["H"], "   ", board_list["J"])
        print(board_list["B"], "   ", board_list["F"], "   ", board_list["I"])
        print(board_list["C"], "   ", board_list["G"])
        print(board_list["D"], "   ", )
        '''

    # Updates the board but unsealing positions on higher levels
    # or sealing them based on bottom positions
    def board_update(self):
        # Unseals J[0]
        if board_list["J"][0] == "s":
            board_list["J"][0] = "e"
        for v, w in board_list["H"], board_list["I"]:
            if v == "e" or w == "e" or v == "s" or w == "s":
                board_list["J"][0] = "s"
        # Unseals H[0]
        if board_list["H"][0] == "s":
            board_list["H"][0] = "e"
        for v, w in board_list["E"][:2], board_list["F"][:2]:
            if v == "e" or w == "e" or v == "s" or w == "s":
                board_list["H"][0] = "s"
        # Unseals H[1]
        if board_list["H"][1] == "s":
            board_list["H"][1] = "e"
        for v, w in board_list["E"][1:3], board_list["F"][1:3]:
            if v == "e" or w == "e" or v == "s" or w == "s":
                board_list["H"][1] = "s"
        # Unseals I[0]
        if board_list["I"][0] == "s":
            board_list["I"][0] = "e"
        for v, w in board_list["F"][:2], board_list["G"][:2]:
            if v == "e" or w == "e" or v == "s" or w == "s":
                board_list["I"][0] = "s"
        # Unseals I[1]
        if board_list["I"][1] == "s":
            board_list["I"][1] = "e"
        for v, w in board_list["F"][1:3], board_list["G"][1:3]:
            if v == "e" or w == "e" or v == "s" or w == "s":
                board_list["I"][1] = "s"
        # Unseals E[0]
        if board_list["E"][0] == "s":
            board_list["E"][0] = "e"
        for v, w in board_list["A"][:2], board_list["B"][:2]:
            if v == "e" or w == "e" or v == "s" or w == "s":
                board_list["E"][0] = "s"
        # Unseals E[1]
        if board_list["E"][1] == "s":
            board_list["E"][1] = "e"
        for v, w in board_list["A"][1:3], board_list["B"][1:3]:
            if v == "e" or w == "e" or v == "s" or w == "s":
                board_list["E"][1] = "s"
        # Unseals E[2]
        if board_list["E"][2] == "s":
            board_list["E"][2] = "e"
        for v, w in board_list["A"][2:4], board_list["B"][2:4]:
            if v == "e" or w == "e" or v == "s" or w == "s":
                board_list["E"][2] = "s"
        # Unseals F[0]
        if board_list["F"][0] == "s":
            board_list["F"][0] = "e"
        for v, w in board_list["B"][:2], board_list["C"][:2]:
            if v == "e" or w == "e" or v == "s" or w == "s":
                board_list["F"][0] = "s"
        # Unseals F[1]
        if board_list["F"][1] == "s":
            board_list["F"][1] = "e"
        for v, w in board_list["B"][1:3], board_list["C"][1:3]:
            if v == "e" or w == "e" or v == "s" or w == "s":
                board_list["F"][1] = "s"
        # Unseals F[2]
        if board_list["F"][2] == "s":
            board_list["F"][2] = "e"
        for v, w in board_list["B"][2:4], board_list["C"][2:4]:
            if v == "e" or w == "e" or v == "s" or w == "s":
                board_list["F"][2] = "s"
        # Unseals G[0]
        if board_list["G"][0] == "s":
            board_list["G"][0] = "e"
        for v, w in board_list["C"][:2], board_list["D"][:2]:
            if v == "e" or w == "e" or v == "s" or w == "s":
                board_list["G"][0] = "s"
        # Unseals G[1]
        if board_list["G"][1] == "s":
            board_list["G"][1] = "e"
        for v, w in board_list["C"][1:3], board_list["D"][1:3]:
            if v == "e" or w == "e" or v == "s" or w == "s":
                board_list["G"][1] = "s"
        # Unseals G[2]
        if board_list["G"][2] == "s":
            board_list["G"][2] = "e"
        for v, w in board_list["C"][2:4], board_list["D"][2:4]:
            if v == "e" or w == "e" or v == "s" or w == "s":
                board_list["G"][2] = "s"

    # Checks if a piece needs to be removed
    # @Returns True if a piece needs to be removed
    # @Returns False if otherwise
    def rcheck(self, letter, position):
        if board_list[letter][position] != "s" and board_list[letter][position] != "e":
            # Level 0
            if letter in ("A", "B", "C", "D"):
                if board_list["A"][position] == board_list["B"][position] == board_list["C"][position] == board_list["D"][position]:
                    return True
                if board_list[letter][0] == board_list[letter][1] == board_list[letter][2] == board_list[letter][3]:
                    return True
                if letter == "A":
                    if position == 0:
                        if board_list["A"][0] == board_list["A"][1] == board_list["B"][0] == board_list["B"][1]:
                            return True
                    if position == 1:
                        if board_list["A"][0] == board_list["A"][1] == board_list["B"][0] == board_list["B"][1]:
                            return True
                        if board_list["A"][1] == board_list["A"][2] == board_list["B"][1] == board_list["B"][2]:
                            return True
                    if position == 2:
                        if board_list["A"][2] == board_list["A"][3] == board_list["B"][2] == board_list["B"][3]:
                            return True
                        if board_list["A"][1] == board_list["A"][2] == board_list["B"][1] == board_list["B"][2]:
                            return True
                    if position == 3:
                        if board_list["A"][2] == board_list["A"][3] == board_list["B"][2] == board_list["B"][3]:
                            return True
                if letter == "B":
                    if position == 0:
                        if board_list["B"][0] == board_list["B"][1] == board_list["A"][0] == board_list["A"][1]:
                            return True
                        if board_list["B"][0] == board_list["B"][1] == board_list["C"][0] == board_list["C"][1]:
                            return True
                    if position == 1:
                        if board_list["B"][0] == board_list["B"][1] == board_list["A"][0] == board_list["A"][1]:
                            return True
                        if board_list["B"][0] == board_list["B"][1] == board_list["C"][0] == board_list["C"][1]:
                            return True
                        if board_list["B"][1] == board_list["A"][1] == board_list["B"][2] == board_list["A"][2]:
                            return True
                        if board_list["B"][1] == board_list["C"][1] == board_list["B"][2] == board_list["C"][2]:
                            return True
                    if position == 2:
                        if board_list["B"][1] == board_list["A"][1] == board_list["B"][2] == board_list["A"][2]:
                            return True
                        if board_list["B"][1] == board_list["C"][1] == board_list["B"][2] == board_list["C"][2]:
                            return True
                        if board_list["B"][2] == board_list["A"][2] == board_list["B"][3] == board_list["A"][3]:
                            return True
                        if board_list["B"][2] == board_list["C"][2] == board_list["B"][3] == board_list["C"][3]:
                            return True
                    if position == 3:
                        if board_list["B"][2] == board_list["A"][2] == board_list["B"][3] == board_list["A"][3]:
                            return True
                        if board_list["B"][2] == board_list["C"][2] == board_list["B"][3] == board_list["C"][3]:
                            return True
                if letter == "C":
                    if position == 0:
                        if board_list["C"][0] == board_list["B"][0] == board_list["B"][1] == board_list["C"][1]:
                            return True
                        if board_list["C"][0] == board_list["D"][0] == board_list["D"][1] == board_list["C"][1]:
                            return True
                    if position == 1:
                        if board_list["C"][0] == board_list["B"][0] == board_list["B"][1] == board_list["C"][1]:
                            return True
                        if board_list["C"][0] == board_list["D"][0] == board_list["D"][1] == board_list["C"][1]:
                            return True
                        if board_list["C"][1] == board_list["B"][1] == board_list["B"][2] == board_list["C"][2]:
                            return True
                        if board_list["C"][1] == board_list["C"][2] == board_list["D"][1] == board_list["D"][2]:
                            return True
                    if position == 2:
                        if board_list["C"][1] == board_list["B"][1] == board_list["B"][2] == board_list["C"][2]:
                            return True
                        if board_list["C"][1] == board_list["C"][2] == board_list["D"][1] == board_list["D"][2]:
                            return True
                        if board_list["C"][2] == board_list["B"][2] == board_list["B"][2] == board_list["C"][3]:
                            return True
                        if board_list["C"][2] == board_list["C"][3] == board_list["D"][3] == board_list["D"][2]:
                            return True
                    if position == 3:
                        if board_list["C"][2] == board_list["B"][2] == board_list["B"][3] == board_list["C"][3]:
                            return True
                        if board_list["C"][2] == board_list["C"][3] == board_list["D"][3] == board_list["D"][2]:
                            return True
                if letter == "D":
                    if position == 0:
                        if board_list["D"][0] == board_list["C"][0] == board_list["C"][1] == board_list["D"][1]:
                            return True
                    if position == 1:
                        if board_list["D"][0] == board_list["C"][0] == board_list["C"][1] == board_list["D"][1]:
                            return True
                        if board_list["D"][1] == board_list["C"][1] == board_list["C"][2] == board_list["D"][2]:
                            return True
                    if position == 2:
                        if board_list["D"][1] == board_list["C"][1] == board_list["C"][2] == board_list["D"][2]:
                            return True
                        if board_list["D"][2] == board_list["C"][2] == board_list["C"][3] == board_list["D"][3]:
                            return True
                    if position == 3:
                        if board_list["D"][2] == board_list["C"][2] == board_list["C"][3] == board_list["D"][3]:
                            return True
            # Level 1
            if letter in ("E", "F", "G"):
                if board_list["E"][position] == board_list["F"][position] == board_list["G"][position]:
                    return True
                if board_list[letter][0] == board_list[letter][1] == board_list[letter][2]:
                    return True
                if letter == "E":
                    if position == 0:
                        if board_list["E"][0] == board_list["E"][1] == board_list["F"][0] == board_list["F"][1]:
                            return True
                    if position == 2:
                        if board_list["E"][1] == board_list["E"][2] == board_list["F"][1] == board_list["F"][2]:
                            return True
                    if position == 1:
                        if board_list["E"][0] == board_list["E"][1] == board_list["F"][0] == board_list["F"][1]:
                            return True
                        if board_list["E"][1] == board_list["E"][2] == board_list["F"][1] == board_list["F"][2]:
                            return True
                if letter == "F":
                    if position == 0:
                        if board_list["E"][0] == board_list["E"][1] == board_list["F"][0] == board_list["F"][1]:
                            return True
                        if board_list["G"][0] == board_list["G"][1] == board_list["F"][0] == board_list["F"][1]:
                            return True
                    if position == 2:
                        if board_list["E"][1] == board_list["E"][2] == board_list["F"][1] == board_list["F"][2]:
                            return True
                        if board_list["G"][1] == board_list["G"][2] == board_list["F"][1] == board_list["F"][2]:
                            return True
                    if position == 1:
                        if board_list["E"][0] == board_list["E"][1] == board_list["F"][0] == board_list["F"][1]:
                            return True
                        if board_list["G"][0] == board_list["G"][1] == board_list["F"][0] == board_list["F"][1]:
                            return True
                        if board_list["E"][1] == board_list["E"][2] == board_list["F"][1] == board_list["F"][2]:
                            return True
                        if board_list["G"][1] == board_list["G"][2] == board_list["F"][1] == board_list["F"][2]:
                            return True
                if letter == "G":
                    if position == 0:
                        if board_list["G"][0] == board_list["G"][1] == board_list["F"][0] == board_list["F"][1]:
                            return True
                    if position == 2:
                        if board_list["G"][1] == board_list["G"][2] == board_list["F"][1] == board_list["F"][2]:
                            return True
                    if position == 1:
                        if board_list["G"][0] == board_list["G"][1] == board_list["F"][0] == board_list["F"][1]:
                            return True
                        if board_list["G"][1] == board_list["G"][2] == board_list["F"][1] == board_list["F"][2]:
                            return True
            # Level 2
            if letter in ("H", "I"):
                if board_list["H"][0] == board_list["H"][1] == board_list["I"][0] == board_list["I"][1]:
                    return True
            return False
        return False

    # Checks if a position can be removed based on if any piece is on top of it
    # @Returns True if no piece stands on top of the position
    # @Returns False if a piece is stacked on top of the position
    def canremove(self, letter, position):
        if letter == "A":
            if position == 0:
                if board_list["E"][0] in ("s", "e"):
                    return True
            if position == 1:
                if board_list["E"][0] in ("s", "e") and board_list["E"][1] in ("s", "e"):
                    return True
            if position == 2:
                if board_list["E"][1] in ("s", "e") and board_list["E"][2] in ("s", "e"):
                    return True
            if position == 3:
                if board_list["E"][2] in ("s", "e"):
                    return True
        elif letter == "B":
            if position == 0:
                if board_list["E"][0] in ("s", "e") and board_list["F"][0] in ("s", "e"):
                    return True
            if position == 1:
                if board_list["E"][0] in ("s", "e") and board_list["F"][0] in ("s", "e") and board_list["E"][1] in ("s", "e") and board_list["F"][1] in ("s", "e"):
                    return True
            if position == 2:
                if board_list["E"][1] in ("s", "e") and board_list["F"][1] in ("s", "e") and board_list["E"][2] in ("s", "e") and board_list["F"][2] in ("s", "e"):
                    return True
            if position == 3:
                if board_list["E"][2] in ("s", "e") and board_list["F"][2] in ("s", "e"):
                    return True
        elif letter == "C":
            if position == 0:
                if board_list["F"][0] in ("s", "e") and board_list["G"][0] in ("s", "e"):
                    return True
            if position == 1:
                if board_list["F"][0] in ("s", "e") and board_list["G"][0] in ("s", "e") and board_list["F"][1] in ("s", "e") and board_list["G"][1] in ("s", "e"):
                    return True
            if position == 2:
                if board_list["F"][1] in ("s", "e") and board_list["F"][2] in ("s", "e") and board_list["G"][1] in ("s", "e") and board_list["G"][2] in ("s", "e"):
                    return True
            if position == 3:
                if board_list["F"][2] in ("s", "e") and board_list["G"][2] in ("s", "e"):
                    return True
        elif letter == "D":
            if position == 0:
                if board_list["G"][0] in ("s", "e"):
                    return True
            if position == 1:
                if board_list["G"][0] in ("s", "e") and  board_list["G"][1] in ("s", "e"):
                    return True
            if position == 2:
                if board_list["G"][1] in ("s", "e") and  board_list["G"][2] in ("s", "e"):
                    return True
            if position == 3:
                if board_list["G"][2] in ("s", "e"):
                    return True
        elif letter == "E":
            if position == 0:
                if board_list["H"][0] in ("s", "e"):
                    return True
                else:
                    print("There is a piece stacked on top.")
                    return False
            if position == 1:
                if board_list["H"][0] in ("s", "e") and board_list["H"][1] in ("s", "e"):
                    return True
                else:
                    print("There is a piece stacked on top.")
                    return False
            if position == 2:
                if board_list["H"][1] in ("s", "e"):
                    return True
                else:
                    print("There is a piece stacked on top.")
                    return False
        elif letter == "F":
            if position == 0:
                if board_list["H"][0] in ("s", "e") and board_list["I"][0] in ("s", "e"):
                    return True
                else:
                    print("There is a piece stacked on top.")
                    return False
            if position == 1:
                if board_list["H"][0] in ("s", "e") and board_list["H"][1] in ("s", "e") and board_list["I"][0] in ("s", "e") and board_list["I"][1] in ("s", "e"):
                    return True
                else:
                    print("There is a piece stacked on top.")
                    return False
            if position == 2:
                if board_list["H"][1] in ("s", "e") and board_list["I"][1] in ("s", "e"):
                    return True
                else:
                    print("There is a piece stacked on top.")
                    return False
        elif letter == "G":
            if position == 0:
                if board_list["I"][0] in ("s", "e"):
                    return True
                else:
                    print("There is a piece stacked on top.")
                    return False
            if position == 1:
                if board_list["I"][0] in ("s", "e") and board_list["I"][1] in ("s", "e"):
                    return True
                else:
                    print("There is a piece stacked on top.")
                    return False
            if position == 2:
                if board_list["I"][1] in ("s", "e"):
                    return True
                else:
                    print("There is a piece stacked on top.")
                    return False
        elif letter in ("H", "I"):
            return True
        else:
            return False

    # Places piece on position
    # @returns True if successful
    # @returns False if otherwise
    def place(self, letter, position, piece, boardlist, piecenumber):
        try:
            if board_list[letter][position] == "e":
                board_list[letter][position] = piece
                return True
            else:
                print("Position is not empty.")
                return False
        except:
            print("Invalid input, please check your input is correct.111")
            return False

    # Raises a piece from position2 to position
    # Destination = letter2
    # From = letter
    # @Returns True if raise is successful
    # @Returns False if otherwise
    def raisep(self, letter, position, piece, letter2, position2, boardlist, piecenumber):
        if self.checklevel(letter2, letter) and self.removep(letter2, position2, piece, boardlist, piecenumber) and self.place(letter, position, piece, boardlist, piecenumber):
            return True
        else:
            return False

    # Removes a piece from position
    # @returns True if remove is successful
    # @returns False if otherwise
    def removep(self, letter, position, piece, boardlist, piecenumber):
        try:
            if self.canremove(letter, position) and board_list[letter][position] == piece:
                board_list[letter][position] = "e"
                return True
            else:
                print("You cannot remove from that position.")
                return False
        except:
            print("Invalid input, please check your input is correct.222")
            return False

    # Checks the level of different coordinates
    # @Returns True if level is lower level 2
    #   for example True for level = A and level 2 = E
    # @Returns False if level is above level 2
    def checklevel(self, letter, letter2):
        num = 0
        num2 = 0
        if letter in ("A", "B", "C", "D"):
            num = 0
        elif letter in ("E", "F", "G"):
            num = 1
        elif letter in ("H", "I"):
            num = 2
        else:
            print("Invalid input.")
            return False
        if letter2 in ("A", "B", "C", "D"):
            num2 = 0
        elif letter2 in ("E", "F", "G"):
            num2 = 1
        elif letter2 in ("H", "I"):
            num2 = 2
        elif letter2 == "Z":
            num2 = 4
        else:
            print("Invalid input.")
            return False
        num3 = num2 - num
        if num3 > 0:
            if letter2 == "Z":
                print("", end="")
            else:
                print("Piece from " + letter + " raised to " + letter2)
            return True
        else:
            print("You can only raise pieces to an upper level.")
            return False

    # Play function that runs the game
    def play(self):
        def switchPlayer(player):
            if player is self.white:
                return self.black
            else:
                return self.white

        player = self.white

        while True:
            board_list["Z"][0] = "e"
            self.board_visual()
            # removes pieces
            if self.rcheck(last_move[0], last_move[1]):
                player = switchPlayer(player)
                x = 0
                while True:
                    if x == 1:
                        break
                    # Tell player it's their turn
                    print(player.name + "'s move please remove a piece.")
                    if player is self.white:
                        input_list = player.move(board_list, self.whitepieces, self.blackpieces, "w", "b", 1)
                    else:
                        input_list = player.move(board_list, self.blackpieces, self.whitepieces, "b", "w", 1)
                    try:
                        i = str(input_list[0])
                        j = int(input_list[1])
                    except:
                        print("Invalid input.")
                        continue
                    if player is self.white:
                        if self.raisep("Z", 0, "w", i, j, board_list, self.whitepieces):
                            self.whitepieces += 1
                            print("Piece removed from " + i + "," + str(j))
                            print(player.name + " now has " + str(self.whitepieces) + " pieces left.")
                            last_move[0] = i
                            last_move[1] = j
                        else:
                            continue
                    else:
                        if self.raisep("Z", 0, "b", i, j, board_list, self.blackpieces):
                            self.blackpieces += 1
                            print("Piece removed from " + i + "," + str(j))
                            print(player.name + " now has " + str(self.blackpieces) + " pieces left.")
                            last_move[0] = i
                            last_move[1] = j
                        else:
                            continue
                    x = 1
                    print(last_move)
                board_list["Z"][0] = "e"
                while x == 1:
                    self.board_visual()
                    # Tell player it's their turn
                    print(player.name + "'s move please remove another piece. Or enter _ to skip")
                    if player is self.white:
                        input_list = player.move(board_list, self.whitepieces, self.blackpieces, "w", "b", 2)
                    else:
                        input_list = player.move(board_list, self.blackpieces, self.whitepieces, "b", "w", 2)
                    if input_list == ["_"] or input_list == "_":
                        x = 0
                        break
                    try:
                        i = str(input_list[0])
                        j = int(input_list[1])
                    except:
                        print("Invalid input.")
                        continue
                    if player is self.white:
                        if self.raisep("Z", 0, "w", i, j, board_list, self.whitepieces):
                            self.whitepieces += 1
                            print("Piece removed from " + i + "," + str(j))
                            print(player.name + " now has " + str(self.whitepieces) + " pieces left.")
                            last_move[0] = i
                            last_move[1] = j
                        else:
                            continue
                    else:
                        if self.raisep("Z", 0, "b", i, j, board_list, self.blackpieces):
                            self.blackpieces += 1
                            print("Piece removed from " + i + "," + str(j))
                            print(player.name + " now has " + str(self.blackpieces) + " pieces left.")
                            last_move[0] = i
                            last_move[1] = j
                        else:
                            continue
                    x = 0
                    print(last_move)
                player = switchPlayer(player)


            # placing pieces
            else:
                # Tell player it's their turn
                print(player.name + "'s move, you have ", end="")
                if player is self.white:
                    print(str(self.whitepieces) + " pieces left")
                    if self.whitepieces == 0:  # if you have 0 pieces the other player wins
                        self.win(switchPlayer(player))
                        break
                    input_list = player.move(board_list, self.whitepieces, self.blackpieces, "w", "b", 0)
                else:
                    print(str(self.blackpieces) + " pieces left")
                    if self.blackpieces == 0:  # if you have 0 pieces the other player wins
                        self.win(switchPlayer(player))
                        break
                    input_list = player.move(board_list, self.blackpieces, self.whitepieces, "b", "w", 0)
                # If you just want to place a piece
                if len(input_list) == 2:
                    try:
                        i = str(input_list[0])
                        j = int(input_list[1])
                    except:
                        print("Invalid input.")
                        continue
                    if player is self.white:
                        if self.place(i, j, "w", board_list, self.whitepieces):
                            self.whitepieces -= 1
                            player = switchPlayer(player)
                            last_move[0] = i
                            last_move[1] = j
                    else:
                        if self.place(i, j, "b", board_list, self.blackpieces):
                            self.blackpieces -= 1
                            player = switchPlayer(player)
                            last_move[0] = i
                            last_move[1] = j
                # if you want to raise a piece
                else:
                    try:
                        i = str(input_list[0])
                        j = int(input_list[1])
                        x = str(input_list[2])
                        y = int(input_list[3])
                    except:
                        print("Invalid input.")
                        continue
                    if player is self.white:
                        if self.raisep(i, j, "w", x, y, board_list, self.whitepieces):
                            player = switchPlayer(player)
                            last_move[0] = i
                            last_move[1] = j
                    else:
                        if self.raisep(i, j, "b", x, y, board_list, self.blackpieces):
                            player = switchPlayer(player)
                            last_move[0] = i
                            last_move[1] = j
                # You win by placing your piece on the top-most position
                if board_list["J"][0] == "b":
                    self.win(switchPlayer(player))
                    break
                elif board_list["J"][0] == "w":
                    self.win(switchPlayer(player))
                    break

    def win(self,player):
        self.board_visual()
        print(player.name + " won!")


#######################################
############ Class: Player ############
#######################################
class Player(object):

    def __init__(self, name):
        self.name = name

    def move(self, boardlist, mypiecenumber, theirpiecenumber, mypiece, theirpiece, flag):
        inputs = input("Enter position seperated by comma for example A,1: ")
        input_list = inputs.split(',')
        return input_list

#######################################
############ Class: AI ################
#######################################
class Artificial(Player):

    # Minimax for finding the best next move
    # @Returns the score and move
    def minimax(self, boardlist, side, mypiece, mynumber, theirpiece, theirnumber, depth, flag):
        best = [None, None]
        #---------------------------------------------------PLACING OR RASING A STONE---------------------------------------------------#
        if flag == 0:  # normal moves or raise
            if depth == 0:  # last move been searched
                if side == 0:  # my turn
                    movelist = self.moveList(boardlist, mypiece)
                    best = [-math.inf, ["F", 0]]
                    for i in movelist:
                        if len(i) == 2:  # if its just a simple place and not a raise
                            self.mplace(i[0], i[1], mypiece, boardlist)  # place the piece
                            myscore = self.evaluate(boardlist, i[0], i[1], mypiece, mynumber-1, theirpiece, theirnumber)  # evaluate the score of the current board state
                            self.mundoplace(i[0], i[1], boardlist)
                        else:  # len(i) == 4 if its a raise
                            self.mplace(i[0], i[1], mypiece, boardlist)  # place the piece first
                            self.mundoplace(i[2], i[3], boardlist)  # then remove the piece
                            myscore = self.evaluate(boardlist, i[0], i[1], mypiece, mynumber-1, theirpiece, theirnumber)  # evaluate the score of the current board state
                            self.mundoplace(i[0], i[1], boardlist)
                            self.mplace(i[2], i[3], mypiece, boardlist)
                        if myscore >= best[0]:  # see if myscore exceeds best score so far
                            best[0] = myscore
                            best[1] = i
                    return best  # return the best score and move
                else:  # if side == 1, ie their turn
                    movelist = self.moveList(boardlist, theirpiece)
                    best = [math.inf, ["F", 0]]
                    for i in movelist:
                        if len(i) == 2:  # if its just a simple place and not a raise
                            self.mplace(i[0], i[1], theirpiece, boardlist)
                            myscore = self.evaluate(boardlist, i[0], i[1], mypiece, mynumber, theirpiece, theirnumber-1)  # evaluate the score of the current board state
                            self.mundoplace(i[0], i[1], boardlist)
                        else:  # len(i) == 4 if its a raise
                            self.mplace(i[0], i[1], theirpiece, boardlist)  # place their piece
                            self.mundoplace(i[2], i[3], boardlist)  # remove that piece thus making a raise
                            myscore = self.evaluate(boardlist, i[0], i[1], mypiece, mynumber, theirpiece, theirnumber-1)  # evaluate the score of the current board state
                            self.mundoplace(i[0], i[1], boardlist)
                            self.mplace(i[2], i[3], theirpiece, boardlist)
                        if myscore <= best[0]:  # see if myscore is smaller than the best score so far
                            best[0] = myscore
                            best[1] = i
                    return best

            else:  # if depth != 0, ie not last move
                if side == 0:  # my turn
                    movelist = self.moveList(boardlist, mypiece)
                    best = [-math.inf, ["F",0]]
                    for i in movelist:
                        if len(i) == 2:  # if its just a simple place and not a raise
                            self.mplace(i[0], i[1], mypiece, boardlist)  # place the piece
                            if self.mrcheck(i[0], i[1], boardlist):
                                myscore = self.minimax(boardlist, 0, mypiece, mynumber-1, theirpiece, theirnumber, depth-1, 1)[0]
                            else:
                                myscore = self.minimax(boardlist, 1, mypiece, mynumber-1, theirpiece, theirnumber, depth-1, 0)[0]
                            self.mundoplace(i[0], i[1], boardlist)
                        else:  # len(i) == 4 if its a raise
                            self.mplace(i[0], i[1], mypiece, boardlist)  # place the piece first
                            self.mundoplace(i[2], i[3], boardlist)  # then remove the piece
                            if self.mrcheck(i[0], i[1], boardlist):
                                myscore = self.minimax(boardlist, 0, mypiece, mynumber, theirpiece, theirnumber, depth-1, 1)[0]
                            else:
                                myscore = self.minimax(boardlist, 1, mypiece, mynumber, theirpiece, theirnumber, depth-1, 0)[0]
                            self.mundoplace(i[0], i[1], boardlist)
                            self.mplace(i[2], i[3], mypiece, boardlist)
                        if myscore >= best[0]:  # see if myscore exceeds best score so far
                            best[0] = myscore
                            best[1] = i
                    return best  # return the best score and move
                else:  # if side == 1, ie their turn
                    movelist = self.moveList(boardlist, theirpiece)
                    best = [math.inf, ["F", 0]]
                    for i in movelist:
                        if len(i) == 2:  # if its just a simple place and not a raise
                            self.mplace(i[0], i[1], theirpiece, boardlist)
                            if self.mrcheck(i[0], i[1], boardlist):
                                myscore = self.minimax(boardlist, 1, mypiece, mynumber, theirpiece, theirnumber-1, depth-1, 1)[0]
                            else:
                                myscore = self.minimax(boardlist, 0, mypiece, mynumber, theirpiece, theirnumber-1, depth-1, 0)[0]
                            self.mundoplace(i[0], i[1], boardlist)
                        else:  # len(i) == 4 if its a raise
                            self.mplace(i[0], i[1], theirpiece, boardlist)  # place their piece
                            self.mundoplace(i[2], i[3], boardlist)  # remove that piece thus making a raise
                            if self.mrcheck(i[0], i[1], boardlist):
                                myscore = self.minimax(boardlist, 1, mypiece, mynumber, theirpiece, theirnumber, depth-1, 1)[0]
                            else:
                                myscore = self.minimax(boardlist, 0, mypiece, mynumber, theirpiece, theirnumber, depth-1, 0)[0]
                            self.mundoplace(i[0], i[1], boardlist)
                            self.mplace(i[2], i[3], theirpiece, boardlist)
                        if myscore <= best[0]:  # see if myscore is smaller than the best score so far
                            best[0] = myscore
                            best[1] = i
                    return best
        #---------------------------------------------------COMPULSORY REMOVES---------------------------------------------------#
        elif flag == 1:  # for must removes
            if depth == 0:  # last move been searched
                if side == 0:  # if its my turn
                    movelist = self.removeList(boardlist, mypiece, 3)  # get a list of all the positions i can remove from
                    best = [-math.inf, ["E", 0]]
                    for i in movelist:
                        self.mundoplace(i[0], i[1], boardlist)
                        myscore = self.evaluate(boardlist, i[0], i[1], mypiece, mynumber+1, theirpiece, theirnumber)
                        self.mplace(i[0], i[1], mypiece, boardlist)
                        if myscore >= best[0]:
                            best[0] = myscore
                            best[1] = i
                    return best
                else:  # if side == 1, ie their turn
                    movelist = self.removeList(boardlist, theirpiece, 3)
                    best = [math.inf, ["E", 0]]
                    for i in movelist:
                        self.mundoplace(i[0], i[1], boardlist)
                        myscore = self.evaluate(boardlist, i[0], i[1], mypiece, mynumber, theirpiece, theirnumber+1)
                        self.mplace(i[0], i[1], theirpiece, boardlist)
                        if myscore <= best[0]:
                            best[0] = myscore
                            best[1] = i
                    return best

            else:  # if depth != 0, ie not the last move been searched
                if side == 0:  # if its my turn
                    movelist = self.removeList(boardlist, mypiece, 3)  # get a list of all the positions i can remove from
                    best = [-math.inf, ["E", 0]]
                    for i in movelist:
                        self.mundoplace(i[0], i[1], boardlist)
                        myscore = self.minimax(boardlist, 0, mypiece, mynumber+1, theirpiece, theirnumber, depth-1, 2)[0]
                        self.mplace(i[0], i[1], mypiece, boardlist)
                        if myscore >= best[0]:
                            best[0] = myscore
                            best[1] = i
                    return best
                else:  # if side == 1, ie their turn
                    movelist = self.removeList(boardlist, theirpiece, 3)
                    best = [math.inf, ["E", 0]]
                    for i in movelist:
                        self.mundoplace(i[0], i[1], boardlist)
                        myscore = self.minimax(boardlist, 1, mypiece, mynumber, theirpiece, theirnumber+1, depth-1, 2)[0]
                        self.mplace(i[0], i[1], theirpiece, boardlist)
                        if myscore <= best[0]:
                            best[0] = myscore
                            best[1] = i
                    return best
        #---------------------------------------------------OPTIONAL REMOVES---------------------------------------------------#
        else:  # flag == 2, for optional removes
            if depth == 0:  # last move been searched
                if side == 0:  # if its my turn
                    movelist = self.removeList(boardlist, mypiece, 3)  # get a list of all the positions i can remove from
                    movelist.append("_")
                    best = [-math.inf, ["E", 0]]
                    for i in movelist:
                        if i == "_":
                            myscore = self.evaluate(boardlist, "Z", 0, mypiece, mynumber, theirpiece, theirnumber)
                        else:
                            self.mundoplace(i[0], i[1], boardlist)
                            myscore = self.evaluate(boardlist, i[0], i[1], mypiece, mynumber+1, theirpiece, theirnumber)
                            self.mplace(i[0], i[1], mypiece, boardlist)
                        if myscore >= best[0]:
                            best[0] = myscore
                            best[1] = i
                    return best
                else:  # if side == 1, ie their turn
                    movelist = self.removeList(boardlist, theirpiece, 3)
                    moevlist.append("_")
                    best = [math.inf, ["E", 0]]
                    for i in movelist:
                        if i == "_":
                            myscore = self.evaluate(boardlist, "Z", 0, mypiece, mynumber, theirpiece, theirnumber)
                        else:
                            self.mundoplace(i[0], i[1], boardlist)
                            myscore = self.evaluate(boardlist, i[0], i[1], mypiece, mynumber, theirpiece, theirnumber+1)
                            self.mplace(i[0], i[1], theirpiece, boardlist)
                        if myscore <= best[0]:
                            best[0] = myscore
                            best[1] = i
                    return best

            else:  # if depth != 0, ie not the last move been searched
                if side == 0:  # if its my turn
                    movelist = self.removeList(boardlist, mypiece, 3)  # get a list of all the positions i can remove from
                    movelist.append("_")
                    best = [-math.inf, ["E", 0]]
                    for i in movelist:
                        if i == "_":
                            myscore = self.minimax(boardlist, 1, mypiece, mynumber, theirpiece, theirnumber, depth-1, 0)[0]
                        else:
                            self.mundoplace(i[0], i[1], boardlist)
                            myscore = self.minimax(boardlist, 1, mypiece, mynumber+1, theirpiece, theirnumber, depth-1, 0)[0]
                            self.mplace(i[0], i[1], mypiece, boardlist)
                        if myscore >= best[0]:
                            best[0] = myscore
                            best[1] = i
                    return best
                else:  # if side == 1, ie their turn
                    movelist = self.removeList(boardlist, theirpiece, 3)
                    movelist.append("_")
                    best = [math.inf, ["E", 0]]
                    for i in movelist:
                        if i == "_":
                            myscore = self.minimax(boardlist, 0, mypiece, mynumber, theirpiece, theirnumber, depth-1, 0)[0]
                        else:
                            self.mundoplace(i[0], i[1], boardlist)
                            myscore = self.minimax(boardlist, 0, mypiece, mynumber, theirpiece, theirnumber+1, depth-1, 0)[0]
                            self.mplace(i[0], i[1], theirpiece, boardlist)
                        if myscore <= best[0]:
                            best[0] = myscore
                            best[1] = i
                    return best

    # Improved version of minimax - alphabeta
    # @Returns the score and move
    def alphabeta(self, alphavalue, betavalue, boardlist, side, mypiece, mynumber, theirpiece, theirnumber, depth, flag):
        best = [None, None]
        alpha = alphavalue
        beta = betavalue
        #---------------------------------------------------PLACING OR RASING A STONE---------------------------------------------------#
        if flag == 0:  # normal moves or raise
            #----------------------------------DEPTH 0----------------------------------#
            if depth == 0:  # last move been searched
                if side == 0:  # my turn
                    movelist = self.moveList(boardlist, mypiece)
                    best = [-math.inf, ["F", 0]]
                    for i in movelist:
                        if best[0] >= beta:
                            break
                        elif best[0] < beta:
                            if len(i) == 2:  # if its just a simple place and not a raise
                                self.mplace(i[0], i[1], mypiece, boardlist)  # place the piece
                                myscore = self.evaluate(boardlist, i[0], i[1], mypiece, mynumber-1, theirpiece, theirnumber)  # evaluate the score of the current board state
                                self.mundoplace(i[0], i[1], boardlist)
                            else:  # len(i) == 4 if its a raise
                                self.mplace(i[0], i[1], mypiece, boardlist)  # place the piece first
                                self.mundoplace(i[2], i[3], boardlist)  # then remove the piece
                                myscore = self.evaluate(boardlist, i[0], i[1], mypiece, mynumber-1, theirpiece, theirnumber)  # evaluate the score of the current board state
                                self.mundoplace(i[0], i[1], boardlist)
                                self.mplace(i[2], i[3], mypiece, boardlist)
                            if myscore >= best[0]:  # see if myscore exceeds best score so far
                                best[0] = myscore
                                best[1] = i
                    return best  # return the best score and move
                else:  # if side == 1, ie their turn
                    movelist = self.moveList(boardlist, theirpiece)
                    best = [math.inf, ["F", 0]]
                    for i in movelist:
                        if best[0] <= alpha:
                            break
                        elif best[0] > alpha:
                            if len(i) == 2:  # if its just a simple place and not a raise
                                self.mplace(i[0], i[1], theirpiece, boardlist)
                                myscore = self.evaluate(boardlist, i[0], i[1], mypiece, mynumber, theirpiece, theirnumber-1)  # evaluate the score of the current board state
                                self.mundoplace(i[0], i[1], boardlist)
                            else:  # len(i) == 4 if its a raise
                                self.mplace(i[0], i[1], theirpiece, boardlist)  # place their piece
                                self.mundoplace(i[2], i[3], boardlist)  # remove that piece thus making a raise
                                myscore = self.evaluate(boardlist, i[0], i[1], mypiece, mynumber, theirpiece, theirnumber-1)  # evaluate the score of the current board state
                                self.mundoplace(i[0], i[1], boardlist)
                                self.mplace(i[2], i[3], theirpiece, boardlist)
                            if myscore <= best[0]:  # see if myscore is smaller than the best score so far
                                best[0] = myscore
                                best[1] = i
                    return best
            #----------------------------------NOT DEPTH 0----------------------------------#
            else:  # if depth != 0, ie not last move
                if side == 0:  # my turn
                    movelist = self.moveList(boardlist, mypiece)
                    best = [-math.inf, ["F", 0]]
                    for i in movelist:
                        if best[0] >= beta:
                            break
                        elif best[0] < beta:
                            if len(i) == 2:  # if its just a simple place and not a raise
                                self.mplace(i[0], i[1], mypiece, boardlist)  # place the piece
                                if self.mrcheck(i[0], i[1], boardlist):
                                    myscore = self.alphabeta(alpha, beta, boardlist, 0, mypiece, mynumber-1, theirpiece, theirnumber, depth-1, 1)[0]
                                else:
                                    myscore = self.alphabeta(alpha, beta, boardlist, 1, mypiece, mynumber-1, theirpiece, theirnumber, depth-1, 0)[0]
                                self.mundoplace(i[0], i[1], boardlist)
                            else:  # len(i) == 4 if its a raise
                                self.mplace(i[0], i[1], mypiece, boardlist)  # place the piece first
                                self.mundoplace(i[2], i[3], boardlist)  # then remove the piece
                                if self.mrcheck(i[0], i[1], boardlist):
                                    myscore = self.alphabeta(alpha, beta, boardlist, 0, mypiece, mynumber, theirpiece, theirnumber, depth-1, 1)[0]
                                else:
                                    myscore = self.alphabeta(alpha, beta, boardlist, 1, mypiece, mynumber, theirpiece, theirnumber, depth-1, 0)[0]
                                self.mundoplace(i[0], i[1], boardlist)
                                self.mplace(i[2], i[3], mypiece, boardlist)
                            if myscore >= best[0]:  # see if myscore exceeds best score so far
                                best[0] = myscore
                                best[1] = i
                                alpha = myscore
                    return best  # return the best score and move
                else:  # if side == 1, ie their turn
                    movelist = self.moveList(boardlist, theirpiece)
                    best = [math.inf, ["F", 0]]
                    for i in movelist:
                        if best[0] <= alpha:
                            break
                        elif best[0] > alpha:
                            if len(i) == 2:  # if its just a simple place and not a raise
                                self.mplace(i[0], i[1], theirpiece, boardlist)
                                if self.mrcheck(i[0], i[1], boardlist):
                                    myscore = self.alphabeta(alpha, beta, boardlist, 1, mypiece, mynumber, theirpiece, theirnumber-1, depth-1, 1)[0]
                                else:
                                    myscore = self.alphabeta(alpha, beta, boardlist, 0, mypiece, mynumber, theirpiece, theirnumber-1, depth-1, 0)[0]
                                self.mundoplace(i[0], i[1], boardlist)
                            else:  # len(i) == 4 if its a raise
                                self.mplace(i[0], i[1], theirpiece, boardlist)  # place their piece
                                self.mundoplace(i[2], i[3], boardlist)  # remove that piece thus making a raise
                                if self.mrcheck(i[0], i[1], boardlist):
                                    myscore = self.alphabeta(alpha, beta, boardlist, 1, mypiece, mynumber, theirpiece, theirnumber, depth-1, 1)[0]
                                else:
                                    myscore = self.alphabeta(alpha, beta, boardlist, 0, mypiece, mynumber, theirpiece, theirnumber, depth-1, 0)[0]
                                self.mundoplace(i[0], i[1], boardlist)
                                self.mplace(i[2], i[3], theirpiece, boardlist)
                            if myscore <= best[0]:  # see if myscore is smaller than the best score so far
                                best[0] = myscore
                                best[1] = i
                                beta = myscore
                    return best
        #---------------------------------------------------COMPULSORY REMOVES---------------------------------------------------#
        elif flag == 1:  # for must removes
            if depth == 0:  # last move been searched
                if side == 0:  # if its my turn
                    movelist = self.removeList(boardlist, mypiece, 3)  # get a list of all the positions i can remove from
                    best = [-math.inf, ["E", 0]]
                    for i in movelist:
                        if best[0] >= beta:
                            break
                        elif best[0] < beta:
                            self.mundoplace(i[0], i[1], boardlist)
                            myscore = self.evaluate(boardlist, i[0], i[1], mypiece, mynumber+1, theirpiece, theirnumber)
                            self.mplace(i[0], i[1], mypiece, boardlist)
                            if myscore >= best[0]:
                                best[0] = myscore
                                best[1] = i
                                alpha = myscore
                    return best
                else:  # if side == 1, ie their turn
                    movelist = self.removeList(boardlist, theirpiece, 3)
                    best = [math.inf, ["E", 0]]
                    for i in movelist:
                        if best[0] <= alpha:
                            break
                        elif best[0] > alpha:
                            self.mundoplace(i[0], i[1], boardlist)
                            myscore = self.evaluate(boardlist, i[0], i[1], mypiece, mynumber, theirpiece, theirnumber+1)
                            self.mplace(i[0], i[1], theirpiece, boardlist)
                            if myscore <= best[0]:
                                best[0] = myscore
                                best[1] = i
                                beta = myscore
                    return best

            else:  # if depth != 0, ie not the last move been searched
                if side == 0:  # if its my turn
                    movelist = self.removeList(boardlist, mypiece, 3)  # get a list of all the positions i can remove from
                    best = [-math.inf, ["E", 0]]
                    for i in movelist:
                        if best[0] >= beta:
                            break
                        elif best[0] < beta:
                            self.mundoplace(i[0], i[1], boardlist)
                            myscore = self.alphabeta(alpha, beta, boardlist, 0, mypiece, mynumber+1, theirpiece, theirnumber, depth-1, 2)[0]
                            self.mplace(i[0], i[1], mypiece, boardlist)
                            if myscore >= best[0]:
                                best[0] = myscore
                                best[1] = i
                                alpha = myscore
                    return best
                else:  # if side == 1, ie their turn
                    movelist = self.removeList(boardlist, theirpiece, 3)
                    best = [math.inf, ["E", 0]]
                    for i in movelist:
                        if best[0] <= alpha:
                            break
                        elif best[0] > alpha:
                            self.mundoplace(i[0], i[1], boardlist)
                            myscore = self.alphabeta(alpha, beta, boardlist, 1, mypiece, mynumber, theirpiece, theirnumber+1, depth-1, 2)[0]
                            self.mplace(i[0], i[1], theirpiece, boardlist)
                            if myscore <= best[0]:
                                best[0] = myscore
                                best[1] = i
                                beta = myscore
                    return best
        #---------------------------------------------------OPTIONAL REMOVES---------------------------------------------------#
        else:  # flag == 2, for optional removes
            if depth == 0:  # last move been searched
                if side == 0:  # if its my turn
                    movelist = self.removeList(boardlist, mypiece, 3)  # get a list of all the positions i can remove from
                    movelist.append("_")
                    best = [-math.inf, ["E", 0]]
                    for i in movelist:
                        if best[0] >= beta:
                            break
                        elif best[0] < beta:
                            if i == "_":
                                myscore = self.evaluate(boardlist, "Z", 0, mypiece, mynumber, theirpiece, theirnumber)
                            else:
                                self.mundoplace(i[0], i[1], boardlist)
                                myscore = self.evaluate(boardlist, i[0], i[1], mypiece, mynumber+1, theirpiece, theirnumber)
                                self.mplace(i[0], i[1], mypiece, boardlist)
                            if myscore >= best[0]:
                                best[0] = myscore
                                best[1] = i
                    return best
                else:  # if side == 1, ie their turn
                    movelist = self.removeList(boardlist, theirpiece, 3)
                    movelist.append("_")
                    best = [math.inf, ["E", 0]]
                    for i in movelist:
                        if best[0] <= alpha:
                            break
                        elif best[0] > alpha:
                            if i == "_":
                                myscore = self.evaluate(boardlist, "Z", 0, mypiece, mynumber, theirpiece, theirnumber)
                            else:
                                self.mundoplace(i[0], i[1], boardlist)
                                myscore = self.evaluate(boardlist, i[0], i[1], mypiece, mynumber, theirpiece, theirnumber+1)
                                self.mplace(i[0], i[1], theirpiece, boardlist)
                            if myscore <= best[0]:
                                best[0] = myscore
                                best[1] = i
                    return best

            else:  # if depth != 0, ie not the last move been searched
                if side == 0:  # if its my turn
                    movelist = self.removeList(boardlist, mypiece, 3)  # get a list of all the positions i can remove from
                    movelist.append("_")
                    best = [-math.inf, ["E", 0]]
                    for i in movelist:
                        if best[0] >= beta:
                            break
                        elif best[0] < beta:
                            if i == "_":
                                myscore = self.alphabeta(alpha, beta, boardlist, 1, mypiece, mynumber, theirpiece, theirnumber, depth-1, 0)[0]
                            else:
                                self.mundoplace(i[0], i[1], boardlist)
                                myscore = self.alphabeta(alpha, beta, boardlist, 1, mypiece, mynumber+1, theirpiece, theirnumber, depth-1, 0)[0]
                                self.mplace(i[0], i[1], mypiece, boardlist)
                            if myscore >= best[0]:
                                best[0] = myscore
                                best[1] = i
                                alpha = myscore
                    return best
                else:  # if side == 1, ie their turn
                    movelist = self.removeList(boardlist, theirpiece, 3)
                    movelist.append("_")
                    best = [math.inf, ["E", 0]]
                    for i in movelist:
                        if best[0] <= alpha:
                            break
                        elif best[0] > alpha:
                            if i == "_":
                                myscore = self.alphabeta(alpha, beta, boardlist, 0, mypiece, mynumber, theirpiece, theirnumber, depth-1, 0)[0]
                            else:
                                self.mundoplace(i[0], i[1], boardlist)
                                myscore = self.alphabeta(alpha, beta, boardlist, 0, mypiece, mynumber, theirpiece, theirnumber+1, depth-1, 0)[0]
                                self.mplace(i[0], i[1], theirpiece, boardlist)
                            if myscore <= best[0]:
                                best[0] = myscore
                                best[1] = i
                                beta = myscore
                    return best

    # Generates possible move list based on game state
    # stores the moves in a list, count
    # @Returns count
    def moveList(self, boardlist, piece):
        count = []
        for i, x in enumerate(boardlist["A"]):
            if x == "e":
                count.append(["A", i])
        for i, x in enumerate(boardlist["B"]):
            if x == "e":
                count.append(["B", i])
        for i, x in enumerate(boardlist["C"]):
            if x == "e":
                count.append(["C", i])
        for i, x in enumerate(boardlist["D"]):
            if x == "e":
                count.append(["D", i])
        for i, x in enumerate(boardlist["E"]):
            if x == "e":
                count.append(["E", i])
                self.mplace("E", i, piece, boardlist)
                removelist = self.removeList(boardlist, piece, 1)
                if len(removelist) > 0:
                    for r in removelist:
                        count.append(["E", i, r[0], r[1]])
                self.mundoplace("E", i, boardlist)
        for i, x in enumerate(boardlist["F"]):
            if x == "e":
                count.append(["F", i])
                self.mplace("F", i, piece, boardlist)
                removelist = self.removeList(boardlist, piece, 1)
                if len(removelist) > 0:
                    for r in removelist:
                        count.append(["F", i, r[0], r[1]])
                self.mundoplace("F", i, boardlist)
        for i, x in enumerate(boardlist["G"]):
            if x == "e":
                count.append(["G", i])
                self.mplace("G", i, piece, boardlist)
                removelist = self.removeList(boardlist, piece, 1)
                if len(removelist) > 0:
                    for r in removelist:
                        count.append(["G", i, r[0], r[1]])
                self.mundoplace("G", i, boardlist)
        for i, x in enumerate(boardlist["H"]):
            if x == "e":
                count.append(["H", i])
                self.mplace("H", i, piece, boardlist)
                removelist = self.removeList(boardlist, piece, 2)
                if len(removelist) > 0:
                    for r in removelist:
                        count.append(["H", i, r[0], r[1]])
                self.mundoplace("H", i, boardlist)
        for i, x in enumerate(boardlist["I"]):
            if x == "e":
                count.append(["I", i])
                self.mplace("I", i, piece, boardlist)
                removelist = self.removeList(boardlist, piece, 2)
                if len(removelist) > 0:
                    for r in removelist:
                        count.append(["I", i, r[0], r[1]])
                self.mundoplace("I", i, boardlist)
        for i, x in enumerate(boardlist["J"]):
            if x == "e":
                count.append(["J", i])
        return count

    # Generates  possible remove list based on game state
    # stores the moves in a list, count
    # @Returns count
    def removeList(self, boardlist, piece, level):
        count = []
        if level >= 1:
            for i, x in enumerate(boardlist["A"]):
                if x == piece and self.mcanremove("A", i, boardlist):
                    count.append(["A", i])
            for i, x in enumerate(boardlist["B"]):
                if x == piece and self.mcanremove("B", i, boardlist):
                    count.append(["B", i])
            for i, x in enumerate(boardlist["C"]):
                if x == piece and self.mcanremove("C", i, boardlist):
                    count.append(["C", i])
            for i, x in enumerate(boardlist["D"]):
                if x == piece and self.mcanremove("D", i, boardlist):
                    count.append(["D", i])
        if level >= 2:
            for i, x in enumerate(boardlist["E"]):
                if x == piece and self.mcanremove("E", i, boardlist):
                    count.append(["E", i])
            for i, x in enumerate(boardlist["F"]):
                if x == piece and self.mcanremove("F", i, boardlist):
                    count.append(["F", i])
            for i, x in enumerate(boardlist["G"]):
                if x == piece and self.mcanremove("G", i, boardlist):
                    count.append(["G", i])
        if level >= 3:
            for i, x in enumerate(boardlist["H"]):
                if x == piece:
                    count.append(["H", i])
            for i, x in enumerate(boardlist["I"]):
                if x == piece:
                    count.append(["I", i])
        return count

    # Places piece on position
    # @returns True if successful
    # @returns False if otherwise
    def mplace(self, letter, position, piece, boardlist):
        try:
            if boardlist[letter][position] == "e":
                boardlist[letter][position] = piece
                self.mboard_update(boardlist)
                return True
            else:
                return False
        except:
            return False

    # Removes a piece from its position (Undos a place)
    # @returns True if successful
    # @returns Flase if otherwise
    def mundoplace(self, letter, position, boardlist):
            if boardlist[letter][position] in ("w", "b"):
                boardlist[letter][position] = "e"
                self.mboard_update(boardlist)
                return True
            else:
                return False

    # Updates the board by unlocking positions if bottom positions are filled
    def mboard_update(self, boardlist):
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
        # Unseals E[0]
        if boardlist["E"][0] == "s":
            boardlist["E"][0] = "e"
        for v, w in boardlist["A"][:2], boardlist["B"][:2]:
            if v == "e" or w == "e" or v == "s" or w == "s":
                boardlist["E"][0] = "s"
        # Unseals E[1]
        if boardlist["E"][1] == "s":
            boardlist["E"][1] = "e"
        for v, w in boardlist["A"][1:3], boardlist["B"][1:3]:
            if v == "e" or w == "e" or v == "s" or w == "s":
                boardlist["E"][1] = "s"
        # Unseals E[2]
        if boardlist["E"][2] == "s":
            boardlist["E"][2] = "e"
        for v, w in boardlist["A"][2:4], boardlist["B"][2:4]:
            if v == "e" or w == "e" or v == "s" or w == "s":
                boardlist["E"][2] = "s"
        # Unseals F[0]
        if boardlist["F"][0] == "s":
            boardlist["F"][0] = "e"
        for v, w in boardlist["B"][:2], boardlist["C"][:2]:
            if v == "e" or w == "e" or v == "s" or w == "s":
                boardlist["F"][0] = "s"
        # Unseals F[1]
        if boardlist["F"][1] == "s":
            boardlist["F"][1] = "e"
        for v, w in boardlist["B"][1:3], boardlist["C"][1:3]:
            if v == "e" or w == "e" or v == "s" or w == "s":
                boardlist["F"][1] = "s"
        # Unseals F[2]
        if boardlist["F"][2] == "s":
            boardlist["F"][2] = "e"
        for v, w in boardlist["B"][2:4], boardlist["C"][2:4]:
            if v == "e" or w == "e" or v == "s" or w == "s":
                boardlist["F"][2] = "s"
        # Unseals G[0]
        if boardlist["G"][0] == "s":
            boardlist["G"][0] = "e"
        for v, w in boardlist["C"][:2], boardlist["D"][:2]:
            if v == "e" or w == "e" or v == "s" or w == "s":
                boardlist["G"][0] = "s"
        # Unseals G[1]
        if boardlist["G"][1] == "s":
            boardlist["G"][1] = "e"
        for v, w in boardlist["C"][1:3], boardlist["D"][1:3]:
            if v == "e" or w == "e" or v == "s" or w == "s":
                boardlist["G"][1] = "s"
        # Unseals G[2]
        if boardlist["G"][2] == "s":
            boardlist["G"][2] = "e"
        for v, w in boardlist["C"][2:4], boardlist["D"][2:4]:
            if v == "e" or w == "e" or v == "s" or w == "s":
                boardlist["G"][2] = "s"

    # Checks if a piece needs to be removed
    # @Returns True if a piece needs to be removed
    # @Returns False if otherwise
    def mrcheck(self, letter, position, boardlist):
        if boardlist[letter][position] != "s" and boardlist[letter][position] != "e":
            # Level 0
            if letter in ("A", "B", "C", "D"):
                if boardlist["A"][position] == boardlist["B"][position] == boardlist["C"][position] == boardlist["D"][position]:
                    return True
                if boardlist[letter][0] == boardlist[letter][1] == boardlist[letter][2] == boardlist[letter][3]:
                    return True
                if letter == "A":
                    if position == 0:
                        if boardlist["A"][0] == boardlist["A"][1] == boardlist["B"][0] == boardlist["B"][1]:
                            return True
                    if position == 1:
                        if boardlist["A"][0] == boardlist["A"][1] == boardlist["B"][0] == boardlist["B"][1]:
                            return True
                        if boardlist["A"][1] == boardlist["A"][2] == boardlist["B"][1] == boardlist["B"][2]:
                            return True
                    if position == 2:
                        if boardlist["A"][2] == boardlist["A"][3] == boardlist["B"][2] == boardlist["B"][3]:
                            return True
                        if boardlist["A"][1] == boardlist["A"][2] == boardlist["B"][1] == boardlist["B"][2]:
                            return True
                    if position == 3:
                        if boardlist["A"][2] == boardlist["A"][3] == boardlist["B"][2] == boardlist["B"][3]:
                            return True
                if letter == "B":
                    if position == 0:
                        if boardlist["B"][0] == boardlist["B"][1] == boardlist["A"][0] == boardlist["A"][1]:
                            return True
                        if boardlist["B"][0] == boardlist["B"][1] == boardlist["C"][0] == boardlist["C"][1]:
                            return True
                    if position == 1:
                        if boardlist["B"][0] == boardlist["B"][1] == boardlist["A"][0] == boardlist["A"][1]:
                            return True
                        if boardlist["B"][0] == boardlist["B"][1] == boardlist["C"][0] == boardlist["C"][1]:
                            return True
                        if boardlist["B"][1] == boardlist["A"][1] == boardlist["B"][2] == boardlist["A"][2]:
                            return True
                        if boardlist["B"][1] == boardlist["C"][1] == boardlist["B"][2] == boardlist["C"][2]:
                            return True
                    if position == 2:
                        if boardlist["B"][1] == boardlist["A"][1] == boardlist["B"][2] == boardlist["A"][2]:
                            return True
                        if boardlist["B"][1] == boardlist["C"][1] == boardlist["B"][2] == boardlist["C"][2]:
                            return True
                        if boardlist["B"][2] == boardlist["A"][2] == boardlist["B"][3] == boardlist["A"][3]:
                            return True
                        if boardlist["B"][2] == boardlist["C"][2] == boardlist["B"][3] == boardlist["C"][3]:
                            return True
                    if position == 3:
                        if boardlist["B"][2] == boardlist["A"][2] == boardlist["B"][3] == boardlist["A"][3]:
                            return True
                        if boardlist["B"][2] == boardlist["C"][2] == boardlist["B"][3] == boardlist["C"][3]:
                            return True
                if letter == "C":
                    if position == 0:
                        if boardlist["C"][0] == boardlist["B"][0] == boardlist["B"][1] == boardlist["C"][1]:
                            return True
                        if boardlist["C"][0] == boardlist["D"][0] == boardlist["D"][1] == boardlist["C"][1]:
                            return True
                    if position == 1:
                        if boardlist["C"][0] == boardlist["B"][0] == boardlist["B"][1] == boardlist["C"][1]:
                            return True
                        if boardlist["C"][0] == boardlist["D"][0] == boardlist["D"][1] == boardlist["C"][1]:
                            return True
                        if boardlist["C"][1] == boardlist["B"][1] == boardlist["B"][2] == boardlist["C"][2]:
                            return True
                        if boardlist["C"][1] == boardlist["C"][2] == boardlist["D"][1] == boardlist["D"][2]:
                            return True
                    if position == 2:
                        if boardlist["C"][1] == boardlist["B"][1] == boardlist["B"][2] == boardlist["C"][2]:
                            return True
                        if boardlist["C"][1] == boardlist["C"][2] == boardlist["D"][1] == boardlist["D"][2]:
                            return True
                        if boardlist["C"][2] == boardlist["B"][2] == boardlist["B"][2] == boardlist["C"][3]:
                            return True
                        if boardlist["C"][2] == boardlist["C"][3] == boardlist["D"][3] == boardlist["D"][2]:
                            return True
                    if position == 3:
                        if boardlist["C"][2] == boardlist["B"][2] == boardlist["B"][3] == boardlist["C"][3]:
                            return True
                        if boardlist["C"][2] == boardlist["C"][3] == boardlist["D"][3] == boardlist["D"][2]:
                            return True
                if letter == "D":
                    if position == 0:
                        if boardlist["D"][0] == boardlist["C"][0] == boardlist["C"][1] == boardlist["D"][1]:
                            return True
                    if position == 1:
                        if boardlist["D"][0] == boardlist["C"][0] == boardlist["C"][1] == boardlist["D"][1]:
                            return True
                        if boardlist["D"][1] == boardlist["C"][1] == boardlist["C"][2] == boardlist["D"][2]:
                            return True
                    if position == 2:
                        if boardlist["D"][1] == boardlist["C"][1] == boardlist["C"][2] == boardlist["D"][2]:
                            return True
                        if boardlist["D"][2] == boardlist["C"][2] == boardlist["C"][3] == boardlist["D"][3]:
                            return True
                    if position == 3:
                        if boardlist["D"][2] == boardlist["C"][2] == boardlist["C"][3] == boardlist["D"][3]:
                            return True
            # Level 1
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
            # Level 2
            if letter in ("H", "I"):
                if boardlist["H"][0] == boardlist["H"][1] == boardlist["I"][0] == boardlist["I"][1]:
                    return True
            return False
        return False

    # Checks if a position can be removed based on if any piece is on top of it
    # @Returns True if no piece stands on top of the position
    # @Returns False if a piece is stacked on top of the position
    def mcanremove(self, letter, position, boardlist):
        if letter == "A":
            if position == 0:
                if boardlist["E"][0] in ("s", "e"):
                    return True
            if position == 1:
                if boardlist["E"][0] in ("s", "e") and boardlist["E"][1] in ("s", "e"):
                    return True
            if position == 2:
                if boardlist["E"][1] in ("s", "e") and boardlist["E"][2] in ("s", "e"):
                    return True
            if position == 3:
                if boardlist["E"][2] in ("s", "e"):
                    return True
        elif letter == "B":
            if position == 0:
                if boardlist["E"][0] in ("s", "e") and boardlist["F"][0] in ("s", "e"):
                    return True
            if position == 1:
                if boardlist["E"][0] in ("s", "e") and boardlist["F"][0] in ("s", "e") and boardlist["E"][1] in ("s", "e") and boardlist["F"][1] in ("s", "e"):
                    return True
            if position == 2:
                if boardlist["E"][1] in ("s", "e") and boardlist["F"][1] in ("s", "e") and boardlist["E"][2] in ("s", "e") and boardlist["F"][2] in ("s", "e"):
                    return True
            if position == 3:
                if boardlist["E"][2] in ("s", "e") and boardlist["F"][2] in ("s", "e"):
                    return True
        elif letter == "C":
            if position == 0:
                if boardlist["F"][0] in ("s", "e") and boardlist["G"][0] in ("s", "e"):
                    return True
            if position == 1:
                if boardlist["F"][0] in ("s", "e") and boardlist["G"][0] in ("s", "e") and boardlist["F"][1] in ("s", "e") and boardlist["G"][1] in ("s", "e"):
                    return True
            if position == 2:
                if boardlist["F"][1] in ("s", "e") and boardlist["F"][2] in ("s", "e") and boardlist["G"][1] in ("s", "e") and boardlist["G"][2] in ("s", "e"):
                    return True
            if position == 3:
                if boardlist["F"][2] in ("s", "e") and boardlist["G"][2] in ("s", "e"):
                    return True
        elif letter == "D":
            if position == 0:
                if boardlist["G"][0] in ("s", "e"):
                    return True
            if position == 1:
                if boardlist["G"][0] in ("s", "e") and  boardlist["G"][1] in ("s", "e"):
                    return True
            if position == 2:
                if boardlist["G"][1] in ("s", "e") and  boardlist["G"][2] in ("s", "e"):
                    return True
            if position == 3:
                if boardlist["G"][2] in ("s", "e"):
                    return True
        elif letter == "E":
            if position == 0:
                if boardlist["H"][0] in ("s", "e"):
                    return True
            if position == 1:
                if boardlist["H"][0] in ("s", "e") and boardlist["H"][1] in ("s", "e"):
                    return True
            if position == 2:
                if boardlist["H"][1] in ("s", "e"):
                    return True
        elif letter == "F":
            if position == 0:
                if boardlist["H"][0] in ("s", "e") and boardlist["I"][0] in ("s", "e"):
                    return True
            if position == 1:
                if boardlist["H"][0] in ("s", "e") and boardlist["H"][1] in ("s", "e") and boardlist["I"][0] in ("s", "e") and boardlist["I"][1] in ("s", "e"):
                    return True
            if position == 2:
                if boardlist["H"][1] in ("s", "e") and boardlist["I"][1] in ("s", "e"):
                    return True
        elif letter == "G":
            if position == 0:
                if boardlist["I"][0] in ("s", "e"):
                    return True
            if position == 1:
                if boardlist["I"][0] in ("s", "e") and boardlist["I"][1] in ("s", "e"):
                    return True
            if position == 2:
                if boardlist["I"][1] in ("s", "e"):
                    return True
        elif letter in ("H", "I"):
            return True
        return False

    # Evaluation function
    # Evaluates based on after placing the piece down
    # @Returns the score of evaluation
    def evaluate(self, boardlist, letter, position, mypiece, mynumber, theirpiece, theirnumber):
        piecepoint = 140
        point = 60
        removepoint = 20
        score = (mynumber - theirnumber) * piecepoint
        if boardlist["J"][0] == mypiece:
            score = math.inf
            return score
        elif boardlist["J"][0] == theirpiece:
            score = -math.inf
            return score
        if boardlist[letter][position] == mypiece:
            if letter in ("B", "C"):
                score += 10
                if position in (1, 2):
                    score += 10
            elif position in ("E", "F", "G"):
                if position == 1:
                    score += 10
                if letter == "F":
                    score += 10
            if self.mrcheck(letter, position, boardlist):
                score += 130
        elif boardlist[letter][position] == theirpiece:
            if letter in ("B", "C"):
                score -= 10
                if position in (1, 2):
                    score -= 10
            if self.mrcheck(letter, position, boardlist):
                score -= 130

        for l in range(9):
            lett = "A"
            lett = chr(ord(lett) + l)
            for i, x in enumerate(boardlist[lett]):
                if x == "e":
                    self.mplace(lett, i, mypiece, boardlist)
                    if self.mrcheck(lett, i, boardlist):
                        score += point
                    self.mundoplace(lett, i, boardlist)
                    self.mplace(lett, i, theirpiece, boardlist)
                    if self.mrcheck(lett, i, boardlist):
                        score -= point
                    self.mundoplace(lett, i, boardlist)
                elif x != "s":
                    if self.mcanremove(lett, i, boardlist):
                        if x == mypiece:
                            score += removepoint
                        else:
                            score -= removepoint

        return score

    def move(self, boardlist, mynumber, theirnumber, mypiece, theirpiece, flag):
        myboardlist = copy.deepcopy(boardlist)
        t0 = time.time()
        #check = self.minimax(myboardlist, 0, mypiece, mynumber, theirpiece, theirnumber, 2, flag)
        check = self.alphabeta(-math.inf, math.inf, myboardlist, 0, mypiece, mynumber, theirpiece, theirnumber, 3, flag)
        t1 = time.time()
        print("AI player chooses:", end=" ")
        print(check[1])
        print("AI used: ", end="")
        print(t1 - t0, end="")
        print(" seconds")
        return check[1]

#######################################
############ Class: AI-2 ##############
#######################################
class Artificial2(Player):

    # Minimax for finding the best next move
    # @Returns the score and move
    def minimax(self, boardlist, side, mypiece, mynumber, theirpiece, theirnumber, depth, flag):
        best = [None, None]
        #---------------------------------------------------PLACING OR RASING A STONE---------------------------------------------------#
        if flag == 0:  # normal moves or raise
            if depth == 0:  # last move been searched
                if side == 0:  # my turn
                    movelist = self.moveList(boardlist, mypiece)
                    best = [-math.inf, ["F",0]]
                    for i in movelist:
                        if len(i) == 2:  # if its just a simple place and not a raise
                            self.mplace(i[0], i[1], mypiece, boardlist)  # place the piece
                            myscore = self.evaluate(boardlist, i[0], i[1], mypiece, mynumber-1, theirpiece, theirnumber)  # evaluate the score of the current board state
                            self.mundoplace(i[0], i[1], boardlist)
                        else:  # len(i) == 4 if its a raise
                            self.mplace(i[0], i[1], mypiece, boardlist)  # place the piece first
                            self.mundoplace(i[2], i[3], boardlist)  # then remove the piece
                            myscore = self.evaluate(boardlist, i[0], i[1], mypiece, mynumber-1, theirpiece, theirnumber)  # evaluate the score of the current board state
                            self.mundoplace(i[0], i[1], boardlist)
                            self.mplace(i[2], i[3], mypiece, boardlist)
                        if myscore >= best[0]:  # see if myscore exceeds best score so far
                            best[0] = myscore
                            best[1] = i
                    return best  # return the best score and move
                else:  # if side == 1, ie their turn
                    movelist = self.moveList(boardlist, theirpiece)
                    best = [math.inf, ["F", 0]]
                    for i in movelist:
                        if len(i) == 2:  # if its just a simple place and not a raise
                            self.mplace(i[0], i[1], theirpiece, boardlist)
                            myscore = self.evaluate(boardlist, i[0], i[1], mypiece, mynumber, theirpiece, theirnumber-1)  # evaluate the score of the current board state
                            self.mundoplace(i[0], i[1], boardlist)
                        else:  # len(i) == 4 if its a raise
                            self.mplace(i[0], i[1], theirpiece, boardlist)  # place their piece
                            self.mundoplace(i[2], i[3], boardlist)  # remove that piece thus making a raise
                            myscore = self.evaluate(boardlist, i[0], i[1], mypiece, mynumber, theirpiece, theirnumber-1)  # evaluate the score of the current board state
                            self.mundoplace(i[0], i[1], boardlist)
                            self.mplace(i[2], i[3], theirpiece, boardlist)
                        if myscore <= best[0]:  # see if myscore is smaller than the best score so far
                            best[0] = myscore
                            best[1] = i
                    return best

            else:  # if depth != 0, ie not last move
                if side == 0:  # my turn
                    movelist = self.moveList(boardlist, mypiece)
                    best = [-math.inf, ["F",0]]
                    for i in movelist:
                        if len(i) == 2:  # if its just a simple place and not a raise
                            self.mplace(i[0], i[1], mypiece, boardlist)  # place the piece
                            if self.mrcheck(i[0], i[1], boardlist):
                                myscore = self.minimax(boardlist, 0, mypiece, mynumber-1, theirpiece, theirnumber, depth-1, 1)[0]
                            else:
                                myscore = self.minimax(boardlist, 1, mypiece, mynumber-1, theirpiece, theirnumber, depth-1, 0)[0]
                            self.mundoplace(i[0], i[1], boardlist)
                        else:  # len(i) == 4 if its a raise
                            self.mplace(i[0], i[1], mypiece, boardlist)  # place the piece first
                            self.mundoplace(i[2], i[3], boardlist)  # then remove the piece
                            if self.mrcheck(i[0], i[1], boardlist):
                                myscore = self.minimax(boardlist, 0, mypiece, mynumber, theirpiece, theirnumber, depth-1, 1)[0]
                            else:
                                myscore = self.minimax(boardlist, 1, mypiece, mynumber, theirpiece, theirnumber, depth-1, 0)[0]
                            self.mundoplace(i[0], i[1], boardlist)
                            self.mplace(i[2], i[3], mypiece, boardlist)
                        if myscore >= best[0]:  # see if myscore exceeds best score so far
                            best[0] = myscore
                            best[1] = i
                    return best  # return the best score and move
                else:  # if side == 1, ie their turn
                    movelist = self.moveList(boardlist, theirpiece)
                    best = [math.inf, ["F", 0]]
                    for i in movelist:
                        if len(i) == 2:  # if its just a simple place and not a raise
                            self.mplace(i[0], i[1], theirpiece, boardlist)
                            if self.mrcheck(i[0], i[1], boardlist):
                                myscore = self.minimax(boardlist, 1, mypiece, mynumber, theirpiece, theirnumber-1, depth-1, 1)[0]
                            else:
                                myscore = self.minimax(boardlist, 0, mypiece, mynumber, theirpiece, theirnumber-1, depth-1, 0)[0]
                            self.mundoplace(i[0], i[1], boardlist)
                        else:  # len(i) == 4 if its a raise
                            self.mplace(i[0], i[1], theirpiece, boardlist)  # place their piece
                            self.mundoplace(i[2], i[3], boardlist)  # remove that piece thus making a raise
                            if self.mrcheck(i[0], i[1], boardlist):
                                myscore = self.minimax(boardlist, 1, mypiece, mynumber, theirpiece, theirnumber, depth-1, 1)[0]
                            else:
                                myscore = self.minimax(boardlist, 0, mypiece, mynumber, theirpiece, theirnumber, depth-1, 0)[0]
                            self.mundoplace(i[0], i[1], boardlist)
                            self.mplace(i[2], i[3], theirpiece, boardlist)
                        if myscore <= best[0]:  # see if myscore is smaller than the best score so far
                            best[0] = myscore
                            best[1] = i
                    return best
        #---------------------------------------------------COMPULSORY REMOVES---------------------------------------------------#
        elif flag == 1:  # for must removes
            if depth == 0:  # last move been searched
                if side == 0:  # if its my turn
                    movelist = self.removeList(boardlist, mypiece, 3)  # get a list of all the positions i can remove from
                    best = [-math.inf, ["E", 0]]
                    for i in movelist:
                        self.mundoplace(i[0], i[1], boardlist)
                        myscore = self.evaluate(boardlist, i[0], i[1], mypiece, mynumber+1, theirpiece, theirnumber)
                        self.mplace(i[0], i[1], mypiece, boardlist)
                        if myscore >= best[0]:
                            best[0] = myscore
                            best[1] = i
                    return best
                else:  # if side == 1, ie their turn
                    movelist = self.removeList(boardlist, theirpiece, 3)
                    best = [math.inf, ["E", 0]]
                    for i in movelist:
                        self.mundoplace(i[0], i[1], boardlist)
                        myscore = self.evaluate(boardlist, i[0], i[1], mypiece, mynumber, theirpiece, theirnumber+1)
                        self.mplace(i[0], i[1], theirpiece, boardlist)
                        if myscore <= best[0]:
                            best[0] = myscore
                            best[1] = i
                    return best

            else:  # if depth != 0, ie not the last move been searched
                if side == 0:  # if its my turn
                    movelist = self.removeList(boardlist, mypiece, 3)  # get a list of all the positions i can remove from
                    best = [-math.inf, ["E", 0]]
                    for i in movelist:
                        self.mundoplace(i[0], i[1], boardlist)
                        myscore = self.minimax(boardlist, 0, mypiece, mynumber+1, theirpiece, theirnumber, depth-1, 2)[0]
                        self.mplace(i[0], i[1], mypiece, boardlist)
                        if myscore >= best[0]:
                            best[0] = myscore
                            best[1] = i
                    return best
                else:  # if side == 1, ie their turn
                    movelist = self.removeList(boardlist, theirpiece, 3)
                    best = [math.inf, ["E", 0]]
                    for i in movelist:
                        self.mundoplace(i[0], i[1], boardlist)
                        myscore = self.minimax(boardlist, 1, mypiece, mynumber, theirpiece, theirnumber+1, depth-1, 2)[0]
                        self.mplace(i[0], i[1], theirpiece, boardlist)
                        if myscore <= best[0]:
                            best[0] = myscore
                            best[1] = i
                    return best
        #---------------------------------------------------OPTIONAL REMOVES---------------------------------------------------#
        else:  # flag == 2, for optional removes
            if depth == 0:  # last move been searched
                if side == 0:  # if its my turn
                    movelist = self.removeList(boardlist, mypiece, 3)  # get a list of all the positions i can remove from
                    movelist.append("_")
                    best = [-math.inf, ["E", 0]]
                    for i in movelist:
                        if i == "_":
                            myscore = self.evaluate(boardlist, "Z", 0, mypiece, mynumber, theirpiece, theirnumber)
                        else:
                            self.mundoplace(i[0], i[1], boardlist)
                            myscore = self.evaluate(boardlist, i[0], i[1], mypiece, mynumber+1, theirpiece, theirnumber)
                            self.mplace(i[0], i[1], mypiece, boardlist)
                        if myscore >= best[0]:
                            best[0] = myscore
                            best[1] = i
                    return best
                else:  # if side == 1, ie their turn
                    movelist = self.removeList(boardlist, theirpiece, 3)
                    moevlist.append("_")
                    best = [math.inf, ["E", 0]]
                    for i in movelist:
                        if i == "_":
                            myscore = self.evaluate(boardlist, "Z", 0, mypiece, mynumber, theirpiece, theirnumber)
                        else:
                            self.mundoplace(i[0], i[1], boardlist)
                            myscore = self.evaluate(boardlist, i[0], i[1], mypiece, mynumber, theirpiece, theirnumber+1)
                            self.mplace(i[0], i[1], theirpiece, boardlist)
                        if myscore <= best[0]:
                            best[0] = myscore
                            best[1] = i
                    return best

            else:  # if depth != 0, ie not the last move been searched
                if side == 0:  # if its my turn
                    movelist = self.removeList(boardlist, mypiece, 3)  # get a list of all the positions i can remove from
                    movelist.append("_")
                    best = [-math.inf, ["E", 0]]
                    for i in movelist:
                        if i == "_":
                            myscore = self.minimax(boardlist, 1, mypiece, mynumber, theirpiece, theirnumber, depth-1, 0)[0]
                        else:
                            self.mundoplace(i[0], i[1], boardlist)
                            myscore = self.minimax(boardlist, 1, mypiece, mynumber+1, theirpiece, theirnumber, depth-1, 0)[0]
                            self.mplace(i[0], i[1], mypiece, boardlist)
                        if myscore >= best[0]:
                            best[0] = myscore
                            best[1] = i
                    return best
                else:  # if side == 1, ie their turn
                    movelist = self.removeList(boardlist, theirpiece, 3)
                    movelist.append("_")
                    best = [math.inf, ["E", 0]]
                    for i in movelist:
                        if i == "_":
                            myscore = self.minimax(boardlist, 0, mypiece, mynumber, theirpiece, theirnumber, depth-1, 0)[0]
                        else:
                            self.mundoplace(i[0], i[1], boardlist)
                            myscore = self.minimax(boardlist, 0, mypiece, mynumber, theirpiece, theirnumber+1, depth-1, 0)[0]
                            self.mplace(i[0], i[1], theirpiece, boardlist)
                        if myscore <= best[0]:
                            best[0] = myscore
                            best[1] = i
                    return best

    # Improved version of minimax - alphabeta
    # @Returns the score and move
    def alphabeta(self, alphavalue, betavalue, boardlist, side, mypiece, mynumber, theirpiece, theirnumber, depth, flag):
        best = [None, None]
        alpha = alphavalue
        beta = betavalue
        #---------------------------------------------------PLACING OR RASING A STONE---------------------------------------------------#
        if flag == 0:  # normal moves or raise
            #----------------------------------DEPTH 0----------------------------------#
            if depth == 0:  # last move been searched
                if side == 0:  # my turn
                    movelist = self.moveList(boardlist, mypiece)
                    best = [-math.inf, ["F", 0]]
                    for i in movelist:
                        if best[0] >= beta:
                            break
                        elif best[0] < beta:
                            if len(i) == 2:  # if its just a simple place and not a raise
                                self.mplace(i[0], i[1], mypiece, boardlist)  # place the piece
                                myscore = self.evaluate(boardlist, i[0], i[1], mypiece, mynumber-1, theirpiece, theirnumber)  # evaluate the score of the current board state
                                self.mundoplace(i[0], i[1], boardlist)
                            else:  # len(i) == 4 if its a raise
                                self.mplace(i[0], i[1], mypiece, boardlist)  # place the piece first
                                self.mundoplace(i[2], i[3], boardlist)  # then remove the piece
                                myscore = self.evaluate(boardlist, i[0], i[1], mypiece, mynumber-1, theirpiece, theirnumber)  # evaluate the score of the current board state
                                self.mundoplace(i[0], i[1], boardlist)
                                self.mplace(i[2], i[3], mypiece, boardlist)
                            if myscore >= best[0]:  # see if myscore exceeds best score so far
                                best[0] = myscore
                                best[1] = i
                    return best  # return the best score and move
                else:  # if side == 1, ie their turn
                    movelist = self.moveList(boardlist, theirpiece)
                    best = [math.inf, ["F", 0]]
                    for i in movelist:
                        if best[0] <= alpha:
                            break
                        elif best[0] > alpha:
                            if len(i) == 2:  # if its just a simple place and not a raise
                                self.mplace(i[0], i[1], theirpiece, boardlist)
                                myscore = self.evaluate(boardlist, i[0], i[1], mypiece, mynumber, theirpiece, theirnumber-1)  # evaluate the score of the current board state
                                self.mundoplace(i[0], i[1], boardlist)
                            else:  # len(i) == 4 if its a raise
                                self.mplace(i[0], i[1], theirpiece, boardlist)  # place their piece
                                self.mundoplace(i[2], i[3], boardlist)  # remove that piece thus making a raise
                                myscore = self.evaluate(boardlist, i[0], i[1], mypiece, mynumber, theirpiece, theirnumber-1)  # evaluate the score of the current board state
                                self.mundoplace(i[0], i[1], boardlist)
                                self.mplace(i[2], i[3], theirpiece, boardlist)
                            if myscore <= best[0]:  # see if myscore is smaller than the best score so far
                                best[0] = myscore
                                best[1] = i
                    return best
            #----------------------------------NOT DEPTH 0----------------------------------#
            else:  # if depth != 0, ie not last move
                if side == 0:  # my turn
                    movelist = self.moveList(boardlist, mypiece)
                    best = [-math.inf, ["F", 0]]
                    for i in movelist:
                        if best[0] >= beta:
                            break
                        elif best[0] < beta:
                            if len(i) == 2:  # if its just a simple place and not a raise
                                self.mplace(i[0], i[1], mypiece, boardlist)  # place the piece
                                if self.mrcheck(i[0], i[1], boardlist):
                                    myscore = self.alphabeta(alpha, beta, boardlist, 0, mypiece, mynumber-1, theirpiece, theirnumber, depth-1, 1)[0]
                                else:
                                    myscore = self.alphabeta(alpha, beta, boardlist, 1, mypiece, mynumber-1, theirpiece, theirnumber, depth-1, 0)[0]
                                self.mundoplace(i[0], i[1], boardlist)
                            else:  # len(i) == 4 if its a raise
                                self.mplace(i[0], i[1], mypiece, boardlist)  # place the piece first
                                self.mundoplace(i[2], i[3], boardlist)  # then remove the piece
                                if self.mrcheck(i[0], i[1], boardlist):
                                    myscore = self.alphabeta(alpha, beta, boardlist, 0, mypiece, mynumber, theirpiece, theirnumber, depth-1, 1)[0]
                                else:
                                    myscore = self.alphabeta(alpha, beta, boardlist, 1, mypiece, mynumber, theirpiece, theirnumber, depth-1, 0)[0]
                                self.mundoplace(i[0], i[1], boardlist)
                                self.mplace(i[2], i[3], mypiece, boardlist)
                            if myscore >= best[0]:  # see if myscore exceeds best score so far
                                best[0] = myscore
                                best[1] = i
                                alpha = myscore
                    return best  # return the best score and move
                else:  # if side == 1, ie their turn
                    movelist = self.moveList(boardlist, theirpiece)
                    best = [math.inf, ["F", 0]]
                    for i in movelist:
                        if best[0] <= alpha:
                            break
                        elif best[0] > alpha:
                            if len(i) == 2:  # if its just a simple place and not a raise
                                self.mplace(i[0], i[1], theirpiece, boardlist)
                                if self.mrcheck(i[0], i[1], boardlist):
                                    myscore = self.alphabeta(alpha, beta, boardlist, 1, mypiece, mynumber, theirpiece, theirnumber-1, depth-1, 1)[0]
                                else:
                                    myscore = self.alphabeta(alpha, beta, boardlist, 0, mypiece, mynumber, theirpiece, theirnumber-1, depth-1, 0)[0]
                                self.mundoplace(i[0], i[1], boardlist)
                            else:  # len(i) == 4 if its a raise
                                self.mplace(i[0], i[1], theirpiece, boardlist)  # place their piece
                                self.mundoplace(i[2], i[3], boardlist)  # remove that piece thus making a raise
                                if self.mrcheck(i[0], i[1], boardlist):
                                    myscore = self.alphabeta(alpha, beta, boardlist, 1, mypiece, mynumber, theirpiece, theirnumber, depth-1, 1)[0]
                                else:
                                    myscore = self.alphabeta(alpha, beta, boardlist, 0, mypiece, mynumber, theirpiece, theirnumber, depth-1, 0)[0]
                                self.mundoplace(i[0], i[1], boardlist)
                                self.mplace(i[2], i[3], theirpiece, boardlist)
                            if myscore <= best[0]:  # see if myscore is smaller than the best score so far
                                best[0] = myscore
                                best[1] = i
                                beta = myscore
                    return best
        #---------------------------------------------------COMPULSORY REMOVES---------------------------------------------------#
        elif flag == 1:  # for must removes
            if depth == 0:  # last move been searched
                if side == 0:  # if its my turn
                    movelist = self.removeList(boardlist, mypiece, 3)  # get a list of all the positions i can remove from
                    best = [-math.inf, ["E", 0]]
                    for i in movelist:
                        if best[0] >= beta:
                            break
                        elif best[0] < beta:
                            self.mundoplace(i[0], i[1], boardlist)
                            myscore = self.evaluate(boardlist, i[0], i[1], mypiece, mynumber+1, theirpiece, theirnumber)
                            self.mplace(i[0], i[1], mypiece, boardlist)
                            if myscore >= best[0]:
                                best[0] = myscore
                                best[1] = i
                                alpha = myscore
                    return best
                else:  # if side == 1, ie their turn
                    movelist = self.removeList(boardlist, theirpiece, 3)
                    best = [math.inf, ["E", 0]]
                    for i in movelist:
                        if best[0] <= alpha:
                            break
                        elif best[0] > alpha:
                            self.mundoplace(i[0], i[1], boardlist)
                            myscore = self.evaluate(boardlist, i[0], i[1], mypiece, mynumber, theirpiece, theirnumber+1)
                            self.mplace(i[0], i[1], theirpiece, boardlist)
                            if myscore <= best[0]:
                                best[0] = myscore
                                best[1] = i
                                beta = myscore
                    return best

            else:  # if depth != 0, ie not the last move been searched
                if side == 0:  # if its my turn
                    movelist = self.removeList(boardlist, mypiece, 3)  # get a list of all the positions i can remove from
                    best = [-math.inf, ["E", 0]]
                    for i in movelist:
                        if best[0] >= beta:
                            break
                        elif best[0] < beta:
                            self.mundoplace(i[0], i[1], boardlist)
                            myscore = self.alphabeta(alpha, beta, boardlist, 0, mypiece, mynumber+1, theirpiece, theirnumber, depth-1, 2)[0]
                            self.mplace(i[0], i[1], mypiece, boardlist)
                            if myscore >= best[0]:
                                best[0] = myscore
                                best[1] = i
                                alpha = myscore
                    return best
                else:  # if side == 1, ie their turn
                    movelist = self.removeList(boardlist, theirpiece, 3)
                    best = [math.inf, ["E", 0]]
                    for i in movelist:
                        if best[0] <= alpha:
                            break
                        elif best[0] > alpha:
                            self.mundoplace(i[0], i[1], boardlist)
                            myscore = self.alphabeta(alpha, beta, boardlist, 1, mypiece, mynumber, theirpiece, theirnumber+1, depth-1, 2)[0]
                            self.mplace(i[0], i[1], theirpiece, boardlist)
                            if myscore <= best[0]:
                                best[0] = myscore
                                best[1] = i
                                beta = myscore
                    return best
        #---------------------------------------------------OPTIONAL REMOVES---------------------------------------------------#
        else:  # flag == 2, for optional removes
            if depth == 0:  # last move been searched
                if side == 0:  # if its my turn
                    movelist = self.removeList(boardlist, mypiece, 3)  # get a list of all the positions i can remove from
                    movelist.append("_")
                    best = [-math.inf, ["E", 0]]
                    for i in movelist:
                        if best[0] >= beta:
                            break
                        elif best[0] < beta:
                            if i == "_":
                                myscore = self.evaluate(boardlist, "Z", 0, mypiece, mynumber, theirpiece, theirnumber)
                            else:
                                self.mundoplace(i[0], i[1], boardlist)
                                myscore = self.evaluate(boardlist, i[0], i[1], mypiece, mynumber+1, theirpiece, theirnumber)
                                self.mplace(i[0], i[1], mypiece, boardlist)
                            if myscore >= best[0]:
                                best[0] = myscore
                                best[1] = i
                    return best
                else:  # if side == 1, ie their turn
                    movelist = self.removeList(boardlist, theirpiece, 3)
                    movelist.append("_")
                    best = [math.inf, ["E", 0]]
                    for i in movelist:
                        if best[0] <= alpha:
                            break
                        elif best[0] > alpha:
                            if i == "_":
                                myscore = self.evaluate(boardlist, "Z", 0, mypiece, mynumber, theirpiece, theirnumber)
                            else:
                                self.mundoplace(i[0], i[1], boardlist)
                                myscore = self.evaluate(boardlist, i[0], i[1], mypiece, mynumber, theirpiece, theirnumber+1)
                                self.mplace(i[0], i[1], theirpiece, boardlist)
                            if myscore <= best[0]:
                                best[0] = myscore
                                best[1] = i
                    return best

            else:  # if depth != 0, ie not the last move been searched
                if side == 0:  # if its my turn
                    movelist = self.removeList(boardlist, mypiece, 3)  # get a list of all the positions i can remove from
                    movelist.append("_")
                    best = [-math.inf, ["E", 0]]
                    for i in movelist:
                        if best[0] >= beta:
                            break
                        elif best[0] < beta:
                            if i == "_":
                                myscore = self.alphabeta(alpha, beta, boardlist, 1, mypiece, mynumber, theirpiece, theirnumber, depth-1, 0)[0]
                            else:
                                self.mundoplace(i[0], i[1], boardlist)
                                myscore = self.alphabeta(alpha, beta, boardlist, 1, mypiece, mynumber+1, theirpiece, theirnumber, depth-1, 0)[0]
                                self.mplace(i[0], i[1], mypiece, boardlist)
                            if myscore >= best[0]:
                                best[0] = myscore
                                best[1] = i
                                alpha = myscore
                    return best
                else:  # if side == 1, ie their turn
                    movelist = self.removeList(boardlist, theirpiece, 3)
                    movelist.append("_")
                    best = [math.inf, ["E", 0]]
                    for i in movelist:
                        if best[0] <= alpha:
                            break
                        elif best[0] > alpha:
                            if i == "_":
                                myscore = self.alphabeta(alpha, beta, boardlist, 0, mypiece, mynumber, theirpiece, theirnumber, depth-1, 0)[0]
                            else:
                                self.mundoplace(i[0], i[1], boardlist)
                                myscore = self.alphabeta(alpha, beta, boardlist, 0, mypiece, mynumber, theirpiece, theirnumber+1, depth-1, 0)[0]
                                self.mplace(i[0], i[1], theirpiece, boardlist)
                            if myscore <= best[0]:
                                best[0] = myscore
                                best[1] = i
                                beta = myscore
                    return best

    # Generates possible move list based on game state
    # stores the moves in a list, count
    # @Returns count
    def moveList(self, boardlist, piece):
        count = []
        for i, x in enumerate(boardlist["A"]):
            if x == "e":
                count.append(["A", i])
        for i, x in enumerate(boardlist["B"]):
            if x == "e":
                count.append(["B", i])
        for i, x in enumerate(boardlist["C"]):
            if x == "e":
                count.append(["C", i])
        for i, x in enumerate(boardlist["D"]):
            if x == "e":
                count.append(["D", i])
        for i, x in enumerate(boardlist["E"]):
            if x == "e":
                count.append(["E", i])
                self.mplace("E", i, piece, boardlist)
                removelist = self.removeList(boardlist, piece, 1)
                if len(removelist) > 0:
                    for r in removelist:
                        count.append(["E", i, r[0], r[1]])
                self.mundoplace("E", i, boardlist)
        for i, x in enumerate(boardlist["F"]):
            if x == "e":
                count.append(["F", i])
                self.mplace("F", i, piece, boardlist)
                removelist = self.removeList(boardlist, piece, 1)
                if len(removelist) > 0:
                    for r in removelist:
                        count.append(["F", i, r[0], r[1]])
                self.mundoplace("F", i, boardlist)
        for i, x in enumerate(boardlist["G"]):
            if x == "e":
                count.append(["G", i])
                self.mplace("G", i, piece, boardlist)
                removelist = self.removeList(boardlist, piece, 1)
                if len(removelist) > 0:
                    for r in removelist:
                        count.append(["G", i, r[0], r[1]])
                self.mundoplace("G", i, boardlist)
        for i, x in enumerate(boardlist["H"]):
            if x == "e":
                count.append(["H", i])
                self.mplace("H", i, piece, boardlist)
                removelist = self.removeList(boardlist, piece, 2)
                if len(removelist) > 0:
                    for r in removelist:
                        count.append(["H", i, r[0], r[1]])
                self.mundoplace("H", i, boardlist)
        for i, x in enumerate(boardlist["I"]):
            if x == "e":
                count.append(["I", i])
                self.mplace("I", i, piece, boardlist)
                removelist = self.removeList(boardlist, piece, 2)
                if len(removelist) > 0:
                    for r in removelist:
                        count.append(["I", i, r[0], r[1]])
                self.mundoplace("I", i, boardlist)
        for i, x in enumerate(boardlist["J"]):
            if x == "e":
                count.append(["J", i])
        return count

    # Generates  possible remove list based on game state
    # stores the moves in a list, count
    # @Returns count
    def removeList(self, boardlist, piece, level):
        count = []
        if level >= 1:
            for i, x in enumerate(boardlist["A"]):
                if x == piece and self.mcanremove("A", i, boardlist):
                    count.append(["A", i])
            for i, x in enumerate(boardlist["B"]):
                if x == piece and self.mcanremove("B", i, boardlist):
                    count.append(["B", i])
            for i, x in enumerate(boardlist["C"]):
                if x == piece and self.mcanremove("C", i, boardlist):
                    count.append(["C", i])
            for i, x in enumerate(boardlist["D"]):
                if x == piece and self.mcanremove("D", i, boardlist):
                    count.append(["D", i])
        if level >= 2:
            for i, x in enumerate(boardlist["E"]):
                if x == piece and self.mcanremove("E", i, boardlist):
                    count.append(["E", i])
            for i, x in enumerate(boardlist["F"]):
                if x == piece and self.mcanremove("F", i, boardlist):
                    count.append(["F", i])
            for i, x in enumerate(boardlist["G"]):
                if x == piece and self.mcanremove("G", i, boardlist):
                    count.append(["G", i])
        if level >= 3:
            for i, x in enumerate(boardlist["H"]):
                if x == piece:
                    count.append(["H", i])
            for i, x in enumerate(boardlist["I"]):
                if x == piece:
                    count.append(["I", i])
        return count

    # Places piece on position
    # @returns True if successful
    # @returns False if otherwise
    def mplace(self, letter, position, piece, boardlist):
        try:
            if boardlist[letter][position] == "e":
                boardlist[letter][position] = piece
                self.mboard_update(boardlist)
                return True
            else:
                return False
        except:
            return False

    # Removes a piece from its position (Undos a place)
    # @returns True if successful
    # @returns Flase if otherwise
    def mundoplace(self, letter, position, boardlist):
            if boardlist[letter][position] in ("w", "b"):
                boardlist[letter][position] = "e"
                self.mboard_update(boardlist)
                return True
            else:
                return False

    # Updates the board by unlocking positions if bottom positions are filled
    def mboard_update(self, boardlist):
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
        # Unseals E[0]
        if boardlist["E"][0] == "s":
            boardlist["E"][0] = "e"
        for v, w in boardlist["A"][:2], boardlist["B"][:2]:
            if v == "e" or w == "e" or v == "s" or w == "s":
                boardlist["E"][0] = "s"
        # Unseals E[1]
        if boardlist["E"][1] == "s":
            boardlist["E"][1] = "e"
        for v, w in boardlist["A"][1:3], boardlist["B"][1:3]:
            if v == "e" or w == "e" or v == "s" or w == "s":
                boardlist["E"][1] = "s"
        # Unseals E[2]
        if boardlist["E"][2] == "s":
            boardlist["E"][2] = "e"
        for v, w in boardlist["A"][2:4], boardlist["B"][2:4]:
            if v == "e" or w == "e" or v == "s" or w == "s":
                boardlist["E"][2] = "s"
        # Unseals F[0]
        if boardlist["F"][0] == "s":
            boardlist["F"][0] = "e"
        for v, w in boardlist["B"][:2], boardlist["C"][:2]:
            if v == "e" or w == "e" or v == "s" or w == "s":
                boardlist["F"][0] = "s"
        # Unseals F[1]
        if boardlist["F"][1] == "s":
            boardlist["F"][1] = "e"
        for v, w in boardlist["B"][1:3], boardlist["C"][1:3]:
            if v == "e" or w == "e" or v == "s" or w == "s":
                boardlist["F"][1] = "s"
        # Unseals F[2]
        if boardlist["F"][2] == "s":
            boardlist["F"][2] = "e"
        for v, w in boardlist["B"][2:4], boardlist["C"][2:4]:
            if v == "e" or w == "e" or v == "s" or w == "s":
                boardlist["F"][2] = "s"
        # Unseals G[0]
        if boardlist["G"][0] == "s":
            boardlist["G"][0] = "e"
        for v, w in boardlist["C"][:2], boardlist["D"][:2]:
            if v == "e" or w == "e" or v == "s" or w == "s":
                boardlist["G"][0] = "s"
        # Unseals G[1]
        if boardlist["G"][1] == "s":
            boardlist["G"][1] = "e"
        for v, w in boardlist["C"][1:3], boardlist["D"][1:3]:
            if v == "e" or w == "e" or v == "s" or w == "s":
                boardlist["G"][1] = "s"
        # Unseals G[2]
        if boardlist["G"][2] == "s":
            boardlist["G"][2] = "e"
        for v, w in boardlist["C"][2:4], boardlist["D"][2:4]:
            if v == "e" or w == "e" or v == "s" or w == "s":
                boardlist["G"][2] = "s"

    # Checks if a piece needs to be removed
    # @Returns True if a piece needs to be removed
    # @Returns False if otherwise
    def mrcheck(self, letter, position, boardlist):
        if boardlist[letter][position] != "s" and boardlist[letter][position] != "e":
            # Level 0
            if letter in ("A", "B", "C", "D"):
                if boardlist["A"][position] == boardlist["B"][position] == boardlist["C"][position] == boardlist["D"][position]:
                    return True
                if boardlist[letter][0] == boardlist[letter][1] == boardlist[letter][2] == boardlist[letter][3]:
                    return True
                if letter == "A":
                    if position == 0:
                        if boardlist["A"][0] == boardlist["A"][1] == boardlist["B"][0] == boardlist["B"][1]:
                            return True
                    if position == 1:
                        if boardlist["A"][0] == boardlist["A"][1] == boardlist["B"][0] == boardlist["B"][1]:
                            return True
                        if boardlist["A"][1] == boardlist["A"][2] == boardlist["B"][1] == boardlist["B"][2]:
                            return True
                    if position == 2:
                        if boardlist["A"][2] == boardlist["A"][3] == boardlist["B"][2] == boardlist["B"][3]:
                            return True
                        if boardlist["A"][1] == boardlist["A"][2] == boardlist["B"][1] == boardlist["B"][2]:
                            return True
                    if position == 3:
                        if boardlist["A"][2] == boardlist["A"][3] == boardlist["B"][2] == boardlist["B"][3]:
                            return True
                if letter == "B":
                    if position == 0:
                        if boardlist["B"][0] == boardlist["B"][1] == boardlist["A"][0] == boardlist["A"][1]:
                            return True
                        if boardlist["B"][0] == boardlist["B"][1] == boardlist["C"][0] == boardlist["C"][1]:
                            return True
                    if position == 1:
                        if boardlist["B"][0] == boardlist["B"][1] == boardlist["A"][0] == boardlist["A"][1]:
                            return True
                        if boardlist["B"][0] == boardlist["B"][1] == boardlist["C"][0] == boardlist["C"][1]:
                            return True
                        if boardlist["B"][1] == boardlist["A"][1] == boardlist["B"][2] == boardlist["A"][2]:
                            return True
                        if boardlist["B"][1] == boardlist["C"][1] == boardlist["B"][2] == boardlist["C"][2]:
                            return True
                    if position == 2:
                        if boardlist["B"][1] == boardlist["A"][1] == boardlist["B"][2] == boardlist["A"][2]:
                            return True
                        if boardlist["B"][1] == boardlist["C"][1] == boardlist["B"][2] == boardlist["C"][2]:
                            return True
                        if boardlist["B"][2] == boardlist["A"][2] == boardlist["B"][3] == boardlist["A"][3]:
                            return True
                        if boardlist["B"][2] == boardlist["C"][2] == boardlist["B"][3] == boardlist["C"][3]:
                            return True
                    if position == 3:
                        if boardlist["B"][2] == boardlist["A"][2] == boardlist["B"][3] == boardlist["A"][3]:
                            return True
                        if boardlist["B"][2] == boardlist["C"][2] == boardlist["B"][3] == boardlist["C"][3]:
                            return True
                if letter == "C":
                    if position == 0:
                        if boardlist["C"][0] == boardlist["B"][0] == boardlist["B"][1] == boardlist["C"][1]:
                            return True
                        if boardlist["C"][0] == boardlist["D"][0] == boardlist["D"][1] == boardlist["C"][1]:
                            return True
                    if position == 1:
                        if boardlist["C"][0] == boardlist["B"][0] == boardlist["B"][1] == boardlist["C"][1]:
                            return True
                        if boardlist["C"][0] == boardlist["D"][0] == boardlist["D"][1] == boardlist["C"][1]:
                            return True
                        if boardlist["C"][1] == boardlist["B"][1] == boardlist["B"][2] == boardlist["C"][2]:
                            return True
                        if boardlist["C"][1] == boardlist["C"][2] == boardlist["D"][1] == boardlist["D"][2]:
                            return True
                    if position == 2:
                        if boardlist["C"][1] == boardlist["B"][1] == boardlist["B"][2] == boardlist["C"][2]:
                            return True
                        if boardlist["C"][1] == boardlist["C"][2] == boardlist["D"][1] == boardlist["D"][2]:
                            return True
                        if boardlist["C"][2] == boardlist["B"][2] == boardlist["B"][2] == boardlist["C"][3]:
                            return True
                        if boardlist["C"][2] == boardlist["C"][3] == boardlist["D"][3] == boardlist["D"][2]:
                            return True
                    if position == 3:
                        if boardlist["C"][2] == boardlist["B"][2] == boardlist["B"][3] == boardlist["C"][3]:
                            return True
                        if boardlist["C"][2] == boardlist["C"][3] == boardlist["D"][3] == boardlist["D"][2]:
                            return True
                if letter == "D":
                    if position == 0:
                        if boardlist["D"][0] == boardlist["C"][0] == boardlist["C"][1] == boardlist["D"][1]:
                            return True
                    if position == 1:
                        if boardlist["D"][0] == boardlist["C"][0] == boardlist["C"][1] == boardlist["D"][1]:
                            return True
                        if boardlist["D"][1] == boardlist["C"][1] == boardlist["C"][2] == boardlist["D"][2]:
                            return True
                    if position == 2:
                        if boardlist["D"][1] == boardlist["C"][1] == boardlist["C"][2] == boardlist["D"][2]:
                            return True
                        if boardlist["D"][2] == boardlist["C"][2] == boardlist["C"][3] == boardlist["D"][3]:
                            return True
                    if position == 3:
                        if boardlist["D"][2] == boardlist["C"][2] == boardlist["C"][3] == boardlist["D"][3]:
                            return True
            # Level 1
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
            # Level 2
            if letter in ("H", "I"):
                if boardlist["H"][0] == boardlist["H"][1] == boardlist["I"][0] == boardlist["I"][1]:
                    return True
            return False
        return False

    # Checks if a position can be removed based on if any piece is on top of it
    # @Returns True if no piece stands on top of the position
    # @Returns False if a piece is stacked on top of the position
    def mcanremove(self, letter, position, boardlist):
        if letter == "A":
            if position == 0:
                if boardlist["E"][0] in ("s", "e"):
                    return True
            if position == 1:
                if boardlist["E"][0] in ("s", "e") and boardlist["E"][1] in ("s", "e"):
                    return True
            if position == 2:
                if boardlist["E"][1] in ("s", "e") and boardlist["E"][2] in ("s", "e"):
                    return True
            if position == 3:
                if boardlist["E"][2] in ("s", "e"):
                    return True
        elif letter == "B":
            if position == 0:
                if boardlist["E"][0] in ("s", "e") and boardlist["F"][0] in ("s", "e"):
                    return True
            if position == 1:
                if boardlist["E"][0] in ("s", "e") and boardlist["F"][0] in ("s", "e") and boardlist["E"][1] in ("s", "e") and boardlist["F"][1] in ("s", "e"):
                    return True
            if position == 2:
                if boardlist["E"][1] in ("s", "e") and boardlist["F"][1] in ("s", "e") and boardlist["E"][2] in ("s", "e") and boardlist["F"][2] in ("s", "e"):
                    return True
            if position == 3:
                if boardlist["E"][2] in ("s", "e") and boardlist["F"][2] in ("s", "e"):
                    return True
        elif letter == "C":
            if position == 0:
                if boardlist["F"][0] in ("s", "e") and boardlist["G"][0] in ("s", "e"):
                    return True
            if position == 1:
                if boardlist["F"][0] in ("s", "e") and boardlist["G"][0] in ("s", "e") and boardlist["F"][1] in ("s", "e") and boardlist["G"][1] in ("s", "e"):
                    return True
            if position == 2:
                if boardlist["F"][1] in ("s", "e") and boardlist["F"][2] in ("s", "e") and boardlist["G"][1] in ("s", "e") and boardlist["G"][2] in ("s", "e"):
                    return True
            if position == 3:
                if boardlist["F"][2] in ("s", "e") and boardlist["G"][2] in ("s", "e"):
                    return True
        elif letter == "D":
            if position == 0:
                if boardlist["G"][0] in ("s", "e"):
                    return True
            if position == 1:
                if boardlist["G"][0] in ("s", "e") and  boardlist["G"][1] in ("s", "e"):
                    return True
            if position == 2:
                if boardlist["G"][1] in ("s", "e") and  boardlist["G"][2] in ("s", "e"):
                    return True
            if position == 3:
                if boardlist["G"][2] in ("s", "e"):
                    return True
        elif letter == "E":
            if position == 0:
                if boardlist["H"][0] in ("s", "e"):
                    return True
            if position == 1:
                if boardlist["H"][0] in ("s", "e") and boardlist["H"][1] in ("s", "e"):
                    return True
            if position == 2:
                if boardlist["H"][1] in ("s", "e"):
                    return True
        elif letter == "F":
            if position == 0:
                if boardlist["H"][0] in ("s", "e") and boardlist["I"][0] in ("s", "e"):
                    return True
            if position == 1:
                if boardlist["H"][0] in ("s", "e") and boardlist["H"][1] in ("s", "e") and boardlist["I"][0] in ("s", "e") and boardlist["I"][1] in ("s", "e"):
                    return True
            if position == 2:
                if boardlist["H"][1] in ("s", "e") and boardlist["I"][1] in ("s", "e"):
                    return True
        elif letter == "G":
            if position == 0:
                if boardlist["I"][0] in ("s", "e"):
                    return True
            if position == 1:
                if boardlist["I"][0] in ("s", "e") and boardlist["I"][1] in ("s", "e"):
                    return True
            if position == 2:
                if boardlist["I"][1] in ("s", "e"):
                    return True
        elif letter in ("H", "I"):
            return True
        return False

    # Evaluation function
    # Evaluates based on after placing the piece down
    # @Returns the score of evaluation
    def evaluate(self, boardlist, letter, position, mypiece, mynumber, theirpiece, theirnumber):
        piecepoint = 140
        point = 60
        removepoint = 20
        score = (mynumber - theirnumber) * piecepoint
        if boardlist["J"][0] == mypiece:
            score = math.inf
            return score
        elif boardlist["J"][0] == theirpiece:
            score = -math.inf
            return score
        if boardlist[letter][position] == mypiece:
            if letter in ("B", "C"):
                score += 10
                if position in (1, 2):
                    score += 10
            elif position in ("E", "F", "G"):
                if position == 1:
                    score += 10
                if letter == "F":
                    score += 10
            if self.mrcheck(letter, position, boardlist):
                score += 130
        elif boardlist[letter][position] == theirpiece:
            if letter in ("B", "C"):
                score -= 10
                if position in (1, 2):
                    score -= 10
            if self.mrcheck(letter, position, boardlist):
                score -= 130

        for l in range(9):
            lett = "A"
            lett = chr(ord(lett) + l)
            for i, x in enumerate(boardlist[lett]):
                if x == "e":
                    self.mplace(lett, i, mypiece, boardlist)
                    if self.mrcheck(lett, i, boardlist):
                        score += point
                    self.mundoplace(lett, i, boardlist)
                    self.mplace(lett, i, theirpiece, boardlist)
                    if self.mrcheck(lett, i, boardlist):
                        score -= point
                    self.mundoplace(lett, i, boardlist)
                elif x != "s":
                    if self.mcanremove(lett, i, boardlist):
                        if x == mypiece:
                            score += removepoint
                        else:
                            score -= removepoint

        return score

    def move(self, boardlist, mynumber, theirnumber, mypiece, theirpiece, flag):
        myboardlist = copy.deepcopy(boardlist)
        t0 = time.time()
        #check = self.minimax(myboardlist, 0, mypiece, mynumber, theirpiece, theirnumber, 2, flag)
        check = self.alphabeta(-math.inf, math.inf, myboardlist, 0, mypiece, mynumber, theirpiece, theirnumber, 4, flag)
        t1 = time.time()
        print("AI player chooses:", end=" ")
        print(check[1])
        print("AI used: ", end="")
        print(t1 - t0, end="")
        print(" seconds")
        return check[1]

#######################################
########### Sets up the game ##########
#######################################
def main():

    print("Welcome to Pylos")
    print("To place a stone please enter its position separated by a comma for example A,0")
    print("To raise a stone please enter its destination then the position of the piece for example E,0,A,3")
    print("For optional removes, if you do not wish to remove any pieces enter _ to not remove any pieces")
    print("Enjoy the game.")
    player1 = input("Is player 1 (white) human or AI? (H or A) ")
    if player1 == "H":
        player1 = Player("Human (White)")
    elif player1 == "A":
        player1 = Artificial("AI (White)")
    elif player1 == "A2":
        player1 = Artificial2("AI-2 (White)")
    else:
        return
    player2 = input("Is player 2 (black) human or AI? (H or A) ")
    if player2 == "H":
        player2 = Player("Human (Black)")
    elif player2 == "A":
        player2 = Artificial("AI (Black)")
    elif player2 == "A2":
        player2 = Artificial("AI-2 (Black)")
    else:
        return

    myBoard = Board(player1, player2)
    myBoard.play()

if __name__ == "__main__":
    main()
