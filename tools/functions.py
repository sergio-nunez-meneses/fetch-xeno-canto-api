def fetch_api(url):
	from urllib.request import Request, urlopen
	from urllib.error import URLError, HTTPError

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


def save_html_file(bird_name, html):
	file_name = bird_name.lower().replace(" ", "_")
	f = open("{0}.html".format(file_name), "w")
	f.write(html)
	f.close()


def create_html_file(recordings):
	html = """
	<style>
		body {
			background: #202124;
			color: #fff;
		}
		.hidden {
			display:none;
		}
		.main-container {
			display: flex;
			flex-wrap: wrap;
			justify-content: space-between;
		}
		.bird-container{
			display: flex;
			flex-direction: column;
			box-shadow: 0 2.8px 2.2px rgba(0, 0, 0, 0.34), 0 6.7px 5.3px rgba(0, 0, 0, 0.48), 0 12.5px 10px rgba(0, 0, 0, 0.6), 0 22.3px 17.9px rgba(0, 0, 0, 0.72), 0 41.8px 33.4px rgba(0, 0, 0, 0.86), 0 100px 80px rgba(0, 0, 0, 0.12);
			border-radius: 5px;
			padding-top: 0.5rem;
			background: rgba(51, 51, 51, 0.8);
			/*transition: transform .2s ease-in-out;*/
		}
		/*.bird-container:hover {
			transform: scale(1.05);
		}*/
		.bird-info > img {
			width: 300px;
		}
		.bird-info {
			display: flex;
			flex-direction: column;
			justify-content: center;
			align-content: center;
			align-items: center;
		}
		.bird-recordings {
			display: flex;
			flex-wrap: wrap;
		}
		.recording {
			display: flex;
			flex-direction: column;
		}
		.bird-recordings, .recording {
			padding:0.5rem;
		}
		.download-link {
			color: #fff;
		}
	</style>
	"""

	html += """
	<div class="main-container">
		<div class="bird-container">
			<div class="bird-info">
				<span class="bird-name">{0}</span>
			</div>
			<div class="bird-recordings">
		""".format(recordings["bird_gen_name"])

	file_url = recordings["recordings"]["file_url"]
	download_url = recordings["recordings"]["download_url"]
	for i in range(len(file_url)):
		html += """
				<span class="recording">
					<audio src="{0}" controls=""></audio>
					<a href="{1}" class="hidden download-link" download>Download file</a>
				</span>
			""".format(file_url[i], download_url[i])

	html += """
			</div> <!-- .bird-recordings -->
		</div> <!-- .bird-container -->
	</div> <!-- .main-container -->
	"""

	html += """
	<script type="text/javascript">
		function showHide(e) {
			const link = e.target.nextElementSibling;

			if (e.type === "ended") {
				link.classList.add("hidden");
			}
			else {
				if (link.classList.contains("hidden")) {
					link.classList.remove("hidden");
				}
				else {
					link.classList.add("hidden");
				}
			}
		}

		document.querySelectorAll("audio").forEach(recording => {
			recording.addEventListener("play", showHide);
			recording.addEventListener("pause", showHide);
			recording.addEventListener("ended", showHide);
		})
	</script>
	"""

	return html
