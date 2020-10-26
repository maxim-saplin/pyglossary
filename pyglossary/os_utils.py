import os
import shutil


class indir(object):
	"""
	mkdir + chdir shortcut to use with `with` statement.

		>>> print(os.getcwd())  # -> "~/projects"
		>>> with indir('my_directory', create=True):
		>>>     print(os.getcwd())  # -> "~/projects/my_directory"
		>>>     # do some work inside new 'my_directory'...
		>>> print(os.getcwd())  # -> "~/projects"
		>>> # automatically return to previous directory.
	"""
	def __init__(self, directory: str, create: bool = False, clear: bool = False):
		self.oldpwd = None
		self.dir = directory
		self.create = create
		self.clear = clear

	def __enter__(self):
		self.oldpwd = os.getcwd()
		if os.path.exists(self.dir):
			if self.clear:
				shutil.rmtree(self.dir)
				os.makedirs(self.dir)
		elif self.create:
			os.makedirs(self.dir)
		os.chdir(self.dir)

	def __exit__(self, exc_type, exc_val, exc_tb):
		os.chdir(self.oldpwd)
		self.oldpwd = None


def runDictzip(filename: str) -> None:
	import subprocess
	dictzipCmd = "/usr/bin/dictzip"  # TODO: save in user config
	if not os.path.isfile(dictzipCmd):
		return False
	if filename[-4:] == ".ifo":
		filename = filename[:-4]
	(out, err) = subprocess.Popen(
		[dictzipCmd, filename + ".dict"],
		stdout=subprocess.PIPE
	).communicate()
#	out = p3[1].read()
#	err = p3[2].read()
#	log.debug(f"dictzip command: {dictzipCmd!r}")
#	if err:
#		log.error(f"dictzip error: {err.replace('\n', ' ')}")
#	if out:
#		log.error(f"dictzip error: {out.replace('\n', ' ')}")


def my_url_show(link: str) -> None:
	import subprocess
	for path in (
		'/usr/bin/gnome-www-browser',
		'/usr/bin/firefox',
		'/usr/bin/iceweasel',
		'/usr/bin/konqueror',
	):
		if os.path.isfile(path):
			subprocess.call([path, link])
			break


"""
try:
	from gnome import url_show
except:
	try:
		from gnomevfs import url_show
	except:
		url_show = my_url_show
"""


def click_website(widget: "Any", link: str) -> None:
	my_url_show(link)
