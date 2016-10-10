class Piece:
  'Every piece has a physical location, a color, and a set of moves.'
  x-loc = 0
  y-loc = 0
  pieceLocation = (x-loc, y-loc)
  team = 'white' # or 'black'
  
  
class Pawn(Piece):
# RIGHT NOW I'M PROGRAMMING ONLY WITH WHITE IN MIND
  'Pawn class moves forward and attacks diagonally in front of it. Can upgrade to new class on reaching the other end of the board.'
  pieceLocation = (0, 2)
  
  def advance(pieceLocation)
    # if piece not in front:
      y-loc += 1
  
  def double-jump(pieceLocation):
    if y-loc = 2:
      # next available move can also include (y-loc) + 2
  
  def pawnStrike(pieceLocation):
    if y-loc +1 and x-loc +-1 contains a piece,
      replace that piece
      recipient piece x-loc, y-loc = 0, 0
      
      
class Rook(Piece)
  available x-loc squares = (add or subtract x-loc until you reach a piece)
    if piece is same color, stop there
     if piece is dif color, you can replace piece and send to graveyard
     
  y-loc protocol is the same
  
  
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
    x-loc = 4
    y-loc = 1
    


 King protocol
  (X+1, Y+1)
  (X+1, Y-1)
  (X-1, Y+1)
  (X-1, Y-1)
  (X+1)
  (X-1)
  (Y+1)
  (Y-1)
  
