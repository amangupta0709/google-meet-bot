import time
from threading import Thread
import sys,subprocess
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

meetlink = sys.argv[1]
min_record_time = 200
min_members = int(input("Maximum amount of people in the meeting required to leave: "))


options = webdriver.ChromeOptions()

options.add_argument('user-data-dir=/home/aman/snap/chromium/common/chromium')

browser = webdriver.Chrome('/snap/bin/chromium.chromedriver',options=options)

browser.get(meetlink)
time.sleep(6)

def meet_join():

	meetpage = browser.find_element_by_tag_name('body')
	meetpage.send_keys(Keys.CONTROL + 'e')
	meetpage.send_keys(Keys.CONTROL + 'd')
	time.sleep(3)

	browser.execute_script('document.getElementsByClassName("snByac")[1].click()')
	time.sleep(5)


def meeting():
	tic = time.perf_counter()
	while True:
		meetingleft = ''
		for classname in ['j7nIZb','nS35F']:
			try:
				meetingleft = browser.find_element_by_xpath(f'//*[contains(concat( " ", @class, " " ), concat( " ", "{classname}", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "snByac", " " ))]').text.strip()
				if meetingleft == 'Return to home screen':
					browser.execute_script('location.reload();')
					meet_join()
					break
			except:
				pass

		try:
			joinpage = browser.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "Jyj1Td", " " ))]').text.strip()
		except:
			joinpage = ''

		toc = time.perf_counter()
		if joinpage != 'Ready to join' and meetingleft != 'Return to home screen' and (toc-tic > min_record_time):
			try:
				members = int(browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[4]/div[3]/div[6]/div[3]/div/div[2]/div[1]/span/span/div/div/span[2]').text.strip())
				print('\n\n'+str(members)+'\n\n')
				if members < min_members:
					#pyautogui.hotkey('ctrl','w')
					browser.close()
					recorder.p.terminate()
					break
			except:
				pass


		time.sleep(6)

def recorder():
	timestr = time.strftime("%Y%m%d-%H%M%S")
	command = f'ffmpeg -f pulse -ac 2 -i alsa_output.pci-0000_00_1f.3.analog-stereo.monitor -f x11grab -r 25 -s 1920x1024 -i :0.0 -vcodec libx264 -pix_fmt yuv420p -preset ultrafast -crf 0 -threads 0 -acodec pcm_s16le -y /home/aman/Documents/output-{timestr}.mkv'.split()

	recorder.p = subprocess.Popen(command, stdout=subprocess.PIPE)


meet_join()
p1 = Thread(target=meeting)
p2 = Thread(target=recorder)

p2.start()
p1.start()



# https://meet.google.com/pem-mbca-nok
# 1790,112
# 1617,551
# 1645,567
# to stop
# 1678,243

#//*[contains(concat( " ", @class, " " ), concat( " ", "j7nIZb", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "snByac", " " ))]

#//*[contains(concat( " ", @class, " " ), concat( " ", "nS35F", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "snByac", " " ))]

#//*[contains(concat( " ", @class, " " ), concat( " ", "snByac", " " ))]
