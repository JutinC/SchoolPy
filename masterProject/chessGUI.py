from chessBoard import ChessBoard
import tkinter as tk

class ChessGUI:
    # initialize class with game and main window
    def __init__(self, game, mainWin):
        self.mainWin = mainWin
        self.board = ChessBoard()
        self.game = game
        self.boardWin = tk.Toplevel(mainWin)
        self.board_frame = tk.Frame(self.boardWin)
        self.move_label = tk.Label(self.boardWin, text=f"Move {self.game.current_move_index+1}/{len(self.game.moves)}")
        self.prev_button = tk.Button(self.boardWin, text="Previous", command=self.go_to_prev_move)
        self.next_button = tk.Button(self.boardWin, text="Next", command=self.go_to_next_move)
        self.display_board()

    # display current state of the board
    def display_board(self):
        # Grid display for the GUI (Board up top, and next/prev buttons on the button, in the middle is the move counter)
        self.board_frame.destroy()
        self.board_frame = tk.Frame(self.boardWin)
        self.game.board.display_board(self.board_frame)
        self.board_frame.grid(row=0, column = 0, columnspan = 3, padx = (50, 0))

        self.move_label.config(text=f"Move {self.game.current_move_index}/{len(self.game.moves)}")
        self.move_label.grid(row = 1, column = 1)

        self.prev_button.grid(row = 1, column = 0, padx = (0, 50))
        self.next_button.grid(row = 1, column = 3, padx = (0, 10))

    def go_to_prev_move(self):
        # rewind the game to the previous move
        self.game.rewind_move()
        self.display_board()

    def go_to_next_move(self):
        # advance the game to the next move
        self.game.advance_move()
        self.display_board()

    def run(self):
        self.boardWin.mainloop()