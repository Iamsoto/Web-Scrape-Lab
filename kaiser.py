import requests

def get_kaiser():

	r = requests.get("https://healthy.kaiserpermanente.org/")
	r.raise_for_status()

	return r.text
print(str(get_kaiser()))
