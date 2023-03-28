from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


def fetch_api(url):
	req = Request(url)
	res = {}

	try:
		response = urlopen(req)
	except HTTPError as e:
		res["error"] = "The server couldn't fulfill the request.\rError code: {0}".format(e.code)
	except URLError as e:
		res["error"] = "We failed to reach a server.\rReason: {0}".format(e.reason)
	else:
		res["status_code"] = response.code
		res["data"] = response.read()

	return res


def save_file(bird_name, html):
	file_name = bird_name.lower().replace(" ", "_")
	f = open("{0}.html".format(file_name), "w")
	f.write(html)
	f.close()
