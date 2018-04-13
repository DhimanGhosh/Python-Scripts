from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.flipkart.com/search?q=graphics%20card&sid=6bo/g0i/6sn&as=on&as-show=on&otracker=start&as-pos=1_1_ic_grap'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
#print(page_soup.body.img)
containers = page_soup.findAll("div", {"class": "_3yI_5w"})
#print(page_soup.prettify)
#print(len(containers))
#print(containers[0].findAll("a", {"class":"_2cLu-l"})[0].text)

file_name = "Products.csv"
f = open(file_name, 'w')

headers = "Brand, Product Description, Price, EMI/Month\n"

f.write(headers)

for container in containers:
	title_container = container.findAll("a", {"class": "_2cLu-l"})
	product_desc = title_container[0].text
	brand = product_desc.split()[0]

	price_container = container.findAll("div", {"class", "_1vC4OE"})
	price = price_container[0].text

	emi_container = container.findAll("div", {"class": "_29N3iy"})
	emi = emi_container[0].span.text.split('/')[0]

	print("Brand: " + brand)
	print("Product Description: " + product_desc)
	print("Price: " + price)
	print("EMI/month: " + emi + "\n\n")

	f.write(brand + "," + product_desc + "," + price + "," + emi + "\n")
f.close()
