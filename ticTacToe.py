#Caroline LaVersa
#Tic Tac Toe
#12/31/2021 -- Happy New Year's Eve!

class Board:
    def __init__(self, width=3, height=3):
        self.width = width
        self.height = height
        self.spaces = {'1':[0,0], '2':[0,1], '3':[0,2], '4':[1,0], '5':[1,1], '6':[1,2], '7':[2,0], '8':[2,1], '9':[2,2]}
        def build(self):
            '''returns 2d array (board) with 'height' rows and 'width' columns'''
            board = []
            x = 1
            while x<10:
                for row in range(height): #loops through number rows
                    fullRow = []
                    for col in range(width): #creates space at every index of column in a row
                        fullRow += [str(x)]
                        x+=1
                    board += [fullRow]
            return board
        self.board = build(self) #reference object for every subsequent board method


    def _str__(self):
        '''returns Board object in string form'''
        board = ''
        for row in self.board:
            board += '|'
            for col in row:
                board = board + str(col) + '|'
            board = board + '\n'
        print(board)


    def possibleMove(self, spaceNum):
        '''checks if move is valid. returns true if valid, false if not. valid if space is empty'''
        if int(spaceNum)>9 or int(spaceNum)<1:
            return False
        else:
            coord = self.spaces[spaceNum]
            row = coord[0]
            col = coord[1]
            if self.board[row][col]!='O' and self.board[row][col]!='X':
                return True
            elif self.board[row][col]=='O' and self.board[row][col]!='X': 
                return False
            else:
                return False

    def makeMove(self, spaceNum, player):
        '''sets space col row of users 2choice with user's symbol, string player, either 'O' or 'X''' 
        coord = self.spaces[spaceNum]
        row = coord[0]
        col = coord[1]
        if Board.possibleMove(self, spaceNum) == True:
            self.board[row][col] = player

    def wVert(self, player):
        '''returns True if user, string player, has won with three in a row in the vertical direction. else False.'''
        if self.board[self.spaces['1'][0]][self.spaces['1'][1]]== player and self.board[self.spaces['4'][0]][self.spaces['4'][1]]==player and self.board[self.spaces['7'][0]][self.spaces['7'][1]] == player:
            return True
        elif self.board[self.spaces['2'][0]][self.spaces['2'][1]]== player and self.board[self.spaces['5'][0]][self.spaces['5'][1]]==player and self.board[self.spaces['8'][0]][self.spaces['8'][1]] == player:
            return True
        elif self.board[self.spaces['3'][0]][self.spaces['3'][1]]== player and self.board[self.spaces['6'][0]][self.spaces['6'][1]]==player and self.board[self.spaces['9'][0]][self.spaces['9'][1]] == player:
            return True
        else:
            return False

    def wHor(self, player):
        '''returns True if user, string player, has won with three in a row in the horizontal direction. else False.'''
        if self.board[self.spaces['1'][0]][self.spaces['1'][1]]== player and self.board[self.spaces['2'][0]][self.spaces['2'][1]]==player and self.board[self.spaces['3'][0]][self.spaces['3'][1]] == player:
            return True
        elif self.board[self.spaces['4'][0]][self.spaces['4'][1]]== player and self.board[self.spaces['5'][0]][self.spaces['5'][1]]==player and self.board[self.spaces['6'][0]][self.spaces['6'][1]] == player:
            return True
        elif self.board[self.spaces['7'][0]][self.spaces['7'][1]]== player and self.board[self.spaces['8'][0]][self.spaces['8'][1]]==player and self.board[self.spaces['9'][0]][self.spaces['9'][1]] == player:
            return True
        else:
            return False
        
    def wDiag(self, player):
        '''returns True if user, string player, has won with three in a row in the diagonal direction. else False.'''
        if self.board[self.spaces['1'][0]][self.spaces['1'][1]]== player and self.board[self.spaces['5'][0]][self.spaces['5'][1]]==player and self.board[self.spaces['9'][0]][self.spaces['9'][1]] == player:
            return True
        elif self.board[self.spaces['3'][0]][self.spaces['3'][1]]== player and self.board[self.spaces['5'][0]][self.spaces['5'][1]]==player and self.board[self.spaces['7'][0]][self.spaces['7'][1]] == player:
            return True
        else:
            return False
    def wins(self, player):
        '''returns True if user, string player either 'O' or 'X', has won with three in a row in any direction. else False.'''
        if Board.wVert(self, player) == True or Board.wHor(self, player)== True or Board.wDiag(self, player) == True:
            return True
        else:
            return False

    def gameOver(self):
        '''returns True if there are no other valid moves to make; ex. when all spaces are filled'''
        count = 0
        for item in self.spaces.items():
            coord = item[1]

            if self.board[coord[0]][coord[1]] == "X" or self.board[coord[0]][coord[1]]== "O":
                count+=1
        if count ==9:
            return True
        else:
            return False

    def play(self):
        '''board method; runs loop that plays game'''
        print("Are you ready to play Tic-Tac-Toe?..")
        Board._str__(self)
        while True: #infinite loop until break that runs the game
            oPlay = input("Player O, enter the space number you would like to play: ")
            while Board.possibleMove(self, oPlay) == False:
                Board._str__(self)
                oPlay = input("Player O, enter a valid space number: ")
            Board.makeMove(self, str(oPlay), 'O')
            Board._str__(self)
            if Board.wins(self, 'O') == True:
                print("O wins!")
                break
            if Board.gameOver(self)==True:
                print("Oops! No more moves;  it's a tie!")
                break
            xPlay = input("Player X, enter the space number you would like to play: ")
            while Board.possibleMove(self, xPlay) == False:
                Board._str__(self)
                xPlay = input("Player X, enter a valid space number: ")
            Board.makeMove(self, str(xPlay), 'X')
            Board._str__(self)
            if Board.wins(self, 'X') == True:
                print("X wins!")
                break
            
        





        
