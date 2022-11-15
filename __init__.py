from random import choice, sample

from pieces import *

class ChessSweeper():

    def __init__(self):
        self.pieceDictionary = {
            'R': ['♜', 'rook'],
            'Q': ['♛', 'queen'],
            'B': ['♝', 'bishop'],
            'N': ['♞', 'knight'],
            'K': ['♚', 'king'],
            'P': ['♟', 'pawn']
        }
        self.askStart()
        
    def askStart(self):
        if 'p' == input('Welcome to ChessSweeper! Press "p" to start a game: ').lower():
            self.startGame()
        else:
            print('Quitting ChessSweeper.')
                
    def placePieces(self):
        numPieces = 16 # EDITABLE
        numRevealed = 32 # EDITABLE
        possiblePlaces = [i for i in range(self.boardSize ** 2)]
        places = sample(possiblePlaces, numPieces+numRevealed)
        for loc in places[:numPieces]:
            row, col = loc // self.boardSize, loc % self.boardSize
            piece = choice(['Queen' for _ in range(self.weights[0])] +
                           ['Rook' for _ in range(self.weights[1])] +
                           ['Bishop' for _ in range(self.weights[2])] +  
                           ['Knight' for _ in range(self.weights[3])] +
                           ['Pawn' for _ in range(self.weights[4])] +
                           ['King' for _ in range(self.weights[5])])
            newPiece = eval(f'{piece}({row}, {col})')
            self.hiddenBoard[row][col] = newPiece
        for row in range(self.boardSize):
            for col in range(self.boardSize):
                if isinstance(self.hiddenBoard[row][col], Piece):
                    for r, c in self.hiddenBoard[row][col].findMoves(self.hiddenBoard):
                        self.hiddenBoard[r][c] += 1
        for loc in places[numPieces:]:
            row, col = loc // self.boardSize, loc % self.boardSize
            self.playerBoard[row][col] = self.hiddenBoard[row][col]

    def display(self, view='player'):
        rows = iter(['8', '7', '6', '5', '4', '3', '2', '1'])
        if view == 'hidden':
            for row in self.hiddenBoard:
                print('{} ['.format(next(rows)), end='')
                for i in range(self.boardSize - 1):
                    print('{} '.format(row[i]), end='')
                print('{}]'.format(row[-1]))    
            print('   a b c d e f g h')        
        else:
            for row in self.playerBoard:
                print('{} ['.format(next(rows)), end='')
                for i in range(self.boardSize - 1):
                    print('{} '.format(row[i]), end='')
                print('{}]'.format(row[-1]))    
            print('   a b c d e f g h') 
    
    def checkWon(self):
        for row in range(self.boardSize):
            for col in range(self.boardSize):
                item = self.playerBoard[row][col]
                if item != self.hiddenBoard[row][col]:
                    return False
        return True 

    def startGame(self):
        self.lives = 5 # EDITABLE
        self.boardSize = 8
        self.playerBoard = [['_' for _ in range(self.boardSize)] for _ in range(self.boardSize)]
        self.flagMode = False       
        self.hiddenBoard = [[0 for _ in range(self.boardSize)] for __ in range(self.boardSize)]
        self.weights = [7, 5, 3, 3, 2, 1] # EDITABLE: Q, R, B, N, P, K weights
        self.placePieces()
        self.playGame()

    def validated(self, move):
        if move.lower() == 'q':
            return True
        elif len(move) == 2 and move[0].lower() in 'abcdefgh' and move[1] in '12345678':
            return True
        elif len(move) == 3 and move[0].lower() in 'abcdefgh' and move[1] in '12345678' and move[2].upper() in 'QKNPBR':
            return True
        return False

    def playGame(self):
        quit = False
        while not quit:
            if self.lives == 0:
                print('You ran out of lives! This was the solution: ')
                self.display('hidden')
                break
            elif self.checkWon():
                print('Congratulations! You solved the board with {} lives left.'.format(self.lives))
                self.display('hidden')                
                break
            else:
                self.display('player')
                move = ''
                while not self.validated(move):
                    move = input('Make your next move. You have {} lives left. Press q to quit: '.format(self.lives))
                if move.lower() == 'q':                        
                    print('Quitting game. Here was the solution: ')
                    self.display('hidden')
                    quit = True
                    break
                else:
                    col = ord(move[0]) - 97
                    row = 8 - int(move[1]) 
                    if len(move) == 3:
                        piece = move[2]
                        print(piece)
                        self.attemptMark(row, col, piece)
                    else:
                        self.attemptMove(row, col)
        if not quit:
            self.askStart()
    
    def attemptMark(self, row, col, piece):
        if isinstance(self.playerBoard[row][col], int):
            print('Square is already revealed!')
        else:
            piece = self.pieceDictionary[piece.upper()]
            self.playerBoard[row][col] = piece[0]
            row = self.boardSize - row
            col = chr(col + 97)
            print('Marked square {}{} with piece {}'.format(col, row, piece[1]))
    
    def attemptMove(self, row, col):
        if isinstance(self.playerBoard[row][col], int):
            print('Square is already revealed!')
        elif isinstance(self.hiddenBoard[row][col], int):
            self.playerBoard[row][col] = self.hiddenBoard[row][col]
        else:
            self.lives -= 1
            self.playerBoard[row][col] = '!'
            row = self.boardSize - row
            col = chr(col + 97)
            print('Oh no! Square {}{} has a piece, now marked by a !.'.format(col, row))          
            
if __name__ == "__main__":
    game = ChessSweeper()
    