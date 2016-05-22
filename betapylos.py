#######################################
############ Class: Board  ############
#######################################
class Board(object):

    def __init__(self, player1, player2):  # player1 begins the game, player1 is white
        self.whitepieces = 1
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
            "J": ["s"]
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

    # Places piece on position
    # @returns True if successful
    # @returns False if otherwise
    def place(self, letter, position, piece):
        try:
            if board_list[letter][position] == "e":
                board_list[letter][position] = piece
                return True
            else:
                print("Position is not empty.")
                return False
        except:
            print("Invalid input, please check your input is correct.")
            return False

    def removep(self, letter, position, piece):
        try:
            if board_list[letter][position] == piece:
                board_list[letter][position] = "e"
                return True
            else:
                print("You cannot remove from that position.")
                return False
        except:
            print("Invalid input, please check your input is correct.")
            return False

    def raise(self, letter, position, piece, letter2, position2):
        self.removep(letter2, position2, piece)
        self.place(letter, position, piece)


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
            # Tell player it's their turn
            print(player.name + "'s move, you have ", end="")
            if player is self.white:
                print(str(self.whitepieces) + " pieces left")
                if self.whitepieces == 0:  # if you have 0 pieces the other player wins
                    self.win(switchPlayer(player))
                    break
            else:
                print(str(self.blackpieces) + " pieces left")
                if self.blackpieces == 0:  # if you have 0 pieces the other player wins
                    self.win(switchPlayer(player))
                    break
            input_list = player.move()
            try:
                i = str(input_list[0])
                j = int(input_list[1])
            except:
                print("Invalid input.")
                continue
            if player is self.white:
                if self.place(i, j, "w"):
                    self.whitepieces -= 1
                    player = switchPlayer(player)
            else:
                if self.place(i, j, "b"):
                    self.blackpieces -= 1
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

    def move(self):
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
    myBoard.board_visual()




if __name__ == "__main__":
    main()