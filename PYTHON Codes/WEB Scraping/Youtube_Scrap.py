from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.youtube.com/'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("li", {"class": "yt-shelf-grid-item yt-uix-shelfslider-item"})

#print(page_soup.prettify())

for container in containers:
	title_container = container.findAll("a")
	video_title = title_container[1].text
	print("Video Title: "+video_title.strip())
	
	video_times = container.findAll("span", {"class": "video-time"})
	try:
	  if(len(video_times[0].text.strip()) != 0):
	    print("Video Duration: "+video_times[0].text.strip())
	  else:
	    print("No duration found!")
	except:
	  print("")
	
	print("Video Link: "+str(my_url[:-1]+title_container[2]['href']))
	
	print()
