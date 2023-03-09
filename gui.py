import customtkinter
from tic_tac_toe import TicTacToe

class App(customtkinter.CTk):

    def __init__(self) -> None:
        super().__init__()

        self.geometry("600x600")
        self.title("Tic Tac Toe")

        self.game = TicTacToe('X', 'O')
        self.btn_list = []

        for index in range(9):
            self.btn_list.append(customtkinter.CTkButton(master=self, width=100, height=100, text="", command=lambda index=index: self.button_callback(index)))
            self.btn_list[index].grid(row=int(index/3), column=int(index%3), padx=5, pady=5)

    def button_callback(self, index):
        game, row, col, activated_btn = self.game, int(index/3), int(index%3), self.btn_list[index]
        if activated_btn.cget("text") == "":
            activated_btn.configure(text="X")
            game.add_letter_to_board(f"{row} {col}", "X")
            if game.win(game.board) == "X":
                # TODO: pop up player 1 won, something wrong with logic p1 appears to win eventhough p2 won
                print("p1 won")
            ai_pos = game.find_best_move()
            print(ai_pos)
            ai_row, ai_col = game.split_position(ai_pos)
            ai_btn = self.btn_list[ai_row*3 + ai_col]
            ai_btn.configure(text="O")
            game.add_letter_to_board(f"{ai_row} {ai_col}", "X")
            if game.win(game.board) == "O":
                # TODO: pop up player 2 won
                print("p2 won")
        else:
            # TODO: return error message?
            pass

if __name__ == "__main__":
    app = App()
    app.mainloop()