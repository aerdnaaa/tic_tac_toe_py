from operator import index


class TicTacToe():

    def __init__(self, player_one_letter, player_two_letter):
        self.player_one = player_one_letter 
        self.player_two = player_two_letter        
        self.board = [['-', '-', '-'],['-', '-', '-'],['-', '-', '-']]
        self.scores = {'X': 1, 'O': -1, 'tie': 0}

    def win(self, board):
        # check rows for win
        for row in board:
            if row[0] == row[1] == row[2] != '-':
                return row[0]
        # check for columns:
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != '-':
                return board[0][col]
        # check for diagonals
        if board[0][0] == board[1][1] == board[2][2] != '-':
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != '-':
            return board[0][2]
        if self.empty_spaces() == []:
            return 'tie'        
        return False

    def add_letter_to_board(self, position, letter):
        row, col = position.split(' ')
        new_board = self.board.copy()        
        if new_board[int(row)][int(col)] == '-':
            new_board[int(row)][int(col)] = letter            
        self.board = new_board      

    def split_position(self, position):
        row, col = position.split(' ')
        return int(row), int(col)
    
    def empty_spaces(self):
        empty_space_list = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == '-':
                    empty_space_list.append(f'{row} {col}')
        return empty_space_list

    def empty_spaces_of_board(self, board):
        empty_space_list = []
        for row in range(3):
            for col in range(3):
                if board[row][col] == '-':
                    empty_space_list.append(f'{row} {col}')
        return empty_space_list

    def game_display_board(self):
        for row in self.board:
            print(' '.join(row))

    def minimax(self, board, depth, is_max):
        if self.win(board) != False:
            score = self.scores[self.win(board)]

            return score

        if is_max:
            best = -1000
            empty_spaces = self.empty_spaces_of_board(board)
            for empty_space in empty_spaces:
                row, col = self.split_position(empty_space)
                board[row][col] = self.player_one
                best = max(best, self.minimax(board, depth + 1, not is_max))
                board[row][col] = '-'
            return best
        else:
            best = 1000
            empty_spaces = self.empty_spaces_of_board(board)
            for empty_space in empty_spaces:
                row, col = self.split_position(empty_space)
                board[row][col] = self.player_two
                best = min(best, self.minimax(board, depth + 1, not is_max))
                board[row][col] = '-'
            return best


    def find_best_move(self):
        best_value = 1000
        best_move = ''
        empty_spaces = self.empty_spaces()
        for empty_space in empty_spaces:
            row, col = self.split_position(empty_space)
            self.board[row][col] = self.player_two
            move_value = self.minimax(self.board, 0, True)
            self.board[row][col] = '-'
            if move_value < best_value:
                best_move = empty_space
                best_value = move_value
        return best_move

def main():
    # players = {'X': '1', 'O' : '2'}
    game = TicTacToe('X', 'O')
    while True:
        player_one_position = input('(P1) Enter position of letter: ')
        game.add_letter_to_board(player_one_position, 'X')
        game.game_display_board()        
        if game.win(game.board) == 'X':
            print('Player 1 won the game.')
            break
        if game.empty_spaces() == []:
            break
        # bot will replace this player             
        player_two_position = game.find_best_move()
        game.add_letter_to_board(player_two_position, 'O')
        game.game_display_board()    
        if game.win(game.board) == 'O':
            print(f'Player 2 won the game.')
            break


# main()


# TODO: to continue, need to make sure game ends

def button_onclick(*args):
    game, col, row, btn_index = args[0], args[1], args[2], args[3]
    activated_btn = btn_list[btn_index]                
    if activated_btn.cget('text') == "":
        activated_btn.configure(text='X')
        game.add_letter_to_board(f"{row} {col}", 'X')
        if game.win(game.board) == "X":
            print('player 1 won')
        ai_position = game.find_best_move()
        row, col = game.split_position(ai_position)
        ai_btn = btn_list[row * 3 + col]
        ai_btn.configure(text='O')
        game.add_letter_to_board(ai_position, 'O')
        if game.win(game.board) == "O":
            print('player 2 won')
    else:
        # TODO: return error message?
        pass
            

def gui():

    game = TicTacToe('X', 'O')
    # current_player = 'X'

    import tkinter as tk

    root = tk.Tk()
    root.title('Tic Tac Toe')
    root.geometry('600x600')

    global btn_num, btn_list
    btn_num = 0
    btn_list = []

    for row in range(3):
        for col in range(3):
            btn_list.append(tk.Button(root, text="", bg="white", command=lambda col=col, row=row, btn_num=btn_num: button_onclick(game, col, row, btn_num)))
            btn_list[btn_num].img = tk.PhotoImage()
            btn_list[btn_num].config(height=100, width=100, image=btn_list[btn_num].img, compound=tk.CENTER)
            btn_list[btn_num].grid(column=col, row=row)

            btn_num += 1                

    root.mainloop()

# gui()