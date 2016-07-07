#!python3

import os
import requests
import bs4
import shutil
import pytesseract

output_path="hark_comics/"
if not os.path.isdir(output_path):
	os.mkdir(output_path)

repeat=0
site_url="http://www.harkavagrant.com/"

while (True):
	res = requests.get(site_url)
	if (res.status_code == requests.codes.ok):
		soup=bs4.BeautifulSoup(res.text, "html.parser")
				
		#find the right span and get first child
		comic = soup.find('span', {'class' : 'rss-content'}).findChildren()[0]
		comic_src = comic['src']
		local_name = comic['src'].split('/')[-1]
		print(local_name)
		comic_img = requests.get(comic_src,stream=True)
		
		if not (comic_img.status_code == requests.codes.ok):
			repeat+=1
			continue	
		
		with open(output_path + local_name, 'wb') as out_file:
   			shutil.copyfileobj(comic_img.raw, out_file)
		del comic_img

		#get the toolbar div
		prevbutton = soup.find('img', {"src" : "buttonprevious.png"})
		prevlink = prevbutton.parent
		site_url = prevlink['href']
		repeat=0
	else:
		if repeat>2:
			break

		repeat+=1
		
	


