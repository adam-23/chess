class Piece:
    """Every piece has a physical location, a color, and a set of moves."""
    def __init__(self, name):
        self.name = name
    x_loc = 0
    y_loc = 0
    team = '(white)'  # or 'black'
    available_moves = []

    def move_piece(self, available_moves):
        x_player_input = input('Input the x move.  ') #Or: X: 
        y_player_input = input('Input the y move.  ')
        if [x_player_input, y_player_input] in available_moves:
            self.x_loc = x_player_input
            self.y_loc = y_player_input

    def clear_moves(self):
        self.available_moves = []

    def status_check(self):
        print(self.name, self.team, "x =", self.x_loc, "y =", self.y_loc)

p = Piece('test piece 1')
p.status_check()
if p.available_moves == []:
    print("Available moves are empty.")


class Pawn(Piece):
    def __init__(self, x_loc, y_loc, name):
        super().__init__(name)
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.name = name
    # RIGHT NOW I'M PROGRAMMING ONLY WITH WHITE IN MIND
    'Pawn class moves forward and attacks diagonally in front of it.'
    # Can upgrade to new class on reaching the other end of the board.'

    @staticmethod
    def advance(x_loc, y_loc, available_moves):
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
  
    """def pawnStrike(self, x_loc, y_loc):
        if y_loc +1 and x_loc +-1:  # contains a piece,
            # add that move to available moves
            # replace that piece
            # recipient piece x_loc, y_loc = 0, 0
            return"""

pawn1 = Pawn(1, 2, "pawn1")
pawn1.status_check()
pawn1.advance(pawn1.x_loc, pawn1.y_loc, pawn1.available_moves)
pawn1.status_check()
print(pawn1.available_moves)








"""
-  

-[Load White moves]
-For 1st player, load moves
-    Available moves should be loaded right at the beginning of the game
-    load pawn moves
-    rook
-    knight
-    bishop
-    queen
-    king
-  
-[Check protocol] 
-    removes available moves that would keep king in check OR put king in check
-    
-    if no moves are left, checkmate activates and game is over
-   
-  
-[White player enters move]
-  
-[game checks if move is in available white moves]
-    if not, ask player again for moves
-
-[Change Piece Location]
-[If possible, remove enemy to graveyard]
-[Start opposing king check if applicable]
-------------
-[Load Available Black Moves]
-  pawn
-  rook
-  knight
-  bishop
-  queen
-  king
-
-[Check Protocol]
-
-[Black Player enters move]
-
-[Game checks if player entered move is in available moves list
-    if not, ask player again for move
-    if yes, change piece location
-        if piece shares location with enemy piece after move, change enemy piece status to dead and remove from board
 
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
