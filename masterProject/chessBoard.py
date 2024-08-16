import tkinter as tk

class ChessBoard:
    def __init__(self):
        # chess starting position
        self.board = [
            ['B♖', 'B♘', 'B♗', 'B♕', 'B♔', 'B♗', 'B♘', 'B♖'],
            ['B♙', 'B♙', 'B♙', 'B♙', 'B♙', 'B♙', 'B♙', 'B♙'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['W♙', 'W♙', 'W♙', 'W♙', 'W♙', 'W♙', 'W♙', 'W♙'],
            ['W♜', 'W♞', 'W♝', 'W♛', 'W♚', 'W♝', 'W♞', 'W♜']
        ]

    def update_board(self, move):
        # convert move to board coordinates
        start_row = 8 - int(move[1])
        start_col = ord(move[0]) - 97
        end_row = 8 - int(move[3])
        end_col = ord(move[2]) - 97
        print(f"start col: {start_col}, start row: {start_row}, end col: {end_col}, end row {end_row}")
        self.end_piece = self.board[end_row][end_col]
        print(f"end piece: {self.board[end_row][end_col]}")

        # Update board state
        self.board[end_row][end_col] = self.board[start_row][start_col]
        self.board[start_row][start_col] = ' '

    def display_board(self, frame):
        # create chess board
        for i in range(8):
            for j in range(8):
                tile_color = "#eae9d2" if (i+j)%2==0 else "#4b7399"
                lbl = tk.Label(frame, text=self.board[i][j], bg=tile_color, fg='black', width=4, height=2)
                lbl.grid(row=i+1, column=j)

        # display row numbers
        for i in range(8):
            lbl = tk.Label(frame, text=str(8-i), fg='black', width=4, height=2)
            lbl.grid(row=i+1, column=8)

        # display column letters
        for j, letter in enumerate("abcdefgh"):
            lbl = tk.Label(frame, text=letter, fg='black', width=4, height=2)
            lbl.grid(row=9, column=j)