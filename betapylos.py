import copy
import math

#######################################
############ Class: Board  ############
#######################################
class Board(object):

    def __init__(self, player1, player2):  # player1 begins the game, player1 is white
        self.whitepieces = 7
        self.blackpieces = 7
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
            "J": ["s"]
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
            "E": ["b","w","e"],
            "F": ["w","w","b"],
            "G": ["e","b","e"],
            "H": ["s","s"],
            "I": ["s","s"],
            "J": ["s"],
            "Z": ["e"]
        }

        global board_list
        board_list = simple_board

        global last_move
        last_move = ["Z", 0]

    # Visualises the board by printing out the values
    def board_visual(self):
        self.board_update()
        print("")
        print(board_list["E"], "   ", board_list["H"], "   ", board_list["J"])
        print(board_list["F"], "   ", board_list["I"])
        print(board_list["G"])

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

    # Checks if a piece needs to be removed
    # @Returns True if a piece needs to be removed
    # @Returns False if otherwise
    def rcheck(self, letter, position):
        if board_list[letter][position] != "s" and board_list[letter][position] != "e":
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
            if letter in ("H", "I"):
                if board_list["H"][0] == board_list["H"][1] == board_list["I"][0] == board_list["I"][1]:
                    return True
            return False
        return False

    # Checks if a position can be removed based on if any piece is on top of it
    # @Returns True if no piece stands on top of the position
    # @Returns False if a piece is stacked on top of the position
    def canremove(self, letter, position):
        if letter == "E":
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
        if letter in ("E", "F", "G"):
            num = 1
        elif letter in ("H", "I"):
            num = 2
        else:
            print("Invalid input.")
            return False
        if letter2 in ("E", "F", "G"):
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
                    player = switchPlayer(player)
                    continue
                if player is self.white:
                    if self.raisep("Z", 0, "w", i, j, board_list, self.whitepieces):
                        self.whitepieces += 1
                        print("Piece removed from " + i + "," + str(j))
                        print(player.name + " now has " + str(self.whitepieces) + " pieces left.")
                        last_move[0] = i
                        last_move[1] = j
                else:
                    if self.raisep("Z", 0, "b", i, j, board_list, self.blackpieces):
                        self.blackpieces += 1
                        print("Piece removed from " + i + "," + str(j))
                        print(player.name + " now has " + str(self.blackpieces) + " pieces left.")
                        last_move[0] = i
                        last_move[1] = j
                player = switchPlayer(player)
                print(last_move)
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
############ Class: Machine ###########
#######################################
class Machine(Player):

    def minimax(self, boardlist, side, mypiece, theirpiece, depth, beginscore, flag):
        best = [None, None]
        ## for normal moves
        if flag == 0:
            movelist = self.moveList(boardlist)
            if depth == 0:
                if side == 0:
                    best = [-math.inf, ["F", 1]]
                    for i in movelist:
                        self.mplace(i[0], i[1], mypiece, boardlist)
                        score = self.evaluate(boardlist, i[0], i[1], beginscore)
                        self.mundoplace(i[0], i[1], boardlist)
                        if score >= best[0]:
                            best[0] = score
                            best[1] = i
                else:
                    best = [math.inf, ["F", 1]]
                    for i in movelist:
                        self.mplace(i[0], i[1], mypiece, boardlist)
                        score = -(self.evaluate(boardlist, i[0], i[1], -beginscore))
                        self.mundoplace(i[0], i[1], boardlist)
                        if score <= best[0]:
                            best[0] = score
                            best[1] = i
            else:
                if side == 0:
                    best = [-math.inf, ["F", 1]]
                    for i in movelist:
                        self.mplace(i[0], i[1], mypiece, boardlist)
                        score = self.evaluate(boardlist, i[0], i[1], beginscore)
                        if self.mrcheck(i[0], i[1], boardlist):
                            self.minimax(boardlist, 0, theirpiece, mypiece, depth-1, score, 1)
                        else:
                            self.minimax(boardlist, 1, theirpiece, mypiece, depth-1, score, 0)
                        self.mundoplace(i[0], i[1], boardlist)
                        if score >= best[0]:
                            best[0] = score
                            best[1] = i
                else:
                    best = [math.inf, ["F", 1]]
                    for i in movelist:
                        self.mplace(i[0], i[1], mypiece, boardlist)
                        score = -(self.evaluate(boardlist, i[0], i[1], -beginscore))
                        if self.mrcheck(i[0], i[1], boardlist):
                            self.minimax(boardlist, 1, theirpiece, mypiece, depth-1, score, 1)
                        else:
                            self.minimax(boardlist, 0, theirpiece, mypiece, depth-1, score, 0)
                        self.mundoplace(i[0], i[1], boardlist)
                        if score <= best[0]:
                            best[0] = score
                            best[1] = i
        ## for removes
        elif flag == 1:
            movelist = self.removeList(boardlist, mypiece)
            if depth == 0:
                if side == 0:
                    best = [-math.inf, ["E", 1]]
                    for i in movelist:
                        score = self.remevaluate(boardlist, i[0], i[1], beginscore)
                        if score >= best[0]:
                            best[0] = score
                            best[1] = i
                else:
                    best = [math.inf, ["E", 1]]
                    for i in movelist:
                        score = self.remevaluate(boardlist, i[0], i[1], beginscore)
                        if score <= best[0]:
                            best[0] = score
                            best[1] = i
            else:
                if side == 0:
                    best = [-math.inf, ["E", 1]]
                    for i in movelist:
                        score = self.remevaluate(boardlist, i[0], i[1], beginscore)
                        self.mundoplace(i[0],i[1], boardlist)
                        self.minimax(boardlist, 1, theirpiece, mypiece, depth-1, score, 0)
                        self.mplace(i[0], i[1], mypiece, boardlist)
                        if score >= best[0]:
                            best[0] = score
                            best[1] = i
                else:
                    best = [math.inf, ["E", 1]]
                    for i in movelist:
                        score = self.remevaluate(boardlist, i[0], i[1], beginscore)
                        self.mundoplace(i[0],i[1], boardlist)
                        self.minimax(boardlist, 0, theirpiece, mypiece, depth-1, score, 0)
                        self.mplace(i[0], i[1], mypiece, boardlist)
                        if score <= best[0]:
                            best[0] = score
                            best[1] = i

        return best


    # Generates possible move list based on game state
    # stores the moves in a list, count
    # @Returns count
    def moveList(self, boardlist):
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

    # Generates  possible remove list based on game state
    # stores the moves in a list, count
    # @Returns count
    def removeList(self, boardlist, piece):
        count = []
        for i, x in enumerate(boardlist["E"]):
            if x == piece and self.mcanremove("E", i, boardlist):
                count.append(["E", i])
        for i, x in enumerate(boardlist["F"]):
            if x == piece and self.mcanremove("F", i, boardlist):
                count.append(["F", i])
        for i, x in enumerate(boardlist["G"]):
            if x == piece and self.mcanremove("G", i, boardlist):
                count.append(["G", i])
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
                print("Position is not empty.1")
                print(letter)
                print(position)
                print(boardlist[letter][position])
                return False
        except:
            print("Invalid input, please check your input is correct.111")
            return False

    def mundoplace(self, letter, position, boardlist):
            if boardlist[letter][position] in ("w", "b"):
                boardlist[letter][position] = "e"
                self.mboard_update(boardlist)
                return True
            else:
                print("mundplace has an error.")
                return False

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

    def mboard_visual(self, boardlist):
        print("")
        print(boardlist["E"], "   ", boardlist["H"], "   ", boardlist["J"])
        print(boardlist["F"], "   ", boardlist["I"])
        print(boardlist["G"])

    # Checks if a piece needs to be removed
    # @Returns True if a piece needs to be removed
    # @Returns False if otherwise
    def mrcheck(self, letter, position, boardlist):
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

    # Checks if a position can be removed based on if any piece is on top of it
    # @Returns True if no piece stands on top of the position
    # @Returns False if a piece is stacked on top of the position
    def mcanremove(self, letter, position, boardlist):
        if letter == "E":
            if position == 0:
                if boardlist["H"][0] in ("s", "e"):
                    return True
                else:
                    return False
            if position == 1:
                if boardlist["H"][0] in ("s", "e") and boardlist["H"][1] in ("s", "e"):
                    return True
                else:
                    return False
            if position == 2:
                if boardlist["H"][1] in ("s", "e"):
                    return True
                else:
                    return False
        elif letter == "F":
            if position == 0:
                if boardlist["H"][0] in ("s", "e") and boardlist["I"][0] in ("s", "e"):
                    return True
                else:
                    return False
            if position == 1:
                if boardlist["H"][0] in ("s", "e") and boardlist["H"][1] in ("s", "e") and boardlist["I"][0] in ("s", "e") and boardlist["I"][1] in ("s", "e"):
                    return True
                else:
                    return False
            if position == 2:
                if boardlist["H"][1] in ("s", "e") and boardlist["I"][1] in ("s", "e"):
                    return True
                else:
                    return False
        elif letter == "G":
            if position == 0:
                if boardlist["I"][0] in ("s", "e"):
                    return True
                else:
                    return False
            if position == 1:
                if boardlist["I"][0] in ("s", "e") and boardlist["I"][1] in ("s", "e"):
                    return True
                else:
                    return False
            if position == 2:
                if boardlist["I"][1] in ("s", "e"):
                    return True
                else:
                    return False
        elif letter in ("H", "I"):
            return True
        else:
            return False

    # Utility function for normal place moves
    def evaluate(self, boardlist, letter, position, prevscore):
        score = prevscore
        if letter == "J":
            score = math.inf
            return score
        if self.mrcheck(letter, position, boardlist):
            score += 10
        ## stop them from winning
        if letter == "E":
            if position == 0:
                if boardlist["E"][0] != boardlist["E"][1] and boardlist["E"][1] not in ["s","e"]:
                    if boardlist["E"][1] == boardlist["E"][2]:
                        score += 7
                    if boardlist["E"][1] == boardlist["F"][1] == boardlist["F"][0]:
                        score += 7
                if boardlist["E"][0] != boardlist["F"][0] and boardlist["F"][0] not in ["s","e"]:
                    if boardlist["F"][0] == boardlist["G"][0]:
                        score += 7
            elif position == 1:
                if boardlist["E"][1] != boardlist["E"][0] and boardlist["E"][0] not in ["s","e"]:
                    if boardlist["E"][0] == boardlist["E"][2]:
                        score += 7
                    if boardlist["E"][0] == boardlist["F"][0] == boardlist["F"][1]:
                        score += 6
                if boardlist["E"][1] != boardlist["F"][1] and boardlist["F"][1] not in ["s","e"]:
                    if boardlist["F"][1] == boardlist["G"][1]:
                        score += 7
                    if boardlist["F"][1] == boardlist["F"][2] == boardlist["E"][2]:
                        score += 7
            elif position == 2:
                if boardlist["E"][2] != boardlist["E"][1] and boardlist["E"][1] not in ["s","e"]:
                    if boardlist["E"][1] == boardlist["E"][0]:
                        score += 7
                    if boardlist["E"][1] == boardlist["F"][1] == boardlist["F"][2]:
                        score += 7
                if boardlist["E"][2] != boardlist["F"][2] and boardlist["F"][2] not in ["s","e"]:
                    if boardlist["F"][2] == boardlist["G"][2]:
                        score += 7
        elif letter == "F":
            if position == 0:
                if boardlist["F"][0] != boardlist["E"][0] and boardlist["E"][0] not in ["s","e"]:
                    if boardlist["E"][0] == boardlist["G"][0]:
                        score += 7
                    if boardlist["E"][0] == boardlist["E"][1] == boardlist["F"][1]:
                        score += 7
                if boardlist["F"][0] != boardlist["F"][1] and boardlist["F"][1] not in ["s","e"]:
                    if boardlist["F"][1] == boardlist["F"][2]:
                        score += 7
                    if boardlist["F"][1] == boardlist["G"][1] == boardlist["G"][0]:
                        score += 7
            elif position == 1:
                if boardlist["F"][1] != boardlist["E"][1] and boardlist["E"][1] not in ["s","e"]:
                    if boardlist["E"][1] == boardlist["G"][1]:
                        score += 7
                    if boardlist["E"][1] == boardlist["E"][0] == boardlist["F"][0]:
                        score += 7
                    if boardlist["E"][1] == boardlist["E"][2] == boardlist["F"][2]:
                        score += 7
                if boardlist["F"][1] != boardlist["F"][2] and boardlist["F"][2] not in ["s","e"]:
                    if boardlist["F"][2] == boardlist["F"][0]:
                        score += 7
                    if boardlist["F"][2] == boardlist["G"][2] == boardlist["G"][1]:
                        score += 7
                if boardlist["F"][1] != boardlist["G"][1] and boardlist["G"][1] not in ["s","e"]:
                    if boardlist["G"][1] == boardlist["G"][0] == boardlist["F"][0]:
                        score += 7
            elif position == 2:
                if boardlist["F"][2] != boardlist["E"][2] and boardlist["E"][2] not in ["s","e"]:
                    if boardlist["E"][2] == boardlist["G"][2]:
                        score += 7
                    if boardlist["E"][2] == boardlist["E"][1] == boardlist["F"][1]:
                        score += 7
                if boardlist["F"][2] != boardlist["F"][1] and boardlist["F"][1] not in ["s","e"]:
                    if boardlist["F"][1] == boardlist["G"][1] == boardlist["G"][2]:
                        score += 7
                    if boardlist["F"][1] == boardlist["F"][0]:
                        score += 7
        elif letter == "G":
            if position == 0:
                if boardlist["G"][0] != boardlist["F"][0] and boardlist["F"][0] not in ["s","e"]:
                    if boardlist["F"][0] == boardlist["E"][0]:
                        score += 7
                    if boardlist["F"][0] == boardlist["F"][1] == boardlist["G"][1]:
                        score += 7
                if boardlist["G"][0] != boardlist["G"][1] and boardlist["G"][1] not in ["s","e"]:
                    if boardlist["G"][1] == boardlist["G"][2]:
                        score += 7
            elif position == 1:
                if boardlist["G"][1] != boardlist["F"][1] and boardlist["F"][1] not in ["s","e"]:
                    if boardlist["F"][1] == boardlist["E"][1]:
                        score += 7
                    if boardlist["F"][1] == boardlist["F"][0] == boardlist["G"][0]:
                        score += 7
                    if boardlist["F"][1] == boardlist["F"][2] == boardlist["G"][2]:
                        score += 7
                if boardlist["G"][1] == boardlist["G"][0] and boardlist["G"][0] not in ["s","e"]:
                    if boardlist["G"][0] == boardlist["G"][2]:
                        score += 7
            elif position == 2:
                if boardlist["G"][2] != boardlist["F"][2] and boardlist["F"][2] not in ["s", "e"]:
                    if boardlist["F"][2] == boardlist["E"][2]:
                        score += 7
                    if boardlist["F"][2] == boardlist["F"][1] == boardlist["G"][1]:
                        score += 7
                if boardlist["G"][2] != boardlist["G"][1] and boardlist["G"][1] not in ["s", "e"]:
                    if boardlist["G"][1] == boardlist["G"][0]:
                        score += 7

        ## Lets get closer to winning position
        if letter == "E":
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
                        score += 3
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
        elif letter == "H":
            if position == 0:
                if boardlist["H"][0] != boardlist["E"][0]:
                    score += 1
                if boardlist["H"][0] != boardlist["E"][1]:
                    score += 1
                if boardlist["H"][0] != boardlist["F"][1]:
                    score += 1
                if boardlist["H"][0] != boardlist["F"][0]:
                    score += 1
            elif position == 1:
                if boardlist["H"][1] != boardlist["E"][1]:
                    score += 1
                if boardlist["H"][1] != boardlist["E"][2]:
                    score += 1
                if boardlist["H"][1] != boardlist["F"][1]:
                    score += 1
                if boardlist["H"][1] != boardlist["F"][2]:
                    score += 1
            score += 1
        elif letter == "I":
            if position == 0:
                if boardlist["I"][0] != boardlist["F"][0]:
                    score += 1
                if boardlist["I"][0] != boardlist["F"][1]:
                    score += 1
                if boardlist["I"][0] != boardlist["G"][1]:
                    score += 1
                if boardlist["I"][0] != boardlist["G"][0]:
                    score += 1
            elif position == 1:
                if boardlist["I"][1] != boardlist["F"][1]:
                    score += 1
                if boardlist["I"][1] != boardlist["F"][2]:
                    score += 1
                if boardlist["I"][1] != boardlist["G"][1]:
                    score += 1
                if boardlist["I"][1] != boardlist["G"][2]:
                    score += 1
            score += 1

        return score

    # Utility function for removes
    def remevaluate(self, boardlist, letter, position, prevscore):
        score = prevscore + 10
        if self.mrcheck(letter, position, boardlist):
            score += 3
        if letter == "E":
            if position == 0:
                if boardlist["E"][0] != boardlist["E"][1] and boardlist["E"][1] not in ["s","e"]:
                    if boardlist["E"][1] == boardlist["E"][2]:
                        score -= 3
                    if boardlist["E"][1] == boardlist["F"][1] == boardlist["F"][0]:
                        score -= 3
                if boardlist["E"][0] != boardlist["F"][0] and boardlist["F"][0] not in ["s","e"]:
                    if boardlist["F"][0] == boardlist["G"][0]:
                        score -= 3
            elif position == 1:
                score -= 1
                if boardlist["E"][1] != boardlist["E"][0] and boardlist["E"][0] not in ["s","e"]:
                    if boardlist["E"][0] == boardlist["E"][2]:
                        score -= 3
                    if boardlist["E"][0] == boardlist["F"][0] == boardlist["F"][1]:
                        score -= 3
                if boardlist["E"][1] != boardlist["F"][1] and boardlist["F"][1] not in ["s","e"]:
                    if boardlist["F"][1] == boardlist["G"][1]:
                        score -= 3
                    if boardlist["F"][1] == boardlist["F"][2] == boardlist["E"][2]:
                        score -= 3
            elif position == 2:
                if boardlist["E"][2] != boardlist["E"][1] and boardlist["E"][1] not in ["s","e"]:
                    if boardlist["E"][1] == boardlist["E"][0]:
                        score -= 3
                    if boardlist["E"][1] == boardlist["F"][1] == boardlist["F"][2]:
                        score -= 3
                if boardlist["E"][2] != boardlist["F"][2] and boardlist["F"][2] not in ["s","e"]:
                    if boardlist["F"][2] == boardlist["G"][2]:
                        score -= 3
        elif letter == "F":
            score -= 1
            if position == 0:
                if boardlist["F"][0] != boardlist["E"][0] and boardlist["E"][0] not in ["s","e"]:
                    if boardlist["E"][0] == boardlist["G"][0]:
                        score -= 3
                    if boardlist["E"][0] == boardlist["E"][1] == boardlist["F"][1]:
                        score -= 3
                if boardlist["F"][0] != boardlist["F"][1] and boardlist["F"][1] not in ["s","e"]:
                    if boardlist["F"][1] == boardlist["F"][2]:
                        score -= 3
                    if boardlist["F"][1] == boardlist["G"][1] == boardlist["G"][0]:
                        score -= 3
            elif position == 1:
                score -= 1
                if boardlist["F"][1] != boardlist["E"][1] and boardlist["E"][1] not in ["s","e"]:
                    if boardlist["E"][1] == boardlist["G"][1]:
                        score -= 3
                    if boardlist["E"][1] == boardlist["E"][0] == boardlist["F"][0]:
                        score -= 3
                    if boardlist["E"][1] == boardlist["E"][2] == boardlist["F"][2]:
                        score -= 3
                if boardlist["F"][1] != boardlist["F"][2] and boardlist["F"][2] not in ["s","e"]:
                    if boardlist["F"][2] == boardlist["F"][0]:
                        score -= 3
                    if boardlist["F"][2] == boardlist["G"][2] == boardlist["G"][1]:
                        score -= 3
                if boardlist["F"][1] != boardlist["G"][1] and boardlist["G"][1] not in ["s","e"]:
                    if boardlist["G"][1] == boardlist["G"][0] == boardlist["F"][0]:
                        score -= 3
            elif position == 2:
                if boardlist["F"][2] != boardlist["E"][2] and boardlist["E"][2] not in ["s","e"]:
                    if boardlist["E"][2] == boardlist["G"][2]:
                        score -= 3
                    if boardlist["E"][2] == boardlist["E"][1] == boardlist["F"][1]:
                        score -= 3
                if boardlist["F"][2] != boardlist["F"][1] and boardlist["F"][1] not in ["s","e"]:
                    if boardlist["F"][1] == boardlist["G"][1] == boardlist["G"][2]:
                        score -= 3
                    if boardlist["F"][1] == boardlist["F"][0]:
                        score -= 3
        elif letter == "G":
            if position == 0:
                if boardlist["G"][0] != boardlist["F"][0] and boardlist["F"][0] not in ["s","e"]:
                    if boardlist["F"][0] ==  boardlist["E"][0]:
                        score -= 3
                    if boardlist["F"][0] == boardlist["F"][1] == boardlist["G"][1]:
                        score -= 3
                if boardlist["G"][0] != boardlist["G"][1] and boardlist["G"][1] not in ["s","e"]:
                    if boardlist["G"][1] == boardlist["G"][2]:
                        score -= 3
            elif position == 1:
                score -= 1
                if boardlist["G"][1] != boardlist["F"][1] and boardlist["F"][1] not in ["s","e"]:
                    if boardlist["F"][1] == boardlist["E"][1]:
                        score -= 3
                    if boardlist["F"][1] == boardlist["F"][0] == boardlist["G"][0]:
                        score -= 3
                    if boardlist["F"][1] == boardlist["F"][2] == boardlist["G"][2]:
                        score -= 3
                if boardlist["G"][1] == boardlist["G"][0] and boardlist["G"][0] not in ["s","e"]:
                    if boardlist["G"][0] == boardlist["G"][2]:
                        score -= 3
            elif position == 2:
                if boardlist["G"][2] != boardlist["F"][2] and boardlist["F"][2] not in ["s", "e"]:
                    if boardlist["F"][2] == boardlist["E"][2]:
                        score -= 3
                    if boardlist["F"][2] == boardlist["F"][1] == boardlist["G"][1]:
                        score -= 3
                if boardlist["G"][2] != boardlist["G"][1] and boardlist["G"][1] not in ["s", "e"]:
                    if boardlist["G"][1] == boardlist["G"][0]:
                        score -= 3
        else:
            score += 1

        return score



    def move(self, boardlist, mypiecenumber, theirpiecenumber, mypiece, theirpiece, flag):
        myboardlist = copy.deepcopy(boardlist)
        check = self.minimax(myboardlist, 0, mypiece, theirpiece, 4, 0, flag)[1]
        print("Machine player chooses:", end=" ")
        print(check)
        return check



#######################################
########### Sets up the game ##########
#######################################
def main():

    print("Welcome to Pylos")
    player1 = input("Is player 1 (white) human or machine? (h or m) ")
    if(player1=="h"): player1 = Player("Human White")
    elif(player1=="m"): player1 = Machine("Machine White")
    else:
        return
    player2 = input("Is player 2 (black) human or machine? (h or m) ")
    if(player2=="h"): player2 = Player("Human Black")
    elif(player2=="m"): player2 = Machine("Machine Black")
    else:
        return
    print("'e' represents an empty block and 's' represents a sealed block")
    myBoard = Board(player1, player2)
    myBoard.play()




if __name__ == "__main__":
    main()