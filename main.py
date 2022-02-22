class chess:
    def __init__(self):
        self.board = [["r","n","b","q","k","b","n","r"],
                      ["p","p","p","p","p","p","p","p"],
                      ["#","#","#","#","#","#","#","#"],
                      ["#","#","#","#","#","#","#","#"],
                      ["#","#","#","#","#","#","#","#"],
                      ["#","#","#","#","#","#","#","#"],
                      ["P","P","P","P","P","P","P","P"],
                      ["R","N","B","Q","K","B","N","R"]]
        self.turn = 'w'

    def print(self):
        print("  01234567",sep='',end='\n')
        for rpos, r in enumerate(self.board):
            print(rpos,sep='',end=' ')
            for cpos, c in enumerate(r):
                print(c,sep='',end='')
            print("\n",sep='',end='')

    def store(self):
        with open("board.txt","w") as file:
            file.write(self.turn)
            file.write(str(self.board))

    def changeTurn(self):
        if self.turn == 'w':
            self.turn = 'b'
        else:
            self.turn = 'w'

    def regulate(self,fx,fy,tx,ty):
        if (fx <= 7 and fx >= 0) and (fy <= 7 and fy >= 0) and (tx <= 7 and tx >= 0) and (ty <= 7 and ty >= 0): # checks if plays are in bounds
            fpiece = self.board[fx][fy]
            tpiece = self.board[tx][ty]

            hitpiece = False
            nx = 0
            ny = 0
            for a in [1,2,3,4,5,6]: #checks if pieces is inbetween moves
                if tx > fx + a:
                    nx = fx + a
                elif tx < fx - a:
                    nx = fx - a
                elif tx == fx:
                    nx = tx
                else:
                    break
                if ty > fy + a:
                    ny = fy + a
                elif ty < fy - a:
                    ny =  fy - a
                elif ty == fy:
                    ny = ty
                else:
                    break
                if self.board[nx][ny] != '#':
                    hitpiece = True
                    break



            if (self.turn == 'b' and fpiece.islower()) or (self.turn == 'w' and fpiece.isupper()): #checks right player is moving
                if (fpiece.islower() != tpiece.islower()) or tpiece == '#': #checks move isnt onto own piece
                    if fpiece.lower() == 'p':
                        if (fpiece.islower() and tx > fx) or (fpiece.isupper() and tx < fx): #checks moving forward
                            if (abs(fx-tx) == 1) and (abs(fy-ty) == 1) and (tpiece != '#'): #checks if attack
                                return True
                            elif (abs(fx-tx) == 1 and tpiece == '#') or (abs(fx-tx) == 2 and (fx == 1 or fx == 6) and tpiece == '#'): #checks if moving forward
                                return True
                            else:
                                return False
                        else:
                            print("No moving pawns backwards")
                            return False
                    elif fpiece.lower() == 'r':
                        if ((fx - tx == 0) or (fy - ty == 0)) and not hitpiece:
                            return True
                        else:
                            return False
                    elif fpiece.lower() == 'n':
                        if ((abs(fx - tx) == 1) and (abs(fy - ty) == 2)) or ((abs(fx - tx) == 2) and (abs(fy - ty) == 1)): #checks if doing horse things
                            return True
                        else:
                            return False
                    elif fpiece.lower() == 'b':
                        if (abs(fx-tx) == abs(fy-ty)) and not hitpiece:
                            return True
                        else:
                            return False
                    elif fpiece.lower() == 'q':
                        if ((fx - tx == 0) or (fy - ty == 0) or (abs(fx-tx) == abs(fy-ty))) and not hitpiece:
                            return True
                        else:
                            return False
                    elif fpiece.lower() == 'k':
                        if abs(fx-tx) < 2 and abs(fy-ty) < 2 and not self.ischeck(tx, ty):
                            return True
                        else:
                            return False
                else:
                    print("Almost landed on your own piece there.")
                    return False
            else:
                print("Only move your own pieces next time buddy.")
                return False
        else:
            print("Out of range.")
            return False

    def isCheck(self, x, y):
        pass #scan board and see if king is in check: use regulate to route every piece to king

    def searchistory(self):
        pass

    def run(self):
        while True:
            print("turn:", self.turn)
            self.print()
            fx = int(input("From x:"))
            fy = int(input("From y:"))
            tx = int(input("To x:"))
            ty = int(input("To y:"))
            if self.regulate(fx,fy,tx,ty):
                self.board[tx][ty] = self.board[fx][fy]
                self.board[fx][fy] = '#'
            self.changeTurn()
game = chess()
game.run()
