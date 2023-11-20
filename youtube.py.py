from selenium import webdriver 
import random
from random import randrange
import time 
from bs4 import BeautifulSoup as soup
from selenium.webdriver.common.keys import Keys
from random import choice
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from datetime import date
import os
from datetime import date, datetime, timedelta
import numpy as np
import pandas as pd
from datetime import date, datetime, timedelta
from oauth2client.service_account import ServiceAccountCredentials
import gspread
from gspread_dataframe import get_as_dataframe, set_with_dataframe
from datetime import date
from googleapiclient  import discovery
from apiclient  import discovery

from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from oauth2client import file,client,tools



#random weights to search term
class WeightedRandomizer:
	def __init__ (self, weights):
		self.__max = .0
		self.__weights = []
		for value, weight in weights.items ():
			self.__max += weight
			self.__weights.append ( (self.__max, value) )
	def random (self):
		r = random.random () * self.__max
		for ceil, value in self.__weights:
			if ceil > r: return value

search_term = ['parkour','bollywood','magic','tanmay bhatt','mobile games','bassi standup','netflix','new hindi series','bluetooth speakers','samsung','trekking india','standup','hip hop']

search_term_m30 = ['meditation','bollywood','magic','buddha','midlife','one plus tv','netflix','new hindi series','travel around','mi phone','yoga','standup','buddhism']

search_term_f30 = ['meditation','bollywood','magic','best hindi serials','recipe','homemade food','netflix','new hindi series','byjus','mi phone','yoga','zumba','web series']

search_term = ['kylie jenner','recipe','bollywood','latest songs','maybelline','mobile games','make up','ukulele','new hindi series','make up tips','latest cosmetics','urooj','tiktok']

#search_term = search_term1+search_term2+search_term3+search_term4

#import sys
  
#search_term = sys.argv[0]

#eid = sys.argv[1]

if eid = 'juicewrldmx':
	search_term = search_term_m23

if eid = 'jojicradle':
	search_term = search_term_m30

if eid = 'jijocradlef':
	search_term = search_term_f30

if eid = 'f1824girl':
	search_term = search_term_f23


print(search_term)

w = {search_term[0]: 5.0, search_term[1]: 2.0, search_term[2]: 1.0,search_term[3]: 4.0,search_term[4]: 2.0,search_term[5]: 3.0,search_term[6]: 4.0,search_term[7]: 5.0,search_term[8]: 2.0,search_term[9]: 2.0,search_term[10]: 2.0,search_term[11]: 1.0,search_term[12]: 5.0}

wr = WeightedRandomizer(w)
# = ['mx player','bollywood','latest songs','voot','mobile games','one plus tv','hotstar','new hindi series','bluetooth earbud','iphone','mi phone','latest phones','standup']

#driver.find_element_by_class_name('style-scope ytd-video-renderer').click()
#search and click
def search_click(wds):
	search_t = wr.random()
	search = wds.find_element_by_css_selector('input[id=search]')
	time.sleep(random.randint(2,3))
	search.clear()
	time.sleep(random.randint(2,5))
	for character in search_t:
		search.send_keys(character)
		time.sleep(0.2)
	time.sleep(random.randint(4,6))
	wds.find_element_by_id("search-icon-legacy").click()
	time.sleep(random.randint(8,10))
	try:
		r=random.randint(0,3)
		wds.find_elements_by_class_name('style-scope ytd-video-renderer')[r].click()
	except:
		home_page_1st_reco(wds)
	

#go to home, click on recommended
def home_page_1st_reco(wds):
	wds.find_element_by_id('logo').click()
	time.sleep(random.randint(9,15))
	try:
		r=random.randint(0,3)
		wds.find_elements_by_id('dismissable')[r].click()
	except:
		search_click(wds)


#video len
def v_len(wds):
	wds.execute_script('document.getElementsByTagName("video")[0].pause()')
	time.sleep(random.randint(2,4))
	video_len = wds.find_element_by_class_name('ytp-time-duration').get_attribute("textContent")
	wds.execute_script('document.getElementsByTagName("video")[0].play()')
	return float(video_len.split(":")[0])*60+float(video_len.split(":")[1])


#play_next
def play_next(wds):
	wds.execute_script('document.getElementsByTagName("video")[0].pause()')
	wds.find_element_by_class_name('ytp-left-controls').find_element_by_class_name('ytp-next-button').click()


#click back
def click_back(wds):
	wds.back()

ads = []



