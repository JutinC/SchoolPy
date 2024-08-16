from masterProject.chessGame import ChessGame
from masterProject.chessGUI import ChessGUI

# convert string into list of moves
def convert(string):
    li = list(string.split(" "))
    return li

originalString = "e2e4 e7e5 g1f3" # change this into the move string list from the table
moveList = convert(originalString) # converted move list
print(moveList)

# from chessGame import ChessGame
# from chessGui import ChessGUI
# def main():
#     # todo: change move list to converted list from convert function i sent earlier
#     moves = ['e2e4', 'e7e5', 'g1f3', 'b8c6', 'f1c4', 'f8c5', 'e1g1', 'h1f1', 'g8f6']
#     game = ChessGame(moves)
#     gui = ChessGUI(game)
#     gui.run()

# if __name__ == '__main__':
#     main()