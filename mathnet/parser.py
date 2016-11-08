import time
import preprocessing as pp
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import action_chains as AC


PATH = '/home/rastice/chromedriver/chromedriver'
URL = 'http://www.mathnet.ru/php/person.phtml?option_lang=rus'


#пока что только каркас
class Authors:
	def __init__(sefl, name, position, e_mail, sci_degree, keywords, resources):
		self.name = name
		self.position = position
		self.e_mail = e_mail
		self.sci_degree = sci_degree
		self.keywords = keywords
		self.resources = resources


def get_links(driver, name):
	try:
		elements = WebDriverWait(driver, 10).until(
			EC.presence_of_all_elements_located((By.CLASS_NAME, name))
		)
	except:
		return None

	return elements

def get_all_td(driver):
	try:
		elements = WebDriverWait(driver, 10).until(
			EC.presence_of_all_elements_located((By.TAG_NAME, 'td'))
		)
	except:
		return None

	return elements


def get_list_of_authors(letter, driver):
	action = AC.ActionChains(driver)
	action.move_to_element(letter).click(letter).perform()
	list_of_authors = get_links(driver, 'SLink')

	return list_of_authors



def get_author_info(driver, autor):
	action = AC.ActionChains(driver)
	action.move_to_element(autor).click(autor).perform()
	name = driver.find_element(By.TAG_NAME, 'font').text

	# императивщик тут плачет..
	e_mails = [x for x in 
		list(map(lambda x: pp.verify_emails(x.text), get_links(driver, 'SLink')))
			if x is not None]
	resources = [x for x in
		list(map(lambda x: pp.verify_resources(x.get_attribute('href')), get_links(driver, 'SLink')))
			if x is not None]
	page_text =list(map(lambda x: x.text, get_all_td(driver)))[1:]
	position = pp.verify_position(page_text)
	sci_degree = pp.verify_sci_degree(page_text)
	keywords = pp.verify_keywords(page_text)



if __name__ == '__main__':
	driver = webdriver.Chrome(PATH)
	driver.get(URL)
	alphabet = get_links(driver, 'SLink')
	autors = get_list_of_authors(alphabet[12],driver)
	get_author_info(driver, autors[252])

	driver.quit()