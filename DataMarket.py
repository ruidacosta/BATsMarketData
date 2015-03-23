import requests

class DataMarket():
	def __init__(self):
		self.us_url = 'http://www.batstrading.com/json/bzx/book/'
		self.eur_url = 'http://www.batstrading.co.uk/json/cxe/book/'
		# r = requests.get('http://www.batstrading.com')
		# self.us_url_cookies = r.cookies
		# r = requests.get('http://www.batstrading.co.uk')
		# self.eur_url_cookies = r.cookies


	def getUSData(self,stock):
		r = requests.get(self.us_url + stock)#,cookies=self.us_url_cookies)
		if r.status_code == 200:
			return r.json()
		else: 
			return None

	def getEurData(self,stock):
		r = requests.get(self.eur_url + stock)#,cookies=self.eur_url_cookies)
		if r.status_code == 200:
			return r.json()
		else:
			return None
