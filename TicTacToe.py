class TicTacToe(object):

    def __init__(self):
        super(TicTacToe, self).__init__()
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.winner = ' '
        print("className.runGame -> command to begin a game of TicTacToe!")
        print()

    def runGame(self):
        self.printBoard()
        currentSym = 'o'
        while(True):

            if(currentSym == 'o'):
                currentSym = 'x'
            else:
                currentSym = 'o'
            row = 5
            while(row > 2 or row < 0):
                row = int(input("row? "))
            column = 5
            while(column > 2 or column < 0):
                column = int(input("column? "))
            self.placeSymbol(currentSym, (row, column))
            self.printBoard()
            if(self.checkFinished() != ' '):
                break

        print(self.winner + " has won the game!!")

    def checkFinished(self):

        for i in range(3):
            tempList = self.board[i].copy()
            tempList.sort()
            if(tempList[0] == ' '):
                continue
            else:
                if(tempList[1] == tempList[2] == tempList[0]):
                    self.winner = tempList[0]

        if(self.winner == ' '):
            if((self.board[0][0] == self.board[1][1] == self.board[2][2]) | (self.board[2][0] == self.board[0][2] == self.board[1][1])):
                self.winner = self.board[1][1]

        return self.winner

    def printBoard(self):
        for i in range(3):
            lineprint = ""
            for j in range(3):
                lineprint += "| " + self.board[i][j] + " "

            print(lineprint + "|")

        print()

    def placeSymbol(self, symbol, position):
        (y, x) = position

        self.board[y][x] = symbol


myGame = TicTacToe()
myGame.runGame()
