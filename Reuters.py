
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


Test2: Given a Url, return true if article contains a given string
"""

def article_contains_string(url= 'https://www.reuters.com/article/us-health-coronavirus-usa-congress/u-s-senate-moves-toward-uncertain-vote-on-massive-coronavirus-relief-package-idUSKBN21A1O0' , 
	words = ['Mitch McConnell', 'John Thune']):
	matching = []
	r1 = requests.get(url)
	page = r1.content
	soup1 = BeautifulSoup(page, "html.parser")

	div_content = soup1.find('div', class_ = "StandardArticleBody_body")
	#print(str(div_content))

	paragraphs = div_content.find_all("p")
	for paragraph in paragraphs:
		# List comprehension, does the paragraph contain any of these words? 
		for word in words:
			#print("Word: {}\nParagraph: {}\n\n".format(word, paragraph.text))
			if word in paragraph.text:
				matching.append(word)
				print("Found it!")

		if len(matching):
			print("Truth!\n" + paragraph.text)
			return True

	print("Falseness..." + str(matching))
	return False
	

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


def testing3():
	article_contains_string()
def testing2():
	print(str(len(get_article_links())))

testing3()
#testing2()
#testing()

#print(get_article_links().prettify())