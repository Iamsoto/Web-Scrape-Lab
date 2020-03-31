def Debugging():
	return True

def ProPublicaFileLocation():
	return 'ProPublica.txt'

def ProPublicaBaseURL():
	return 'https://api.propublica.org/congress/v1/'

# TODO: Update every election
def houseMembersURL(congress = '116'):
	return "https://api.propublica.org/congress/v1/{}/house/members.json".format(str(congress))

def senateMembersURL(congress = '116'):
	return "https://api.propublica.org/congress/v1/{}/senate/members.json".format(str(congress))