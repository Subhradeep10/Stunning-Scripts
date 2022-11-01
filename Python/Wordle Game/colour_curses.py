"""
Can only be imported after the curses screen is intialised
"""

from utils import curses

curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(5, curses.COLOR_CYAN, curses.COLOR_BLACK)
curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)


W = curses.color_pair(0)
WB = curses.color_pair(0) + curses.A_BOLD
WU = curses.color_pair(0) + curses.A_UNDERLINE
WBU = WUB = curses.color_pair(0) + curses.A_BOLD + curses.A_UNDERLINE


R = curses.color_pair(1)
RB = curses.color_pair(1) + curses.A_BOLD
RU = curses.color_pair(1) + curses.A_UNDERLINE
RBU = RUB = curses.color_pair(1) + curses.A_BOLD + curses.A_UNDERLINE

G = curses.color_pair(2)
GB = curses.color_pair(2) + curses.A_BOLD
GU = curses.color_pair(2) + curses.A_UNDERLINE
GBU = GUB = curses.color_pair(2) + curses.A_BOLD + curses.A_UNDERLINE

B = curses.color_pair(3)
BB = curses.color_pair(3) + curses.A_BOLD
BU = curses.color_pair(3) + curses.A_UNDERLINE
BBU = BUB = curses.color_pair(3) + curses.A_BOLD + curses.A_UNDERLINE

Y = curses.color_pair(4)
YB = curses.color_pair(4) + curses.A_BOLD
YU = curses.color_pair(4) + curses.A_UNDERLINE
YBU = YUB = curses.color_pair(4) + curses.A_BOLD + curses.A_UNDERLINE


C = curses.color_pair(5)
CB = curses.color_pair(5) + curses.A_BOLD
CU = curses.color_pair(5) + curses.A_UNDERLINE
CBU = CUB = curses.color_pair(5) + curses.A_BOLD + curses.A_UNDERLINE

M = curses.color_pair(6)
MB = curses.color_pair(6) + curses.A_BOLD
MU = curses.color_pair(6) + curses.A_UNDERLINE
MBU = MUB = curses.color_pair(6) + curses.A_BOLD + curses.A_UNDERLINE
