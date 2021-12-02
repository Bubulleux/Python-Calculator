import serialaze
import calculator
import curses
import key_value
import navigation
current_menu = None

def main(stdscr: curses.window):
	global current_menu

	stdscr.clear()
	current_menu = navigation.Calculator(stdscr)
	while True:
		key_input = str(stdscr.getkey())
		if key_input == "^C":
			exit(0)
		stdscr.addstr(5, 0, str(key_input) + " " * 30)
		current_menu.update(key_input)


curses.wrapper(main)
# curses.initscr()
# main(curses.newwin(50, 50, 0, 0))

