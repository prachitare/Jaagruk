import requests
from bs4 import BeautifulSoup as bs 
import datetime

def get_count():
	url = 'https://www.worldometers.info/coronavirus/'
	r = requests.get(url)

	soup = bs(r.content, 'html5lib')
	soup.prettify()

	current_count = soup.find("td", text="India").find_next_sibling("td").text

	for link in soup.findAll('td', {'align': 'right'}):
	    print(link.text)

	#getting current date and time
	dt = str(datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"))

	return [current_count, dt]