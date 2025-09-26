# 2048 Game - Python Implementation

A complete implementation of the classic 2048 puzzle game using Python and Tkinter for the graphical interface.

## Game Overview

2048 is a sliding tile puzzle game where players combine numbered tiles on a 4x4 grid to create a tile with the number 2048. The game challenges your strategic thinking and planning skills.

### Features
- **Clean GUI**: Colorful, intuitive interface with smooth animations
- **Score Tracking**: Real-time score display with best score tracking
- **Game States**: Win detection (2048 tile) and game over conditions
- **Responsive Controls**: Keyboard arrow key controls
- **New Game Option**: Restart anytime with the New Game button

## How to Play

### Basic Rules
- **Goal**: Combine tiles to create a **2048** tile
- **Movement**: Use arrow keys (↑, ↓, ←, →) to slide tiles
- **Merging**: Two identical tiles merge into their sum when they collide
- **New Tiles**: After each move, a new tile (90% chance of 2, 10% chance of 4) appears
- **Game Over**: When the board is full and no moves are possible

### Controls
- **↑** Up Arrow - Move tiles upward
- **↓** Down Arrow - Move tiles downward
- **←** Left Arrow - Move tiles left
- **→** Right Arrow - Move tiles right

### Strategy Tips
1. **Corner Strategy**: Keep your highest number in a corner
2. **Plan Ahead**: Think 2-3 moves in advance
3. **Chain Merges**: Set up multiple merges in one move
4. **Avoid Random Moves**: Have a consistent movement pattern

##  Code Architecture

### Project Structure
```
2048-game/
│
├── 2048_game.py          # Main game file
├── README.md             # This file
└── 2038_game2.py      # version2
```

### Class Diagram
```
Board (Manages GUI and grid state)
├── GUI elements (window, frames, labels)
├── Grid management (4x4 matrix)
├── Tile rendering and styling
└── Game state tracking

Game (Handles game logic and user input)
├── Move processing
├── Win/lose conditions
└── Keyboard event handling
```

##  Code Explanation

### Main Components

#### 1. Board Class (`Board`)
The `Board` class handles all graphical elements and grid state management.

**Key Responsibilities:**
- Creates and manages the Tkinter GUI
- Handles tile rendering with appropriate colors and fonts
- Manages the 4x4 game grid state
- Tracks score and game statistics

**Key Methods:**
- `__init__()`: Initializes GUI and game state
- `paint_grid()`: Renders tiles with proper colors and styling
- `compress_grid()`: Moves tiles after user input
- `merge_grid()`: Handles tile merging logic
- `random_cell()`: Spawns new tiles randomly

#### 2. Game Class (`Game`)
The `Game` class contains the core game logic and handles user input.

**Key Responsibilities:**
- Processes keyboard inputs and translates to game moves
- Checks win/lose conditions
- Manages game flow and state transitions
- Coordinates with Board class for rendering

**Key Methods:**
- `__init__()`: Initializes game state
- `link_keys()`: Handles keyboard input and triggers moves
- Move processing for all four directions
- Win/lose condition checking

### Core Algorithms

#### Tile Movement Logic
```python
def compress_grid(self):
    # Moves all tiles to the left, removing empty spaces
    temp = [[0] * 4 for _ in range(4)]
    for i in range(4):
        cnt = 0
        for j in range(4):
            if self.gridCell[i][j] != 0:
                temp[i][cnt] = self.gridCell[i][j]
                cnt += 1
    self.gridCell = temp
```

#### Tile Merging Logic
```python
def merge_grid(self):
    # Combines adjacent identical tiles
    for i in range(4):
        for j in range(3):
            if self.gridCell[i][j] == self.gridCell[i][j + 1] and self.gridCell[i][j] != 0:
                self.gridCell[i][j] *= 2
                self.gridCell[i][j + 1] = 0
                self.score += self.gridCell[i][j]
```

#### Move Processing (Example: Left Move)
```python
# Left move processing
self.compress_grid()    # Shift tiles left
self.merge_grid()       # Merge identical tiles
self.compress_grid()    # Shift again after merging
```

### Color Scheme System
The game uses a carefully designed color scheme for different tile values:

```python
bg_color = {
    '2': '#eee4da',    # Light beige
    '4': '#ede0c8',    # Cream
    '8': '#f2b179',    # Orange
    '16': '#f59563',   # Dark orange
    '32': '#f67c5f',   # Red-orange
    '64': '#f65e3b',   # Bright red
    '128': '#edcf72',  # Gold
    '256': '#edcc61',  # Yellow-gold
    '512': '#edc850',  # Yellow
    '1024': '#edc53f', # Bright yellow
    '2048': '#edc22e', # Golden yellow
}
```

##  Installation and Running

### Prerequisites
- Python 3.6 or higher
- Tkinter (usually included with Python)

### Running the Game
```bash
# Clone or download the project files
# Navigate to the project directory
python 2048_game.py
```

### File Structure Explanation
- **2048_game.py**: Main executable file containing all game code
- The game is self-contained in a single file for simplicity

## 🔧 Technical Details

### Dependencies
- **tkinter**: Standard Python GUI library
- **random**: For random tile generation
- **time**: For animation timing (future enhancement)

### Game State Management
The game maintains several important states:
- `gridCell`: 4x4 matrix representing current tile positions
- `score`: Current player score
- `end`: Boolean indicating game over state
- `won`: Boolean indicating if 2048 has been reached

### Move Validation
The game checks if a move is valid by:
1. Comparing grid state before and after move processing
2. Only spawning new tiles if the board actually changed
3. Checking if any tiles were compressed or merged

##  Game Logic Deep Dive

### Win Condition
```python
# Check for 2048 tile
for i in range(4):
    for j in range(4):
        if self.gamepanel.gridCell[i][j] == 2048:
            self.won = True
```

### Game Over Condition
```python
def is_game_over(self):
    # Check for empty spaces
    for i in range(4):
        for j in range(4):
            if self.gridCell[i][j] == 0:
                return False
    # Check for possible merges
    return not self.can_merge()
```

### Tile Generation Algorithm
```python
def random_cell(self):
    cells = []
    # Find all empty cells
    for i in range(4):
        for j in range(4):
            if self.gridCell[i][j] == 0:
                cells.append((i, j))
    
    if cells:
        i, j = random.choice(cells)
        # 90% chance for 2, 10% chance for 4
        self.gridCell[i][j] = 2 if random.random() < 0.9 else 4
```

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

##  Enjoy Playing!

Start the game and challenge yourself to reach 2048! Remember the strategies:
- Keep your highest number in a corner
- Plan your moves in advance
- Try to create chain reactions
- Don't give up - practice makes perfect!

---

*Happy coding and gaming! 🚀*
