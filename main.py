import json
from urllib.parse import quote
from tools.functions import fetch_api, save_html_file, create_html_file


def get_bird_recordings(bird_name):
	api_url = "https://xeno-canto.org/api/2/recordings?query={0}+cnt:france".format(
		quote(bird_name.lower().encode("utf8")))
	api = fetch_api(api_url)
	bird = {}

	if "error" not in api:
		api_data = json.loads(api["data"].decode('utf-8'))

		if api_data["numRecordings"] > "0":
			bird["bird_gen_name"] = bird_name.title()
			bird["recordings"] = {
				"file_url":     [],
				"download_url": []
			}

			for recording in api_data["recordings"]:
				file_path = recording["sono"]["small"].split("ffts")[0]
				file_name = quote(recording["file-name"].encode("utf-8"))
				file_url = "https:{0}{1}".format(file_path, file_name)

				bird["recordings"]["file_url"].append(file_url)
				bird["recordings"]["download_url"].append(recording["file"])
	else:
		return api["error"]
	return bird


bird_recordings = get_bird_recordings(input("Enter bird generic name (e.g., Dendrocopos Major): "))

if bird_recordings:
	save_html_file(bird_recordings["bird_gen_name"], create_html_file(bird_recordings))
else:
	print(bird_recordings)
