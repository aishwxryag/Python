import requests
from bs4 import BeautifulSoup

#web scraping: newegg.com

url = "https://www.newegg.com/global/in-en/p/23B-00G6-000D4?Description=realme%20gt%20neo%202&cm_re=realme_gt%20neo%202-_-23B-00G6-000D4-_-Product&quicklink=true"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")


model_name = soup.find_all('h1', attrs={"class":"product-title"})[0].get_text()

print("\n\n"+model_name+"\n")


price = soup.find_all('div', attrs={"class":"price-current"})[0].get_text()

print("\nPrice = "+price)


availabilty = soup.find_all('div', attrs={"class":"product-inventory"})[0].get_text()

print("\nAvailability: "+availabilty)


spec = soup.find_all('div', attrs={"class":"product-bullets"})[0].get_text()

print("\nSpecifications: "+spec)


colour = soup.find_all('strong', attrs={"class":"form-current-value"})[0].get_text()

print("\nColour of model: "+colour+"\n")

print("***END***")
