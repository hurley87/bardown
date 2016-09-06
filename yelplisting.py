from bs4 import BeautifulSoup
import requests

url = 'https://www.yelp.ca/search?find_desc=Bars&find_loc=100+Front+St+E,+Toronto,+Ontario,+Canada'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

links = soup.find_all('a', 'biz-name')
bars = soup.find_all('div', 'biz-listing-large')


for bar in bars:
	print(bar.find('a','biz-name').getText())
	print(bar.find('span', 'biz-phone').getText())
	print(bar.find('address').getText())