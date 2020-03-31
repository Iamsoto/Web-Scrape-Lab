
import requests
from bs4 import BeautifulSoup
from ProPublicaRequests import houseMembers

""" 
A file deticated to fetching Public information on all Congreemen/women
"""
"""
Temporary class for testing purposes 
"""
class Scrapper_Politic_Person():
	def __init__(self, *args, **kwargs ):
		self.first_name = kwargs.get('first_name', None)
		self.last_name = kwargs.get('last_name', None)
		self.party = kwargs.get('party', None)

def get_facebook_profile_pic(Facebook_id):
	url = "https://www.facebook.com/{}".format(str(Facebook_id))
	r1 = request.get(url)
	page = r1.content 
	soup1 = BeautifulSoup(page, "html.parser")

	div_contents = soup1.find('a', aria-label = )


# Let's get our political people
def get_political_people():
	house_members_list = houseMembers()
	# Every item should be house_member_id : fb_profile url 
	house member_ids = {}

	for member_item in house_members_list:
		if member_item['id'] not in house_member_ids:
			profile_pic = get_facebook_profile_pic(member_item['facebook_account'])
			house_member_ids['id'] = profile_pic