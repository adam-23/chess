class Piece:
    """Every piece has a physical location, a color, and a set of moves."""
    def __init__(self, name):
        self.name = name
    x_loc = 0
    y_loc = 0
    pieceLocation = [(x_loc, y_loc)]
    team = 'white'  # or 'black'
    available_moves = [(0, 0), (2, 2)]

    def move_piece(self, available_moves):
        x_player_input = input('Input the x move.  ')
        y_player_input = input('Input the y move.  ')
        if [x_player_input, y_player_input] in available_moves:
            self.x_loc = x_player_input
            self.y_loc = y_player_input

    def clear_moves(self):
            self.available_moves = []

p = Piece('p2')
print(p.available_moves, p.team, p.pieceLocation)
for term in p.available_moves:
    if p.pieceLocation == term in p.available_moves:
        print("Whoo it works")


class Pawn(Piece):
    x_loc = 0
    y_loc = 2
    # RIGHT NOW I'M PROGRAMMING ONLY WITH WHITE IN MIND
    'Pawn class moves forward and attacks diagonally in front of it.'
    # Can upgrade to new class on reaching the other end of the board.'

    def advance(self, x_loc, y_loc, available_moves):
        # if piece not in front:
        available_y = (y_loc + 1)
        # if there's no piece occupying (x_loc, available_y) then add to the available moves list
        available_moves.append((x_loc, available_y))

        return

    def double_jump(self, x_loc, y_loc, available_moves):
        if y_loc == 2 and (x_loc, (y_loc + 2)):  # is not shared by any other piece:
            # available_y = y_loc +2
            # available_moves.append(x_loc, available_y)
            return
  
    def pawnStrike(self, x_loc, y_loc):
        if y_loc +1 and x_loc +-1:  # contains a piece,
            # add that move to available moves
            # replace that piece
            # recipient piece x_loc, y_loc = 0, 0
            return







"""
class Rook(Piece)
    available x_loc squares = (add or subtract x_loc until you reach a piece)
        if piece is same color, stop there
        if piece is dif color, you can replace piece and send to graveyard
     
  y_loc protocol is the same
  
  
class Bishop(Piece)
  available move protocol:
  (X+1, Y+1)*n
  (X+1, Y-1)*n
  (X-1, Y+1)*n
  (X-1, Y-1)*n
  stop once you encounter a piece
    if piece is enemy, you can replace piece and send to grave
    
    
class Queen(Piece)
  # Starting location:
    x_loc = 4
    y_loc = 1
    


 King protocol
  (X+1, Y+1)
  (X+1, Y-1)
  (X-1, Y+1)
  (X-1, Y-1)
  (X+1)
  (X-1)
  (Y+1)
  (Y-1)
  
"""