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
        for r in self.board:
            for c in r:
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

    def regulate(self,come,go):
        pass


    def run(self):
        self.print()


game = chess()
game.run()
