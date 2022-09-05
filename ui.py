from cgitb import text
from os import abort
import tkinter as tk
import time
from typing import Text
import threading

from game import *

class UI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Game of Life")
        self.geometry("800x600")
        self.w, self.h = self.winfo_screenwidth(), self.winfo_screenheight()
        width = 950
        height = 500
        self.geometry("%dx%d+0+0" % (width, height))
        self.bt_list = []
        self.row = 21
        self.col = 30
        self.game = Game(25, 25)
        self.game_board = self.game.ret_board()
        self.count = 0
        self.first_r = True
        self.current = []
        self.abort = False
        self.liveCells = 0

    def board(self):
        for i in range(self.row):
            self.bt_list.append([])
            row = self.bt_list[-1]
            for j in range(self.col):
                cell = tk.Button(self, width=3, highlightbackground="white", command=lambda r=i, c=j:self.select(r, c))
                row.append(cell)
                cell.grid(row = i, column= j)
        tk.Button(self, text="start", command=self.start, width=5).grid(row=self.row, column=0, columnspan=2)
        tk.Button(self, text="restart", command=self.restart, width=5).grid(row=self.row, column=2, columnspan=2)
        self.pauseBt = tk.Button(self, text="pause", command=self.pause, width=5)
        self.pauseBt.grid(row=self.row, column=4, columnspan=2)
        self.liveCount = tk.Label(self, text="There are 0 living cell", width=15)
        self.liveCount.grid(row=self.row, column=6, columnspan=15)
    
    def init_board(self):
        self.abort = False
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
            self.game_board[r][c] = 1
        else:
            self.bt_list[r][c].configure(highlightbackground='white')
            self.game_board[r][c] = 0
    
    def restart(self):
        self.abort = True
        self.clear_board()
        for i in self.game_board:
            for j in i:
                j = 0
        self.first_r = True
        self.count = 0
        self.liveCount.config(text=f"There are {0} living cell")

    
    def clear_board(self):
        for r in range(len(self.bt_list)):
            for c in range(len(self.bt_list[r])):
                self.bt_list[r][c].configure(highlightbackground='white')
    
    def pause(self):
        self.abort = not self.abort
        if self.abort == True:
            self.pauseBt.config(text="resume")
        else:
            self.pauseBt.config(text="pause")
            self.change()

    def start(self):
        if self.abort:
            self.abort = False
        self.change()

    def change(self):
        if self.abort:
            print("abort")
            return
        if self.first_r:
            print("in first round")
            self.game.read_baord(self.init_board())
            self.first_r = False
            self.abort = False
        print(f"round: {self.count}")
        self.count+=1
        self.game_board = self.game.new_round()
        self.liveCells = 0
        for r in range(len(self.game_board)):
            for c in range(len(self.game_board[r])):
                if self.game_board[r][c] == 1:
                    self.bt_list[r][c].configure(highlightbackground='grey')
                    self.liveCells += 1
                else:
                    self.bt_list[r][c].configure(highlightbackground='white')

        self.liveCount.config(text=f"There are {self.liveCells} living cells")

        self.bt_list[0][0].after(200, # milliseconds
                        self.change)


if __name__ == "__main__":
    life_game = UI()
    life_game.board()
    life_game.mainloop()
