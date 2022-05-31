import os
from loglevel import LogLevel
from time import strftime, gmtime, localtime
from inspect import getframeinfo, stack

TIME_FMT = "%y-%m-%d %H:%M:%S"
DAY_FMT = "%y-%m-%d"

class LoggerExt:

	def __init__(self, ownerComp):
		self.ownerComp = ownerComp
		# clear existing errors
		self.error_dat = op( 'error1' ).par.clear.pulse()
		# configure settings 
		self.Log_to_file_bool = bool(parent().par.Logtofile)
		self.Log_to_textport_bool = bool(parent().par.Logtotextport)
		self.UTC = str(parent().par.Timeformat) == "utc"
		self.Folder = parent().par.Logfolder.eval()
		self.Rotate_file = str(parent().par.Rotatefile)
		self.Logname = str(parent().par.Logname)
		# set the log level
		self.SetLevel(str(parent().par.Logginglevel))
		self.Debug("Initialized Logger")

	def SetLevel(self, level):
		if level not in LogLevel.levels:
			self.Warning(f"Cannot set log level to \"{level}\"")
			return
		self.level = LogLevel(level)
		self.Debug("set log level to " + level)

	def Verbose(self, msg):
		if self.level > LogLevel.VERBOSE():
			return
		self.log(msg, "verbose")

	def Debug(self, msg):
		if self.level > LogLevel.DEBUG():
			return
		self.log(msg, "debug")

	def Info(self, msg):
		if self.level > LogLevel.INFO():
			return
		self.log(msg, "info")

	def Warning(self, msg):
		if self.level > LogLevel.WARNING():
			return
		self.log(msg, "warning")

	def Error(self, msg):
		if self.level > LogLevel.ERROR():
			return
		self.log(msg, "error")

	def Fatal(self, msg):
		self.log(msg, "fatal")

	def ComposeLog(self, msg, severity):
		if severity == "info":
			self.Info(msg)
		elif severity == "warning":
			self.Warning(msg)
		elif severity == "error":
			self.Error(msg)
		elif severity == "fatal":
			self.Fatal(msg)
		else:
			self.Debug(msg)

	def log(self, msg, level):
		msg = self.formatMsg(msg, level)
		self.log_to_textport(msg)
		self.log_to_file(msg)


	def log_to_file(self, msg):
		if self.Log_to_file_bool:
			if self.Rotate_file:

				if self.UTC:
					day = gmtime()
				else:
					day = localtime()
				root = os.path.join(self.Folder, strftime("%m", day))
				try:
					with open(os.path.join(root, strftime(DAY_FMT, day) + ".log"), 'a+', encoding='utf-8') as outfile:
						outfile.write(msg + "\n")
				except FileNotFoundError:
					os.makedirs(root)
					return self.log_to_file(msg)

			else:
				with open(os.path.join(self.Folder, self.Logname + ".log"), 'a+', encoding='utf-8') as outfile:
					outfile.write(msg + "\n")


	def log_to_textport(self, msg):
		if self.Log_to_textport_bool:
			print(msg)

	def timestamp(self):
		if self.UTC:
			return strftime( TIME_FMT, gmtime() )
		return strftime( TIME_FMT, localtime() )

	def formatMsg(self, msg, level):
		# get the original function caller
		caller = getframeinfo(stack()[3][0])
		return f"|{level.ljust(LogLevel.padding)}| {self.timestamp()} | {caller.filename}[{caller.lineno}] | {msg}"