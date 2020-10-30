import os
path = os.getcwd()
DRIVERS_PATH = path[0: path.find("python", 0)] + 'python/drivers/'

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class WebDrivers:
	def __init__ (self):
		self.value1 = 1

	def get_firefox(self, headless=True, options = None):
		if options is None:
			options = Options()
			options.headless=headless

		path = DRIVERS_PATH + "geckodriver"
		driver = webdriver.Firefox(options=options, executable_path=path)
		return driver