import curses


class TextInput:
	def __init__(self, stdscr: curses.window, pos_x, pos_y, length):
		self.text = ""
		self.cursor_pos = 0
		self.view = 0
		self.stdscr = stdscr
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.length = length

	def update(self, key_input):
		if key_input == "KEY_BACKSPACE" and len(self.text) != 0:
			self.text = self.text[:self.cursor_pos - 1] + self.text[self.cursor_pos:]
			self.cursor_pos -= 1
		elif key_input == "KEY_LEFT" and self.cursor_pos > 0:
			self.cursor_pos -= 1
		elif key_input == "KEY_RIGHT" and self.cursor_pos < len(self.text):
			self.cursor_pos += 1
		elif key_input.isprintable() and len(key_input) == 1:
			self.text = self.text[:self.cursor_pos] + key_input + self.text[self.cursor_pos:]
			self.cursor_pos += 1

		self.stdscr.addstr(6, 0, f"Char Input view:{self.view} length: {self.length} cursor_pos:{self.cursor_pos}: {self.text} {' ' * 20}")
		self.stdscr.addstr(8, 0, f"{self.pos_y} {self.pos_x + self.cursor_pos - self.view}")
		if self.cursor_pos < self.view:
			self.view = self.cursor_pos

		if self.cursor_pos > self.view + self.length:
			self.view = self.cursor_pos - self.length

		self.refresh()

	def refresh(self):
		text_rendered = self.text[self.view: self.view + self.length]
		self.stdscr.addstr(self.pos_x, self.pos_y, text_rendered + (" " * (self.length - len(text_rendered))))
		#self.stdscr.addstr(20, 0, f"{self.pos_y} {self.pos_x + self.cursor_pos - self.view}")
		#self.stdscr.move(self.pos_y, self.pos_x + self.cursor_pos - self.view)



