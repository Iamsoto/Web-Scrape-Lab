import requests
from bs4 import BeautifulSoup
from News import NewsScrapper


def ReutersScrapper(NewsScrapper):
	self.articles_url = "https://www.reuters.com/politics"
	
	"""
	Return True if given name in Reuters Article
	False otherwise
	"""
	def article_contains_name(self, url, name)
		matching = []
		r1 = requests.get(url)
		page = r1.content
		soup1 = BeautifulSoup(page, "html.parser")

		paragraphs = div_content.find_all("p")
		for paragraph in paragraphs:
			if name in paragraph.text:
				return True

		return False
	
	"""
		format: 
			<h2>
				<a> </a> 
			</h2>
	"""
	def get_articles(self):
		r1 = requests.get(self.articles_url)
		coverpage = r1.content	
		soup1 = BeautifulSoup(coverpage, "html.parser")

		# Grab all header tags
		headline_tags = soup1.find_all('h2', class_ = 'FeedItemHeadline_headline')
		article_urls = []

		# Grab the hyper link
		for headline_tag in headline_tags:
			try:
				article_urls.append(headline_tag.a['href'])
			except Exception as e:
				print(e)

		return article_urls


#testing2()
#testing()

#print(get_article_links().prettify())