import random
from time import sleep
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
        self.turn = 'W'

    def print(self):
        print("  01234567",sep='',end='\n')
        for rpos, r in enumerate(self.board):
            print(rpos,sep='',end=' ')
            for cpos, c in enumerate(r):
                print(c,sep='',end='')
            print("\n",sep='',end='')

    def store(self):
        with open("board.txt","w") as file:
            file.write(self.turn+'\n')
            file.write(str(self.board))

    def changeTurn(self):
        if self.turn == 'W':
            self.turn = 'b'
        else:
            self.turn = 'W'

    def regulate(self,fx,fy,tx,ty, checkplayer = True):
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



            if not checkplayer or (((self.turn == 'b' and (fpiece.islower())) or (self.turn == 'W' and fpiece.isupper()))): #checks right player is moving
                if (fpiece.islower() != tpiece.islower()) or tpiece == '#': #checks move isnt onto own piece
                    if fpiece.lower() == 'p':
                        if (fpiece.islower() and tx > fx) or (fpiece.isupper() and tx < fx): #checks moving forward
                            if (abs(fx-tx) == 1) and (abs(fy-ty) == 1) and (tpiece != '#'): #checks if attack
                                return True
                            elif (abs(fx-tx) == 1 and tpiece == '#' and fy == ty) or (abs(fx-tx) == 2 and (fx == 1 or fx == 6) and tpiece == '#' and fy == ty): #checks if moving forward
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
                        if abs(fx-tx) < 2 and abs(fy-ty) < 2 and not self.isCheck(tx, ty):
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

    def isCheck(self, isx, isy):
        for ypos, y in enumerate(self.board):
            for xpos, x in enumerate(y):
                if x != '#' and (x.islower() != self.turn.islower()):
                    if self.regulate(ypos, xpos, isy, isx, False):
                        return True
        return False

    def searchistory(self):
        pass

    def run(self):
        self.print()
        while True:
            print("turn:", self.turn)
            fx = int(random.randint(0,7))
            fy = int(random.randint(0,7))
            tx = int(random.randint(0,7))
            ty = int(random.randint(0,7))
            if self.regulate(fx,fy,tx,ty):
                self.board[tx][ty] = self.board[fx][fy]
                self.board[fx][fy] = '#'
                self.print()
                self.store()
                sleep(10)
            self.changeTurn()
game = chess()
game.run()
