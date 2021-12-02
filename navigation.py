import curses
import curses.textpad
import key_value
from text_input import TextInput


class Menu:
	window: curses.window = None

	def __init__(self, window: curses.window):
		self.window = window
		self.window.clear()
		self.resize_window()
		self.height = 0
		self.width = 0

	def resize_window(self):
		self.height, self.width = self.window.getmaxyx()
		return

	def update(self, key):
		return


class Calculator(Menu):
	raw_formula = ""
	text_input = None

	def __init__(self, window: curses.window):
		super().__init__(window)

	def resize_window(self):
		super().resize_window()
		curses.textpad.rectangle(self.window, 0, 0, 2, self.width - 1)
		self.text_input = TextInput(self.window, 1, 1, self.width - 2)

	def update(self, key):
		super().update(key)
		self.text_input.update(key)





