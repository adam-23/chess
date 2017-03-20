"""Python file used for unit-testing."""
from chess_classes import Player

p1 = Player()
p2 = Player()
p1.ask_player_name()
p2.ask_player_name()
p1.input_move()
p2.input_move()

"""
a = [1, 2]
b = [2, 3]
print_this = [a, b]
print(print_this)
if 3 in print_this:
    print("HELLO")
for item in print_this:
    if 1 in item:
        print("I am in" + str(item))
# USE THIS TO CHECK IF MOVES ARE POSSIBLE/valid
"""
