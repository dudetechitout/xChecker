from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import time 

global count
global total
total = 0

def check_alert(d):
	global count 
	count += 1
	if(count >= 3):
		d.quit()
	else:
		try:
			a = d.switch_to_alert()
			print(a.text)
			return a.text
		except:
			time.sleep(5)
			print("Slept")
			check_alert(d)

def launch(c):
		try:
			global total
			d = webdriver.Firefox()
			d.set_page_load_timeout(10)
			d.get(c)
			wait = WebDriverWait(d, 10)
			wait.until(lambda d: d.current_url == "http://example.com/")
			http_split = c.split("://")
			domain_split = http_split[1].split("/")
			domains = domain_split[0].replace("www.", "")
			if(d.current_url == "http://example.com/"):
				total += 1
				print("[" + domains + "]" + " Got em' " + "[" + str(total) + "]")
				with open("log.txt", "a") as myfile:
					myfile.write(c + "\n")
			else:
				print("Not em'")
			d.quit()
		except:
			print("Not em'")
			d.quit()
			pass

with open('check.txt') as f:
	for line in f:
		global count
		count = 0
		launch(line)
