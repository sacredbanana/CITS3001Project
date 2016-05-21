#######################################
############ Class: Board  ############
#######################################
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
            self.board_update()
            self.board_visual()
            #Tell player it's their turn
            print("Your move, " + player.name + ", you have ", end="")
            if player is self.white:
                print(str(self.whitepieces) + " pieces left")
            else:
                print(str(self.blackpieces) + " pieces left")
            #Get player's move Z[0,0]
            input_list = player.move()
            if player is self.white:
                if self.place(str(input_list[0]),  int(input_list[1]), "w"):
                    self.whitepieces -= 1  # minus one piece from player
                    if self.checkRemove():
                        while True:
                            print("Please remove 1 piece")
                            self.board_update()
                            self.board_visual()
                            input_list = player.move()
                            if self.removep(str(input_list[0]),  int(input_list[1]), "b"):
                                self.whitepieces += 1 # ++ one piece after removing one off board
                                break
                    player = switchPlayer(player)
            else:
                if self.place(str(input_list[0]),  int(input_list[1]), "b"):
                    self.blackpieces -= 1  # minus one piece from player
                    if self.checkRemove():
                        while True:
                            print("Please remove 1 piece")
                            self.board_update()
                            self.board_visual()
                            input_list = player.move()
                            if self.removep(str(input_list[0]),  int(input_list[1]), "w"):
                                self.blackpieces += 1 # ++ one piece after removing one off board
                                break
                            else:
                                print("Error input.")
                    player = switchPlayer(player)
            if (J[0] == "b"):
                self.win(switchPlayer(player))
                break
            elif(J[0] == "w"):
                self.win(switchPlayer(player))
                break

    def win(self,player):
        print(player.name + " won!")

    def board_visual(self):
        print("Level: 0     Level: 1   Level: 2  Level: 3")
        print("  0 1 2 3      0 1 2      0 1       0")
        ##################################################### LINE 1
        print("A",end="")
        for i in A:
            print("|", end="")
            print(i, end="")
        print("|   ", end="")
        print("E",end="")
        for i in E:
            print("|", end="")
            print(i, end="")
        print("|   ", end="")
        print("H",end="")
        for i in H:
            print("|", end="")
            print(i, end="")
        print("|    ", end="")
        print("J",end="")
        for i in J:
            print("|",end="")
            print(i, end="")
        print("|")
        print("B",end="")
        #################################################### LINE 2
        for i in B:
            print("|",end="")
            print(i, end="")
        print("|   ", end="")
        print("F",end="")
        for i in F:
            print("|", end="")
            print(i, end="")
        print("|   ", end="")
        print("I",end="")
        for i in I:
            print("|",end="")
            print(i, end="")
        print("|")
        print("C",end="")
        #################################################### LINE 3
        for i in C:
            print("|",end="")
            print(i, end="")
        print("|   ", end="")
        print("G",end="")
        for i in G:
            print("|", end="")
            print(i, end="")
        print("|")
        print("D",end="")
        for i in D:
            print("|", end="")
            print(i, end="")
        print("|\n")
        ####################################################

    # Places piece on position
    # @returns True if piece is successfully placed on position
    # @returns False if position is occupied or input was out of bound
    def place(self, letter, position, piece):
        if letter == "A" and 0 <= position <= 3:
            if A[position] == "e":
                A[position] = piece
                return True
            else:
                print("position not empty.")
                return False
        elif letter == "B" and 0 <= position <= 3:
            if B[position] == "e":
                B[position] = piece
                return True
            else:
                print("position not empty.")
                return False
        elif letter == "C" and 0 <= position <= 3:
            if C[position] == "e":
                C[position] = piece
                return True
            else:
                print("position not empty.")
                return False
        elif letter == "D" and 0 <= position <= 3:
            if D[position] == "e":
                D[position] = piece
                return True
            else:
                print("position not empty.")
                return False
        elif letter == "E" and 0 <= position <= 2:
            if E[position] == "e":
                E[position] = piece
                return True
            else:
                print("position not empty.")
                return False
        elif letter == "F" and 0 <= position <= 2:
            if F[position] == "e":
                F[position] = piece
                return True
            else:
                print("position not empty.")
                return False
        elif letter == "G" and 0 <= position <= 2:
            if G[position] == "e":
                G[position] = piece
                return True
            else:
                print("position not empty.")
                return False
        elif letter == "H" and 0 <= position <= 1:
            if H[position] == "e":
                H[position] = piece
                return True
            else:
                print("position not empty.")
                return False
        elif letter == "I" and 0 <= position <= 1:
            if I[position] == "e":
                I[position] = piece
                return True
            else:
                print("position not empty.")
                return False
        elif letter == "J" and position == 0:
            if J[position] == "e":
                J[position] = piece
                return True
            else:
                print("position not empty.")
                return False
        else:
            print("Invalid input, please check if your position is a valid input.")
            return False

    ### removes a piece ###
    def removep(self, letter, position, piece):
        if letter == "A":
            if A[position] == "e":
                print("Position is empty.")
                return False
            elif A[position] != "q" and A[position] != "v" and A[position] == piece:
                A[position] = "e"
                return True
            else:
                print("You cannot remove that piece")
                return False
        if letter == "B":
            if B[position] == "e":
                print("Position is empty.")
                return False
            elif B[position] != "q" and B[position] != "v"and B[position] == piece:
                B[position] = "e"
                return True
            else:
                print("You cannot remove that piece")
                return False
        if letter == "C":
            if C[position] == "e":
                print("Position is empty.")
                return False
            elif C[position] != "q" and C[position] != "v"and C[position] == piece:
                C[position] = "e"
                return True
            else:
                print("You cannot remove that piece")
                return False
        if letter == "D":
            if D[position] == "e":
                print("Position is empty.")
                return False
            elif D[position] != "q" and D[position] != "v"and D[position] == piece:
                D[position] = "e"
                return True
            else:
                print("You cannot remove that piece")
                return False

    ### unlocks sealed spaces on upper levels
    ### TODO: theres a bug in the code which needs fixing, with level 2 and above tht makes them e when they are supposed to be s
    def board_update(self):
        ### LEVEL 1 ###
        if(A[0] != "e" and A[1] != "e" and B[0] != "e" and B[1] != "e" and E[0] == "s"):  #unseals E0
            E[0] = "e"
        elif(A[0] == "e" or A[1] == "e" or B[0] == "e" or B[1] == "e" and E[0] == "e"): #makes E0 sealed again
            E[0] = "s"
        if(A[1] != "e" and A[2] != "e" and B[1] != "e" and B[2] != "e" and E[1] == "s"):  #unseals E1
            E[1] = "e"
        elif(A[1] == "e" or A[2] == "e" or B[1] == "e" or B[2] == "e" and E[1] == "e"): #makes E1 sealed again
            E[1] = "s"
        if(A[2] != "e" and A[3] != "e" and B[2] != "e" and B[3] != "e" and E[2] == "s"):  #unseals E2
            E[2] = "e"
        elif(A[2] == "e" or A[3] == "e" or B[2] == "e" or B[3] == "e" and E[2] == "e"): #makes E2 sealed again
            E[2] = "s"
        if(B[0] != "e" and B[1] != "e" and C[0] != "e" and C[1] != "e" and F[0] == "s"):  #unseals F0
            F[0] = "e"
        elif(B[0] == "e" or B[1] == "e" or C[0] == "e" or C[1] == "e" and F[0] == "e"): #makes F0 sealed again
            F[0] = "s"
        if(B[1] != "e" and B[2] != "e" and C[1] != "e" and C[2] != "e" and F[1] == "s"):  #unseals F1
            F[1] = "e"
        elif(B[1] == "e" or B[2] == "e" or C[1] == "e" or C[2] == "e" and F[1] == "e"): #makes F1 sealed again
            F[1] = "s"
        if(B[2] != "e" and B[3] != "e" and C[2] != "e" and C[3] != "e" and F[2] == "s"):  #unseals F2
            F[2] = "e"
        elif(B[2] == "e" or B[3] == "e" or C[2] == "e" or C[3] == "e" and F[2] == "e"): #makes F2 sealed again
            F[2] = "s"
        if(C[0] != "e" and C[1] != "e" and D[0] != "e" and D[1] != "e" and G[0] == "s"):  #unseals G0
            G[0] = "e"
        elif(C[0] == "e" or C[1] == "e" or D[0] == "e" or D[1] == "e" and G[0] == "e"): #makes G0 sealed again
            G[0] = "s"
        if(C[1] != "e" and C[2] != "e" and D[1] != "e" and D[2] != "e" and G[1] == "s"):  #unseals G1
            G[1] = "e"
        elif(C[1] == "e" or C[2] == "e" or D[1] == "e" or D[2] == "e" and G[1] == "e"): #makes G1 sealed again
            G[1] = "s"
        if(C[2] != "e" and C[3] != "e" and D[2] != "e" and D[3] != "e" and G[2] == "s"):  #unseals G2
            G[2] = "e"
        elif(C[2] == "e" or C[3] == "e" or D[2] == "e" or D[3] == "e" and G[1] == "e"): #makes G2 sealed again
            G[2] = "s"
        ### LEVEL 2 ###
        if(E[0] != "e" and E[1] != "e" and F[0] != "e" and F[1] != "e" and H[0] == "s"):  #unseals H0
            H[0] = "e"
        elif(E[0] == "e" or E[1] == "e" or F[0] == "e" or F[1] == "e" and H[0] == "e"): #makes H0 sealed again
            H[0] = "s"
        if(E[1] != "e" and E[2] != "e" and F[1] != "e" and F[2] != "e" and H[1] == "s"):  #unseals H1
            H[1] = "e"
        elif(E[1] == "e" or E[2] == "e" or F[2] == "e" or F[2] == "e" and H[1] == "e"): #makes H1 sealed again
            H[1] = "s"
        if(F[0] != "e" and F[1] != "e" and G[0] != "e" and G[1] != "e" and I[0] == "s"):  #unseals I0
            I[0] = "e"
        elif(F[0] == "e" or F[1] == "e" or G[0] == "e" or G[1] == "e" and I[0] == "e"): #makes I0 sealed again
            I[0] = "s"
        if(F[1] != "e" and F[2] != "e" and G[1] != "e" and G[2] != "e" and I[1] == "s"):  #unseals I1
            I[1] = "e"
        elif(F[1] == "e" or F[2] == "e" or G[1] == "e" or G[2] == "e" and I[1] == "e"): #makes I1 sealed again
            I[1] = "s"
        ### LEVEL 3 ###
        if(H[0] != "e" and H[1] != "e" and I[0] != "e" and I[1] != "e" and J[0] == "s"):  #unseals J0
            J[0] = "e"
        elif(H[0] == "e" or H[1] == "e" or I[0] == "e" or I[1] == "e" and J[0] == "e"): #makes J0 sealed again
            J[0] = "s"

    # Checks if a piece needs to be removed
    # Returns True if yes a piece needs to be removed
    def checkRemove(self):
        ### LEVEL 1 ###
        if(A[0] != "e"):
            if(A[0] == A[1] == A[2] == A[3]):
                return True
            if(A[0] == B[0] == C[0] == D[0]):
                return True
            if(A[0] == A[1] == B[0] == B[1]):
                return True
        if(C[0] != "e"):
            if(C[0] == C[1] == C[2] == C[3]):
                return True
            if(C[0] == C[1] == B[0] == B[1]):
                return True
            if(C[0] == C[1] == D[0] == D[1]):
                return True
        if(B[2] != "e"):
            if(B[0] == B[1] == B[2] == B[3]):
                return True
            if(A[1] == A[2] == B[1] == B[2]):
                return True
            if(C[1] == C[2] == B[1] == B[2]):
                return True
            if(A[2] == B[2] == C[2] == D[2] and A[2] != "e"):
                return True
            if(A[2] == A[3] == B[2] == B[3]):
                return True
            if(C[2] == C[3] == B[2] == B[3]):
                return True
        if(D[0] == D[1] == D[2] == D[3] and D[0] != "e"):
            return True
        if(A[1] == B[1] == C[1] == D[1] and A[1] != "e"):
            return True
        if(A[3] == B[3] == C[3] == D[3] and A[3] != "e"):
            return True
        if(C[1] == C[2] == D[1] == D[2] and C[1] != "e"):
            return True
        if(C[2] == C[3] == D[2] == D[3] and C[2] != "e"):
            return True

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
    myBoard = Board(player1,player2)
    myBoard.play()
    myBoard.board_visual()
    #myBoard.testtest()
    #myBoard.board_visual()




if __name__ == "__main__":
    main()