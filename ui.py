import tkinter as tk
import time

from game import *

class UI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Game of Life")
        self.geometry("800x600")
        self.bt_list = []
        self.game = Game(9, 13)
        self.game_board = self.game.ret_board()
        self.count = 0

    def board(self):
        for i in range(len(self.game_board)):
            self.bt_list.append([])
            row = self.bt_list[-1]
            for j in range(len(self.game_board[0])):
                if self.game_board[i][j] == 0:
                    cell = tk.Button(self, width=5)
                else:
                    cell = tk.Button(self, width=5, highlightbackground="grey")
                row.append(cell)
                cell.grid(row = i, column= j)
        tk.Button(self, text="start", command=self.change, width=5).grid(row=len(self.game_board), column=0)
        
    
    def change(self):
        print("called")
        print(self.count)
        self.count+=1
        self.game_board = self.game.new_round()
        for r in range(len(self.game_board)):
            for c in range(len(self.game_board[r])):
                if self.game_board[r][c] == 1:
                    self.bt_list[r][c].configure(highlightbackground='grey')
                else:
                    self.bt_list[r][c].configure(highlightbackground='white')
        self.bt_list[0][0].after(200, # milliseconds
                        self.change)


if __name__ == "__main__":
    life_game = UI()
    life_game.board()
    life_game.mainloop()
