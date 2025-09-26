from tkinter import *
from tkinter import messagebox
import random
import time

class Board:
    bg_color = {
        '2': '#eee4da',
        '4': '#ede0c8',
        '8': '#f2b179',
        '16': '#f59563',
        '32': '#f67c5f',
        '64': '#f65e3b',
        '128': '#edcf72',
        '256': '#edcc61',
        '512': '#edc850',
        '1024': '#edc53f',
        '2048': '#edc22e',
        '4096': '#3c3a32',
        '8192': '#3c3a32'
    }
    
    color = {
        '2': '#776e65',
        '4': '#776e65',
        '8': '#f9f6f2',
        '16': '#f9f6f2',
        '32': '#f9f6f2',
        '64': '#f9f6f2',
        '128': '#f9f6f2',
        '256': '#f9f6f2',
        '512': '#f9f6f2',
        '1024': '#f9f6f2',
        '2048': '#f9f6f2',
        '4096': '#f9f6f2',
        '8192': '#f9f6f2'
    }
    
    font_sizes = {
        1: ('arial', 22, 'bold'),
        2: ('arial', 20, 'bold'),
        3: ('arial', 18, 'bold'),
        4: ('arial', 16, 'bold'),
        5: ('arial', 14, 'bold')
    }

    def __init__(self):
        self.window = Tk()
        self.window.title('2048 - Enhanced Edition')
        self.window.configure(bg='#faf8ef')
        self.window.resizable(False, False)
        
        # Header with score
        self.header = Frame(self.window, bg='#faf8ef', pady=10)
        self.header.pack()
        
        title = Label(self.header, text='2048', font=('arial', 40, 'bold'), 
                     bg='#faf8ef', fg='#776e65')
        title.grid(row=0, column=0, padx=20)
        
        # Score frame
        self.score_frame = Frame(self.header, bg='#bbada0', padx=10, pady=5)
        self.score_frame.grid(row=0, column=1, padx=20)
        
        self.score_label = Label(self.score_frame, text='SCORE', font=('arial', 12, 'bold'),
                                bg='#bbada0', fg='#eee4da')
        self.score_label.pack()
        
        self.score_value = Label(self.score_frame, text='0', font=('arial', 20, 'bold'),
                                bg='#bbada0', fg='white')
        self.score_value.pack()
        
        # Game area
        self.game_area = Frame(self.window, bg='#bbada0', padx=10, pady=10)
        self.game_area.pack(pady=10)
        
        # Instructions
        self.instructions = Label(self.window, 
                                 text='Use arrow keys to move. Combine tiles with the same number to reach 2048!',
                                 font=('arial', 10), bg='#faf8ef', fg='#776e65')
        self.instructions.pack(pady=5)
        
        # New game button
        self.new_game_btn = Button(self.window, text='New Game', font=('arial', 12, 'bold'),
                                  bg='#8f7a66', fg='white', command=self.new_game)
        self.new_game_btn.pack(pady=10)
        
        self.board = []
        self.gridCell = [[0] * 4 for _ in range(4)]
        self.compress = False
        self.merge = False
        self.moved = False
        self.score = 0
        self.best_score = 0
        
        # Create game grid
        for i in range(4):
            rows = []
            for j in range(4):
                # Background tile
                bg_tile = Frame(self.game_area, width=80, height=80, bg='#cdc1b4')
                bg_tile.grid(row=i, column=j, padx=5, pady=5)
                bg_tile.grid_propagate(False)
                
                # Number tile
                l = Label(bg_tile, text='', font=('arial', 22, 'bold'), width=4, height=2)
                l.pack(expand=True)
                rows.append(l)
            self.board.append(rows)
        
        self.new_game()

    def get_font_size(self, number):
        digits = len(str(number))
        return self.font_sizes.get(digits, self.font_sizes[5])

    def paint_grid(self):
        for i in range(4):
            for j in range(4):
                value = self.gridCell[i][j]
                if value == 0:
                    self.board[i][j].config(text='', bg='#cdc1b4', fg='#776e65')
                else:
                    font_size = self.get_font_size(value)
                    self.board[i][j].config(text=str(value), font=font_size,
                                          bg=self.bg_color.get(str(value), '#3c3a32'),
                                          fg=self.color.get(str(value), '#f9f6f2'))
        
        # Update score
        self.score_value.config(text=str(self.score))
        
        # Update best score
        if self.score > self.best_score:
            self.best_score = self.score

    def reverse(self):
        for ind in range(4):
            i, j = 0, 3
            while i < j:
                self.gridCell[ind][i], self.gridCell[ind][j] = self.gridCell[ind][j], self.gridCell[ind][i]
                i += 1
                j -= 1

    def transpose(self):
        self.gridCell = [list(t) for t in zip(*self.gridCell)]

    def compress_grid(self):
        self.compress = False
        temp = [[0] * 4 for _ in range(4)]
        for i in range(4):
            cnt = 0
            for j in range(4):
                if self.gridCell[i][j] != 0:
                    temp[i][cnt] = self.gridCell[i][j]
                    if cnt != j:
                        self.compress = True
                    cnt += 1
        self.gridCell = temp

    def merge_grid(self):
        self.merge = False
        for i in range(4):
            for j in range(3):
                if self.gridCell[i][j] == self.gridCell[i][j + 1] and self.gridCell[i][j] != 0:
                    self.gridCell[i][j] *= 2
                    self.gridCell[i][j + 1] = 0
                    self.score += self.gridCell[i][j]
                    self.merge = True

    def random_cell(self):
        cells = []
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j] == 0:
                    cells.append((i, j))
        
        if cells:
            i, j = random.choice(cells)
            # 90% chance for 2, 10% chance for 4
            self.gridCell[i][j] = 2 if random.random() < 0.9 else 4
            return True
        return False

    def can_merge(self):
        for i in range(4):
            for j in range(3):
                if self.gridCell[i][j] == self.gridCell[i][j + 1]:
                    return True
        
        for i in range(3):
            for j in range(4):
                if self.gridCell[i + 1][j] == self.gridCell[i][j]:
                    return True
        return False

    def is_game_over(self):
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j] == 0:
                    return False
        return not self.can_merge()

    def new_game(self):
        self.gridCell = [[0] * 4 for _ in range(4)]
        self.score = 0
        self.random_cell()
        self.random_cell()
        self.paint_grid()

