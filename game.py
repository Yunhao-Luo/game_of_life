import time

class Game:

    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.board = []
        for i in range(r):
            self.board.append([0]*c)

        self.board = [[0,1,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                      [1,1,1,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [1,1,1,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        self.r = len(self.board)
        self.c = len(self.board[0])
    
    def print_board(self):
        for i in self.board:
            print(i)
    
    def check_surounding(self, r, c):
        count = 0
        left, right, top, bottom = False, False, False, False
        if c == 0:
            left = True
        if c == self.c-1:
            right = True
        if r == 0:
            top = True
        if r == self.r-1:
            bottom = True
        
        if top and left:
            return self.board[r][c+1] + self.board[r+1][c+1] + self.board[r+1][c]
        if bottom and left:
            return self.board[r-1][c] + self.board[r-1][c+1] + self.board[r][c+1]
        if top and right:
            return self.board[r][c-1] + self.board[r+1][c-1] + self.board[r+1][c]
        if bottom and right:
            return self.board[r-1][c] + self.board[r-1][c-1] + self.board[r][c-1]
        if top:
            return self.board[r][c-1] + self.board[r+1][c-1] + self.board[r+1][c] + self.board[r+1][c+1] + self.board[r][c+1]
        if bottom:
            return self.board[r][c-1] + self.board[r-1][c-1] + self.board[r-1][c] + self.board[r-1][c+1] + self.board[r][c+1]
        if left:
            return self.board[r-1][c] + self.board[r-1][c+1] + self.board[r][c+1] + self.board[r+1][c+1] + self.board[r+1][c]
        if right:
            return self.board[r-1][c] + self.board[r-1][c-1] + self.board[r][c-1] + self.board[r+1][c-1] + self.board[r+1][c]
        return self.board[r-1][c] + self.board[r-1][c-1] + self.board[r][c-1] + self.board[r+1][c-1] + self.board[r+1][c] + self.board[r+1][c+1] + self.board[r][c+1] + self.board[r-1][c+1]
        
    def new_round(self):
        death_update = []
        life_update = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] == 1 and self.check_surounding(r, c) < 2:
                    death_update.append([r, c])
                if self.board[r][c] == 1 and self.check_surounding(r, c) > 3:
                    death_update.append([r, c])
                if self.board[r][c] == 0 and self.check_surounding(r, c) == 3:
                    life_update.append([r, c])
        for d in death_update:
            self.board[d[0]][d[1]] = 0
        for l in life_update:
            self.board[l[0]][l[1]] = 1

        return self.board

    def ret_board(self):
        return self.board
    
    def start(self):
        while self.board != [[0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0]]:
            self.new_round()
            time.sleep(1)
            print("new round")
            self.print_board()




if __name__ == "__main__":
    test = Game(5, 10)
    test.print_board()
    #test.start()