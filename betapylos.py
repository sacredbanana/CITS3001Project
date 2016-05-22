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

        global board_list
        board_list = simple_board

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
    # TODO
    def rcheck(self):
        num = 0
        if board_list["E"][0] != "s" and board_list["E"][0] != "e":
            if board_list["E"][0] == board_list["E"][1] == board_list["E"][2]:
                return True
            if board_list["E"][0] == board_list["F"][0] == board_list["G"][0]:
                return True
        if board_list["F"][1] != "s" and board_list["F"][1] != "e":
            if board_list["F"][0] == board_list["F"][1] == board_list["F"][2]:
                return True
            if board_list["E"][1] == board_list["F"][1] == board_list["G"][1]:
                return True
            if board_list["F"][0] == board_list["F"][1] == board_list["G"][0] == board_list["G"][1]:
                return True
            if board_list["F"][1] == board_list["F"][2] == board_list["G"][1] == board_list["G"][2]:
                return True
            if board_list["E"][0] == board_list["E"][1] == board_list["F"][0] == board_list["F"][1]:
                return True
            if board_list["E"][1] == board_list["E"][2] == board_list["F"][1] == board_list["F"][2]:
                return True
        if board_list["G"][2] != "s" and board_list["G"][2] != "e":
            if board_list["G"][0] == board_list["G"][1] == board_list["G"][2]:
                return True
            if board_list["E"][2] == board_list["F"][2] == board_list["G"][2]:
                return True
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
            if board_list[letter][position] == piece:
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
                print("Piece removed from "+ letter)
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
            self.board_visual()
            if self.rcheck():
                player = switchPlayer(player)
                 # Tell player it's their turn
                print(player.name + "'s move please remove a piece.")
                if player is self.white:
                    input_list = player.move(board_list, self.whitepieces)
                else:
                    input_list = player.move(board_list, self.blackpieces)
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
                        print(player.name + " now has " + str(self.whitepieces) + " pieces left.")
                        player = switchPlayer(player)
                else:
                    if self.raisep("Z", 0, "b", i, j, board_list, self.blackpieces):
                        self.blackpieces += 1
                        print(player.name + " now has " + str(self.blackpieces) + " pieces left.")
                        player = switchPlayer(player)
            else:
                # Tell player it's their turn
                print(player.name + "'s move, you have ", end="")
                if player is self.white:
                    print(str(self.whitepieces) + " pieces left")
                    if self.whitepieces == 0:  # if you have 0 pieces the other player wins
                        self.win(switchPlayer(player))
                        break
                    input_list = player.move(board_list, self.whitepieces)
                else:
                    print(str(self.blackpieces) + " pieces left")
                    if self.blackpieces == 0:  # if you have 0 pieces the other player wins
                        self.win(switchPlayer(player))
                        break
                    input_list = player.move(board_list, self.blackpieces)
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
                    else:
                        if self.place(i, j, "b", board_list, self.blackpieces):
                            self.blackpieces -= 1
                            player = switchPlayer(player)
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
                    else:
                        if self.raisep(i, j, "b", x, y, board_list, self.blackpieces):
                            player = switchPlayer(player)
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

    def move(self, boardlist, piecenumber):
        inputs = input("Enter position seperated by comma for example A,1: ")
        input_list = inputs.split(',')
        return input_list


#######################################
########### Sets up the game ##########
#######################################
def main():

    print("Welcome to Pylos")
    player1 = input("Is player 1 (white) human or machine? (h or m) ")
    if(player1=="h"): player1 = Player("White")
    elif(player1=="m"): player1 = Machine("Machine White")
    else: return
    player2 = input("Is player 2 (black) human or machine? (h or m) ")
    if(player2=="h"): player2 = Player("Black")
    elif(player2=="m"): player2 = Machine("Machine Black")
    else: return
    print("'e' represents an empty block and 's' represents a sealed block")
    myBoard = Board(player1, player2)
    myBoard.play()




if __name__ == "__main__":
    main()