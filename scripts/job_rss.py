import sys
import os
path = os.getcwd()
final_path = path[0: path.find("python", 0)] + 'python/'
sys.path.append(final_path)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.send_mail import send_mail
from drivers.webdrivers import WebDrivers

url = 'https://www.3pillarglobal.com/job-opportunities'

driver = WebDrivers().get_firefox()
driver.get(url)
try:
	elements = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.CLASS_NAME, "job-title"))
	)
finally:
	jobs=driver.find_elements_by_class_name('job-title')

jobs_list=["0"]
stringjob =''
for element in jobs:
	driver.execute_script("return arguments[0].scrollIntoView(true);", element)
	jobs_list.append(element.get_attribute("innerHTML"))
	stringjob = stringjob + jobs_list[-1] + ", "

driver.quit()

for job in jobs_list:
	if ('DATA' in job.upper() and 'ENGINEER' in job.upper()):
		message_text = "There is a possible job oppening at 3Pillars for Data Engineer:\n {}".format(url)
	else:
		message_text = "These are the open jobs at 3pillars:\n {}".format(stringjob)

send_mail(["marius.bistika@gmail.com"], message_text)
