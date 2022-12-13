"""
Loglevel is used to define what severity a printout is
"""

class LogLevel:

	levels = {'verbose' : 0, 'debug' : 1, 'info' : 2, 'warning' : 3, 'error' : 4, 'fatal' : 5}
	padding = max([len(key) for key in levels.keys()])

	def __init__(self, level):
		self.level = level

	@staticmethod
	def VERBOSE():
		return LogLevel("verbose")

	@staticmethod
	def DEBUG():
		return LogLevel("debug")

	@staticmethod
	def INFO():
		return LogLevel("info")

	@staticmethod
	def WARNING():
		return LogLevel("warning")

	@staticmethod
	def ERROR():
		return LogLevel("error")

	@staticmethod
	def FATAL():
		return LogLevel("fatal")

	def stringToInt(self, level):
		return self.levels.get(level)

	def __lt__(self, other):
		return self.stringToInt(self.level) < self.stringToInt(other.level)

	def __le__(self, other):
		return self.stringToInt(self.level) <= self.stringToInt(other.level)

	def __gt__(self, other):
		return self.stringToInt(self.level) > self.stringToInt(other.level)

	def __ge__(self, other):
		return self.stringToInt(self.level) >= self.stringToInt(other.level)

	def __eq__(self, other):
		return self.level == other.level

	def __ne__(self, other):
		return self.level != other.level

	def __str__(self):
		return f"Log level is {self.level}"