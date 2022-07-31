import tkinter as tk
import time

from game import *

class UI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Game of Life")
        self.geometry("800x600")
        self.w, self.h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (0.995 * self.w, 0.9 * self.h))
        self.bt_list = []
        self.row = 33
        self.col = 46
        self.game = Game(25, 25)
        self.game_board = self.game.ret_board()
        self.count = 0
        self.first_r = True
        self.current = []
        self.abort = False

    def board(self):
        for i in range(self.row):
            self.bt_list.append([])
            row = self.bt_list[-1]
            for j in range(self.col):
                cell = tk.Button(self, width=3, highlightbackground="white", command=lambda r=i, c=j:self.select(r, c))
                row.append(cell)
                cell.grid(row = i, column= j)
        tk.Button(self, text="start", command=self.change, width=5).grid(row=self.row, column=0, columnspan=2)
        tk.Button(self, text="restart", command=self.restart, width=5).grid(row=self.row, column=2, columnspan=2)
    
    def init_board(self):
        res = []
        for i in range(len(self.bt_list)):
            res.append([])
            temp = res[-1]
            for j in range(len(self.bt_list[i])):
                if self.bt_list[i][j]['highlightbackground'] == "grey": temp.append(1)
                else: temp.append(0)
        return res

    def select(self, r, c):
        if self.bt_list[r][c]["highlightbackground"] == "white":
            self.bt_list[r][c].configure(highlightbackground='grey')
        else:
            self.bt_list[r][c].configure(highlightbackground='white')
        self.abort = False
    
    def restart(self):
        self.abort = True
        self.clear_board()
        self.init_board()
        self.game_board = []
        self.first_r = True
    
    def clear_board(self):
        for r in range(len(self.bt_list)):
            for c in range(len(self.bt_list[r])):
                self.bt_list[r][c].configure(highlightbackground='white')

    def change(self):
        if self.abort:
            return
        if self.first_r:
            self.game.read_baord(self.init_board())
            self.first_r = False
        print(f"round: {self.count}")
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
