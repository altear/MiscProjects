#!python3

import os
import requests
import bs4
import shutil

xkcd_path="/home/pi/xkcd_imgs/"
if not os.path.isdir(xkcd_path):
	os.mkdir(xkcd_path)

repeat=0
xkcd_url="http://xkcd.com"
page="/1/"
while (True):
	res = requests.get(xkcd_url+page)
	if (res.status_code == requests.codes.ok):
		soup=bs4.BeautifulSoup(res.text, "html5lib")
		comic_elem = soup.select('#comic img')
		comic_link = 'http:' + comic_elem[0].get('src')
		comic_name = comic_link.split('/')[-1]
		print(comic_name)				
		comic = requests.get(comic_link,stream=True)
		
		if not (comic.status_code == requests.codes.ok):
			repeat+=1
			continue	
		
		with open(xkcd_path + comic_name, 'wb') as out_file:
    			shutil.copyfileobj(comic.raw, out_file)
		del comic

		repeat=0
		page = soup.select('a[rel="next"]')[0].get('href')
		print(page)		
	else:
		if repeat>2:
			break
		repeat+=1
		
	


