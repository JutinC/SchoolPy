from chessBoard import ChessBoard

class ChessGame:
    def __init__(self, moves):
        self.board = ChessBoard()
        self.moves = moves
        self.pieceCaptured = False
        self.current_move_index = 0
        if self.moves[0][0] == 'w':
            self.board.board.reverse()

    def advance_move(self):
        # advance move
        if self.current_move_index < len(self.moves):
            print(self.current_move_index)
            move = self.moves[self.current_move_index]
            print(move)
            self.board.update_board(move)
            self.current_move_index += 1

            # Check if a piece was captured
            if self.board.end_piece  != ' ':
                self.pieceCaptured = True
                self.captured_piece = self.board.end_piece

    def rewind_move(self):
        # go back a move
        if self.current_move_index > 0:
            self.current_move_index -= 1
            move = self.moves[self.current_move_index]

            # convert col and row into integers
            start_row = 8 - int(move[1])
            start_col = ord(move[0]) - 97
            end_row = 8 - int(move[3])
            end_col = ord(move[2]) - 97

            # Check if a piece was captured
            if self.pieceCaptured == True:
                captured_row = end_row
                captured_column = end_col
                
                # set original piece back
                original_piece = self.board.board[captured_row][captured_column]
                self.board.board[start_row][start_col] = original_piece

                # set piece captured piece back
                self.board.board[captured_row][captured_column] = self.captured_piece

                # set variables back to none
                self.captured_piece = None
                captured_column = None
                captured_row = None
                self.pieceCaptured = False
            
            else:
                # set board state back to what it was before the last move
                self.board.board[start_row][start_col] = self.board.board[end_row][end_col]
                self.board.board[end_row][end_col] = ' '

        elif self.current_move_index == 0:
            # If already at the first move, just set the board state back to what it was before the last move
            self.current_move_index = 0

            # set board state back to what it was before the last move
            self.board.board[start_row][start_col] = self.board.board[end_row][end_col]
            self.board.board[end_row][end_col] = ' '