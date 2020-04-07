import requests
from bs4 import BeautifulSoup
from ProPublicaRequests import houseMembers
from Reuters import ReutersScrapper

# Let's get our political people
def fetch_Congress_News_Test():
	house_members_list = houseMembers()
	# Every item should be house_member_id : fb_profile url 
	my_house_members = {}

	reutersScraper = ReutersScrapper()
	for member_item in house_members_list:
		if member_item['id'] not in my_house_members:
			names_to_search = []
			matched_articles = []		
			articles_list = []
			my_house_members[member_item['id']] = {}

			rep_name = "{} {}".format(member_item['first_name'],member_item['last_name'])
			my_house_members[member_item['id']]['Name'] = rep_name

			names_to_search.append(rep_name)
			articles_list = reutersScraper.get_articles()
			for article in articles_list:
				#print("Looking at article: {}".format(str(article)))
				if reutersScraper.article_contains_names(article, names_to_search):
					matched_articles.append(article)
					print(" Article Contains Name !!!!!!")
				else:
					pass
					#print("-")
			my_house_members[member_item['id']]['matched_articles']=matched_articles

	with open("Fetch_Results.txt", "w+") as f:
		for member in my_house_members:
			f.write(str(member))


		#profile_pic = get_facebook_profile_pic(member_item['facebook_account'])
		#house_member_ids['id'] = profile_pic
fetch_Congress_News_Test()