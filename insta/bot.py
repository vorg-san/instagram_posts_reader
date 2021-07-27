import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from reader.models import Account, Posts

class FirstPage:
	def __init__(self, browser):
		self.browser = browser
		self.browser.get('https://www.instagram.com/')
	
	def login(self):
		username_input = self.browser.find_element_by_css_selector("input[name='username']")
		password_input = self.browser.find_element_by_css_selector("input[name='password']")
		username_input.send_keys(os.environ['insta_bot_username'])
		password_input.send_keys(os.environ['insta_bot_pass'])
		login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
		login_button.click()
		sleep(3)

		# not_save_login_button = self.browser.find_elements_by_css_selector(".sqdOP.yWX7d.y3zKF")
		# if len(not_save_login_button):
		# 	not_save_login_button[0].click()
		# 	sleep(2)

		# not_notification_button = self.browser.find_elements_by_css_selector(".aOOlW.HoLwm ")
		# if len(not_notification_button):
		# 	not_notification_button[0].click()
		# 	sleep(1)

		return HomePage(self.browser)

class HomePage:
	def __init__(self, browser):
		self.browser = browser

	def user_page(self, handle):
		self.browser.get(f'https://www.instagram.com/{handle}')
		sleep(1.4)

		self.seguir()

		div_links = self.browser.find_elements_by_css_selector(".v1Nh3.kIKUG._bz0w")
		post_links = [d.find_element(By.TAG_NAME, "a") for d in div_links]
		return post_links

	def get_post(self, post_link):
		fechar = self.browser.find_elements_by_css_selector('.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG')
		if len(fechar):
			fechar[0].find_element_by_xpath(".//button").click()
			sleep(1)

		post_link.find_element_by_xpath('..').click()
		sleep(2.1)

		post = self.browser.find_element_by_css_selector(".C4VMK").find_elements(By.TAG_NAME, "span")[-1]
		return post.text
		
	def seguir(self):
		follow_button = self.browser.find_elements_by_css_selector("._5f5mN.jIbKX._6VtSN.yZn4P")

		if len(follow_button):
			follow_button[0].click()
			sleep(1.7)

def run(accounts):	 
	browser = webdriver.Firefox()
	browser.implicitly_wait(5)
	first = FirstPage(browser)
	home = first.login()

	for acc in accounts:
		print(acc.handle)
		posts_db = acc.posts_set.all()
		post_links = home.user_page(acc.handle)

		for post in post_links[:5]:
			print(post)
			print(post.get_attribute('href'))
			link = post.get_attribute('href')
			if link in [p.link for p in posts_db]:
				break
			
			post_text = home.get_post(post)

			if post_text:
				p = Posts(account=acc, link=link, text=post_text)
				p.save()

	# browser.close()