import requests
from bs4 import BeautifulSoup
from ProPublicaRequests import ProPublicaRequest
from Reuters import ReutersScrapper

"""
	TODO: Multithread
"""
def file_contains_name(file, names):
	content = open(file, "r").read()
	for name in names:
		if name in content:
			return True
	return False


"""
	Create a file that shows 
	1) the names each house of rep member
	2) the links whose articles have been found to contain their name

"""
def run():
	ppr = ProPublicaRequest()
	house_members_list = ppr.houseMembers()

	my_house_members = {}

	reutersScraper = ReutersScrapper()
	reutersScraper.download_articles()

	for member_item in house_members_list:
		if member_item['id'] not in my_house_members:
			my_house_members[member_item['id']] = {}
			my_house_members[member_item['id']]['name'] = "{} {} {}".format(member_item['short_title'], member_item['first_name'], member_item['last_name'])
			files_to_search = reutersScraper.get_local_files()
			
			my_house_members[member_item['id']]['links'] = []
			for file in files_to_search:
				if file_contains_name(file, my_house_members[member_item['id']]['name']):
					# url should be the first element of the file
					url = open(file, "r").read().splitlines()[0]
					my_house_members[member_item['id']]['links'].append(url)
					#print("Found a URL!! {}".format(url))
				# Todo: Multi thread this part
	reutersScraper.remove_local_files()
			
	with open("Fetch_Results.txt", "w+") as f:
		for member, value in my_house_members.items():
			f.write("==={}====:{}\n\n\n".format(value['name'], str(value['links']))) 


run()
		#profile_pic = get_facebook_profile_pic(member_item['facebook_account'])
		#house_member_ids['id'] = profile_pic
#fetch_Congress_News_Test()