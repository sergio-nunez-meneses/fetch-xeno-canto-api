from tools.functions import get_bird_recordings, save_html_file, create_html_file

bird_recordings = get_bird_recordings(input("Enter bird generic name (e.g., Dendrocopos Major): "))

if bird_recordings:
	save_html_file(bird_recordings["bird_gen_name"], create_html_file(bird_recordings))
else:
	print(bird_recordings)