class Game:
    def __init__(self, gamepanel):
        self.gamepanel = gamepanel
        self.end = False
        self.won = False
        self.animation_speed = 50  # milliseconds

    def start(self):
        self.gamepanel.window.bind('<Key>', self.link_keys)
        self.gamepanel.window.mainloop()

    def animate_move(self, direction):
        # Simple animation by updating the display
        self.gamepanel.paint_grid()
        self.gamepanel.window.update()

    def link_keys(self, event):
        if self.end or self.won:
            return

        pressed_key = event.keysym
        valid_moves = ['Up', 'Down', 'Left', 'Right']

        if pressed_key not in valid_moves:
            return

        self.gamepanel.compress = False
        self.gamepanel.merge = False
        self.gamepanel.moved = False

        original_grid = [row[:] for row in self.gamepanel.gridCell]

        if pressed_key == 'Up':
            self.gamepanel.transpose()
            self.gamepanel.compress_grid()
            self.gamepanel.merge_grid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compress_grid()
            self.gamepanel.transpose()

        elif pressed_key == 'Down':
            self.gamepanel.transpose()
            self.gamepanel.reverse()
            self.gamepanel.compress_grid()
            self.gamepanel.merge_grid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compress_grid()
            self.gamepanel.reverse()
            self.gamepanel.transpose()

        elif pressed_key == 'Left':
            self.gamepanel.compress_grid()
            self.gamepanel.merge_grid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compress_grid()

        elif pressed_key == 'Right':
            self.gamepanel.reverse()
            self.gamepanel.compress_grid()
            self.gamepanel.merge_grid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compress_grid()
            self.gamepanel.reverse()

        # Animate the move
        self.animate_move(pressed_key)

        # Check for win
        for i in range(4):
            for j in range(4):
                if self.gamepanel.gridCell[i][j] == 2048 and not self.won:
                    self.won = True
                    messagebox.showinfo('2048', 'Congratulations! You reached 2048!\nKeep going to get higher scores!')
                    break

        # Add new tile if moved
        if self.gamepanel.moved:
            self.gamepanel.random_cell()
            self.gamepanel.paint_grid()

        # Check game over
        if self.gamepanel.is_game_over():
            self.end = True
            messagebox.showinfo('2048', f'Game Over!\nYour score: {self.gamepanel.score}')

# Start the game
if __name__ == "__main__":
    gamepanel = Board()
    game2048 = Game(gamepanel)
    game2048.start()
