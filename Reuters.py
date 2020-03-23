
import requests
from bs4 import BeautifulSoup

"""
Useful links: 
https://morioh.com/p/abf3d53739f8

https://www.crummy.com/software/BeautifulSoup/bs4/doc/

Reuters URL
https://www.reuters.com/politics

Find specific text in a web page
https://stackoverflow.com/questions/51640636/how-to-locate-a-specific-html-row-containing-specific-text-with-python

"""

# Test 1: Give base URL, return article links
"""
	format: 
		<h2>
			<a> </a> 
		</h2>
"""
def get_article_links(url="https://www.reuters.com/politics"):
	r1 = requests.get(url)
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
	#return headline_divs[0].find('h2').find('a')['href']


def testing2():
	print(str(len(get_article_links())))

"""
def testing():
	file_name = "WashPost_Headers.txt"
	with open(file_name, "w+")as f:
		children_of_first_story_headline_div = get_article_links()
		for child in children_of_first_story_headline_div:
			f.write("{}\n".format(str(child)))

"""
testing2()
#testing()

#print(get_article_links().prettify())