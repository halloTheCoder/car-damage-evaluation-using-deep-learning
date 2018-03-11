from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import os
import json
import webbrowser
import sys
import time

def main():
	search_text = sys.argv[1]
	num_requested = int(sys.argv[2])
	num_of_scrolls = int(num_requested/400)+1
	# number_of_scrolls * 400 images will be opened in the browser

	search_text = search_text.replace(' ','+')

	counter = 0
	succounter = 0

	url = "https://www.google.co.in/search?q="+search_text+"&source=lnms&tbm=isch"

	webbrowser.open_new_tab(url)

	browser = webdriver.Chrome(executable_path='/home/akash/drivers/chromedriver')
	browser.get(url)

	images = browser.find_elements_by_xpath("//div[contains(@class,'rg_meta')]")

	if not os.path.exists(search_text):
	    os.mkdir(search_text)

	for _ in range(num_of_scrolls):
	    for __ in range(10):
	    	# multiple scrolls needed to show all 400 images
	    	browser.execute_script("window.scrollBy(0,10000)")
	    	time.sleep(0.2)
	    # to load next 400 images
	    time.sleep(0.5)
	    try:
	    	elem = browser.find_element_by_xpath("//input[contains(@value,'Show more results')]")
	    	elem.send_keys(Keys.RETURN)
	    except Exception as e:
	    	print("Less images found:", str(e))
	    	break

	dest_filename = os.path.join(search_text)

	for x in browser.find_elements_by_xpath("//div[contains(@class,'rg_meta')]"):
	    counter = counter + 1
	    print("Total Count:", counter)
	    print("Succsessful Count:", succounter)
	    print("URL:",json.loads(x.get_attribute('innerHTML'))["ou"])

	    img = json.loads(x.get_attribute('innerHTML'))["ou"]
	    imgtype = json.loads(x.get_attribute('innerHTML'))["ity"]
	    print(img,imgtype)
	    src = img.split('/')[-1]
	    print(src)
	    try:
	    	dst = os.path.join(dest_filename,src)
	    	if(os.path.exists(dst)):
	    		print('%s already present'%src)
	    	else:
	    		urllib.request.urlretrieve(img,filename = dst)
	    	succounter += 1
	    except Exception as e:
	    	print("can't get img ",img)
	    	print(str(e))

	    if(counter >= num_requested):
	    	break

	print("Total downloaded: ", succounter, "/", counter)
	browser.quit()

if __name__ == "__main__":
	main()
