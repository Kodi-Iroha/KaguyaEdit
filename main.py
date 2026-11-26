
import sys
import curses 
from pathlib import Path

# Settings 
stdscr = curses.initscr()
curses.curs_set(1)
curses.start_color()
curses.use_default_colors()
curses.init_pair(1, curses.COLOR_CYAN, -1)    # 行號顏色
curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)  # 底部狀態列

# Init 
stdscr.keypad(True)
scrool_top = 0

file = Path(sys.argv[1])
content = file.read_text(encoding="utf-8", errors="replace")
lines = content.splitlines()

# Core 
commands = ""

while commands != "exit": 
    stdscr.erase()
    heigh, width = stdscr.getmaxyx()
    body_heigh = max(1, heigh - 1)  

    for row in range(len(lines)):
        line = lines[row]
        remain = len(lines) - row
        stdscr.addstr(row, 0, line, remain)
    
    if (len(lines) + scrool_top) < heigh:
       stdscr.addstr(row, 0, "~", 1)

    status = f" {file.name} | Lines: {len(lines)} | [Up/Down] Scroll  [q] Quit "        
    stdscr.refresh()    
    key = stdscr.getch()
    if key in (ord("q"), ord("Q")):
          commands = "exit"
    elif key == curses.KEY_DOWN:
        if scrool_top + body_height < len(lines):
            scrool_top += 1
    elif key == curses.KEY_UP:
        if scrool_top > 0:
            scrool_top -= 1
 
