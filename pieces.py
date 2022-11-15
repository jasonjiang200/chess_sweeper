class Piece():
    def __init__(self, row, col):
        self.dirs = []
        self.row, self.col = row, col
        self.moveLimit = 7
        self.symbol = ''

    def __repr__(self):
        return self.symbol

    def findMoves(self, board):
        moves = []
        for dir in self.dirs:
            row, col = self.row, self.col
            hitPiece = False
            numMoves = 0
            while numMoves < self.moveLimit and not hitPiece:
                row += dir[0]
                col += dir[1]
                if not((0 <= row < 8) and (0 <= col < 8)) or isinstance(board[row][col], Piece):
                    hitPiece = True
                else:
                    numMoves += 1
                    moves.append((row, col)) 
        return moves

    def __eq__(self, other):
        if isinstance(other, str):
            return self.symbol == other

class Rook(Piece):

    def __init__(self, row, col):
        super().__init__(row, col)
        self.dirs = [[-1, 0], [1, 0],[0, 1], [0, -1]]
        self.symbol = '♜'
    
class Queen(Piece):

    def __init__(self, row, col):
        super().__init__(row, col)
        self.dirs = [[-1, 0], [1, 0],[0, 1], [0, -1], [-1, -1], [-1, 1], 
                        [1, 1], [1, -1]]
        self.symbol = '♛'

class Pawn(Piece):

    def __init__(self, row, col):
        super().__init__(row, col)
        self.dirs = [[-1, -1], [-1, 1]]
        self.moveLimit = 1
        self.symbol = '♟'

class Bishop(Piece):

    def __init__(self, row, col):
        super().__init__(row, col)
        self.dirs = [[-1, -1], [-1, 1], [1, 1], [1, -1]]
        self.symbol = '♝'

class Knight(Piece):

    def __init__(self, row, col):
        super().__init__(row, col)
        self.dirs = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], 
                     [-1, 2], [-1, -2]]
        self.moveLimit = 1
        self.symbol = '♞'
        
class King(Piece):

    def __init__(self, row, col):
        super().__init__(row, col)
        self.dirs = [[-1, 0], [1, 0],[0, 1], [0, -1], [-1, -1], [-1, 1], 
                     [1, 1], [1, -1]]
        self.moveLimit = 1
        self.symbol = '♚'