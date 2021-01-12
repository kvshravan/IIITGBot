from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from creds import email,passwd,NotHSCourse
import time
import datetime
driver = None
def start_browser():
	global driver
	PATH='C:\chromedriver.exe'
	driver = webdriver.Chrome(PATH)
	driver.get("https://iiitg.codetantra.com/login.jsp")
	time.sleep(4)
	if 'login.jsp' in driver.current_url:
		login()
	if 'home.jsp' in driver.current_url:
		print("Login Successful")
		openClasses()
	else:
		print("Something wrong with the credentials")
		driver.quit()
		exit()
	while True:
		if 'm.jsp' in driver.current_url:
			try:
				openCurrentOngoingClass()
			except Exception as e:
				raise
		if 'mi.jsp' in driver.current_url:
			try:
				joinClass()
			except Exception as e:
				raise
		else:
			print("No ongoing classes currently or already in a classs....")
		if 'jnr.jsp' in driver.current_url:
			print("Joined Successfully")
			now = datetime.datetime.now()
			timediff = 60-(now.minute)
			print("Checking for next class in ",timediff," minutes")
			time.sleep(timediff*60)
			print("Cheking for next class, Press ctrl+c to exit")
def login():
	emailId = driver.find_element_by_id("loginId")
	password = driver.find_element_by_id("password")
	submitBtn = driver.find_element_by_id("loginBtn")
	CREDS = {'email' : email,'passwd':passwd}
	emailId.click()
	emailId.send_keys(CREDS['email'])
	password.click()
	password.send_keys(CREDS['passwd'])
	submitBtn.click()
	time.sleep(5)
def openClasses():
	classBtn=driver.find_element_by_xpath("//a[@title='Click here to view Meetings']")
	classBtn.click()
	time.sleep(3)
def openCurrentOngoingClass():
	classElements=driver.find_elements_by_xpath("//a[contains(@class, 'fc-time-grid-event')]")
	for eachClass in classElements:
		if ('rgb(55, 136, 216)' in eachClass.get_attribute('style') or 'green' in eachClass.get_attribute('style')) and NotHSCourse not in eachClass.get_attribute('title'):
			eachClass.click()
			break
	time.sleep(3)
def joinClass():
	try:
		WebDriverWait(driver, 3600).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href,'jnr.jsp')]")))
		joinBtn = driver.find_element_by_xpath("//a[contains(@href,'jnr.jsp')]")
		joinBtn.click()
	except Exception as e:
		raise
if __name__ == '__main__':
	start_browser()