def detect_ad(wds):
	page = wds.page_source
	if "ytp-ad-player-overlay" in page:
		ads.append([])
		try:
			wds.execute_script('document.getElementsByTagName("video")[0].pause()')
			time.sleep(1)
			ads[len(ads)-1].append(wds.find_element_by_class_name('ytp-title-subtext').text)
			ads[len(ads)-1].append(wds.find_element_by_class_name('ytp-title-link').text)
			ads[len(ads)-1].append(wds.find_element_by_class_name('ytp-ad-player-overlay-instream-info').find_element_by_class_name('ytp-ad-button-text').text)
			print('video ad')
		except:
			try:
				time.sleep(1)
				ads[len(ads)-1].append(wds.find_element_by_id('action-companion-click-target').find_element_by_id('header').text)
				ads[len(ads)-1].append(wds.find_element_by_id('domain').text)
				ads[len(ads)-1].append(wds.find_element_by_class_name('ytp-ad-player-overlay-instream-info').find_element_by_class_name('ytp-ad-button-text').text)
				print('video ad captured')
				time.sleep(2)
			except:
				ads[len(ads)-1].append("display ad")
				ads[len(ads)-1].append(wds.find_element_by_id('action-companion-click-target').find_element_by_id('header').text)
				ads[len(ads)-1].append(wds.find_element_by_id('domain').text)
				print("display ad captured")
	else:
		try:
			wds.find_element_by_id('domain').text
			ads.append([])
			ads[len(ads)-1].append("display ad")
			ads[len(ads)-1].append(wds.find_element_by_id('action-companion-click-target').find_element_by_id('header').text)
			ads[len(ads)-1].append(wds.find_element_by_id('domain').text)
			print("display ad captured")
		except:
			print('no ad')




#skip sec
def skip_sec(wds):
	vlen = v_len(wds)
	sec = str(random.randint(round((0.3*vlen)), round(0.8*vlen)))
	wds.execute_script('document.getElementsByTagName("video")[0].currentTime +='+sec)

#randomly assign sleep time in [a,b] range
def time_sleep(a,b):
	time.sleep(random.randint(a,b))

def skip_ad(wds):
	wds.find_element_by_class_name("ytp-ad-skip-button-container").click()


#after a video is openned what does a human do?
def human(wds):
	skip_sec(wds)
	time_sleep(3,6)



#fns1 = [skip_sec, time_sleep]
def to_do_ad(wds):
	l=len(ads)
	try:
		detect_ad(wds)
	except:
		time_sleep(3,5)
		detect_ad(wds)
	print(l)
	print(len(ads))
	if(len(ads)>l):
		print("ad detected")
		try:
			skip_ad(wds)
			print("ad skipped")
		except:
			print("skip button gone")
			pass
	else:
		print("no ad")
		human(wds)
		detect_ad(wds)
		try:
			skip_ad(wds)
			print("ad skipped!")
		except:
			print("no ad/can't skip")
		time_sleep(4,10)
	time_sleep(2,5)
	try:
		play_next(driver)
	except:
		wds.back()

#player-ads
#sign in using eid
def sign_in(wds,eid):
	time.sleep(3)
	wds.find_element_by_xpath('//div[2]/ytd-button-renderer/a').click()
	time.sleep(5)
	email = wds.find_element_by_css_selector('input[type=email]')
	time.sleep(5)
	#eid = "juicewrldmx"
	for character in eid:
		email.send_keys(character)
		time.sleep(0.2)
	time.sleep(6)
	wds.find_element_by_id("identifierNext").click()
	time.sleep(random.randint(6,8))
	password = wds.find_element_by_css_selector('input[type=password]')
	time.sleep(random.randint(5,8))
	passkey = "10p15vp0011"
	for character in passkey:
		password.send_keys(character)
		time.sleep(0.2)
	time.sleep(random.randint(6,8))
	wds.find_element_by_id("passwordNext").click()
	time.sleep(random.randint(5,8))


fns = [search_click, home_page_1st_reco]
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--window-size=1920x1080")

#eid = 'juicewrldmx'

driver = webdriver.Chrome(chrome_options=chrome_options)


driver.get('http://www.youtube.com')


time.sleep(random.randint(5,8))


n=75

while(len(ads)<n):
	try:
		driver.get('http://www.youtube.com')
		sign_in(driver,eid)
		print("you're signed in")
	except:
		pass
	#driver.get('http://www.youtube.com')
	print("outside")
	time.sleep(3)
	try:
		choice(fns)(driver)
	except:
		choice(fns)(driver)
	time_sleep(6,9)
	#home_page_1st_reco(driver)
	to_do_ad(driver)
	r = random.randint(6,12)
	for i in range(r):
		print("inside")
		to_do_ad(driver)


for i in range(5):
	for i in range(len(ads)):
		print(len(ads[i]))
		if(len(ads[i])!=3):
			del ads[i]


today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
		
dat = np.array(ads)


data = pd.DataFrame({'Date': d1,'Emailid': eid,'Platform': 'YouTube', 'Advertiser': dat[:,0],'Brand': dat[:,1],'Ad unit': dat[:,2]})

#data = pd.DataFrame(ads, columns = ['Advertiser', 'brand','Advertiser'])  


data.to_csv("check_"+str(today)+eid+".csv", encoding="utf-8", index = False) 






