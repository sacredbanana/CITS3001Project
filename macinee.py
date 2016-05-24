import math

#######################################
############ Class: Machine ###########
#######################################
class Machine(Player):

    def minimax(self, boardlist, side, mypiece, theirpiece):
        myboardlist = copy.deepcopy(boardlist)
        self.mboard_visual(myboardlist)
        movelist = self.moveList(myboardlist)
        print("Movelist: ", end="")
        print(movelist)
        best = [None, None]
        nextmove= [None, None]
        if side == 0:
            print("")
            print("Black's turn:")
            best[0] = -20
            for i in movelist:
                print("currently looping for " + str(i) + " in " + str(movelist))
                nextmove[0] = str(i[0])
                nextmove[1] = int(i[1])
                print("1nextmove: ", end="")
                print(nextmove)
                if nextmove == ["J", 0]:
                    return [20, ["J", 0]]
                self.mplace(nextmove[0], nextmove[1], mypiece, myboardlist)
                reply = self.minimax(myboardlist, 1, mypiece, theirpiece)
                print(reply)
                print(best)
                if reply[0] >= best[0]:  # maximise, [20, ['I', 1]]
                    best[0] = reply[0]
                    best[1] = nextmove
                    print("------------------")
                    print("it gets here1")
                    print(reply)
                    print(best)
                    print("------------------")
                self.mundoplace(nextmove[0], nextmove[1], myboardlist)
                self.mboard_visual(myboardlist)
                print(str(nextmove) + " got removed1")
        else:
            print("")
            print("White's turn:")
            best[0] = 20
            for i in movelist:
                print("currently looping for " + str(i) + " in " + str(movelist))
                nextmove[0] = str(i[0])
                nextmove[1] = int(i[1])
                print("2nextmove: ", end="")
                print(nextmove)
                if nextmove == ["J", 0]:
                    return [20, ["J", 0]]
                self.mplace(nextmove[0], nextmove[1], theirpiece, myboardlist)
                reply = self.minimax(myboardlist, 0, mypiece, theirpiece)
                print(reply)
                print(best)
                if reply[0] <= best[0]: # minimise
                    best[0] = reply[0]
                    best[1] = nextmove
                    print("------------------")
                    print("it gets here2")
                    print("------------------")
                self.mundoplace(nextmove[0], nextmove[1], myboardlist)
                self.mboard_visual(myboardlist)
                print(str(nextmove) + " got removed2")
        return best

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
    '''
    def generatemove(self, boardlist):
        for i in boardlist["E"][:]:
            if i == "e":
                return ["E", boardlist["E"].index(i)]
        for i in boardlist["F"][:]:
            if i == "e":
                return ["F", boardlist["F"].index(i)]
        for i in boardlist["G"][:]:
            if i == "e":
                return ["G", boardlist["G"].index(i)]
        for i in boardlist["H"][:]:
            if i == "e":
                return ["H", boardlist["H"].index(i)]
        for i in boardlist["I"][:]:
            if i == "e":
                return ["I", boardlist["I"].index(i)]
        if boardlist["J"][0] == "e":
            return ["J", 0]
        else:
            print("No more spots left")
            return None
    '''
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

    def evaluate(self, boardlist, letter, position, prevscore):
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



    def move(self, boardlist, mypiecenumber, theirpiecenumber, mypiece, theirpiece):
        check = self.minimax(boardlist, 0, mypiece, theirpiece)[1]
        print("Machine player chooses:", end=" ")
        print(check)
        return check