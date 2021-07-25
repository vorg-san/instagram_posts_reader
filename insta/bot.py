import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class FirstPage:
	def __init__(self, browser):
		self.browser = browser
		self.browser.get('https://www.instagram.com/')
	
	def login(self):
		username_input = browser.find_element_by_css_selector("input[name='username']")
		password_input = browser.find_element_by_css_selector("input[name='password']")
		username_input.send_keys(os.environ['insta_bot_username'])
		password_input.send_keys(os.environ['insta_bot_pass'])
		login_button = browser.find_element_by_xpath("//button[@type='submit']")
		login_button.click()
		sleep(3)

		not_save_login_button = browser.find_elements_by_css_selector(".sqdOP.yWX7d.y3zKF")
		
		if len(not_save_login_button):
			not_save_login_button[0].click()
			sleep(2)

		not_notification_button = browser.find_elements_by_css_selector(".aOOlW.HoLwm ")
		
		if len(not_notification_button):
			not_notification_button[0].click()
			sleep(1)

		return HomePage(self.browser)

class HomePage:
	def __init__(self, browser):
		self.browser = browser

	def user_page(self, page):
		self.browser.get(f'https://www.instagram.com/{page}')
		sleep(1.4)

		self.seguir()

		post_link = self.browser.find_elements_by_css_selector(".v1Nh3.kIKUG._bz0w")

		if len(post_link):
			post_link[0].click()
			sleep(2.3)

			post = self.browser.find_element_by_css_selector(".C4VMK").find_elements(By.TAG_NAME, "span")[1]
			print(post.text)


	def seguir(self):
		follow_button = self.browser.find_elements_by_css_selector("._5f5mN.jIbKX._6VtSN.yZn4P")

		if len(follow_button):
			follow_button[0].click()
			sleep(1.7)


browser = webdriver.Firefox()
browser.implicitly_wait(5)

first = FirstPage(browser)
home = first.login()

pages = ['rcnaomono', 'pefabiodemelo', 'genipapos', 'omarcusboaventura', 'masculinidade.saudavel']

for page in pages[0:1]:
	home.user_page(page)

sleep(5)

# browser.close()