class Board(object):

    def __init__(self,player1,player2):  # player1 begins the game, player1 is white
        self.whitepieces = 15
        self.blackpieces = 15
        self.white = player1  # white
        self.black = player2  # black

        # Creates the board at its clean state
        # e = Empty
        # Level 0:
        global A
        A = ["e","e","e","e"]
        global B
        B = ["e","e","e","e"]
        global C
        C = ["e","e","e","e"]
        global D
        D = ["e","e","e","e"]

        # Level 1:
        global E
        E = ["s","s","s"]
        global F
        F = ["s","s","s"]
        global G
        G = ["s","s","s"]

        # Level 2:
        global H
        H = ["s","s"]
        global I
        I = ["s","s"]

        # Level 3, top level:
        global J
        J = ["s"]


    def play(self):
        def switchPlayer(player):
            if player is self.white:
                return self.black
            else:
                return self.white

        player = self.white

        while True:  # game playing
            self.board_visual()
            print("")
            print("Your move, " + player.name)
            if player is self.white:
                print(player.name + ", you have " + self.whitepieces + " left")
            else:
                print(player.name + ", you have " + self.blackpieces + " left")
            #Get player's move Z[0,0]
            move = player.move()
            if move == "e":  # if position is empty, make move
                if player is self.white: # minus one piece from player
                    self.whitepieces -= 1
                else:
                    self.blackpieces -= 1
            else:
                print("Your move is illegal, thus you lost the game.")
                self.win(switchPlayer(player))
                break
            player = switchPlayer(player)


        def win(self,player):
            print(player.name + " won!")

    def board_visual(self):
        ### LEVEL ZERO ###
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
            print("|", end="")
            print(i, end="")
        print("|\n")



class Player(object):

    def __init__(self, name):
        self.name = name

    def move(self, position):
        while True:
            try:
                return input()
            except:
                print("Invalid input")


#Sets Up Game
def main():

    print("Welcome to Pylos")
    player1 = input("Is player1 human or machine? (h or m) ")
    if(player1=="h"): player1 = Player("Player 1")
    elif(player1=="m"): player1 = Machine("Machine Player 1")
    else: return
    player2 = input("Is player2 human or machine? (h or m) ")
    if(player2=="h"): player2 = Player("Player 2")
    elif(player2=="m"): player2 = Machine("Machine Player 2")
    else: return
    myBoard = Board(player1,player2)
    ##myBoard.play()
    myBoard.board_visual()




if __name__ == "__main__":
    main()