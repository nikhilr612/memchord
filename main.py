import os
import json
import playback
from ui import show_ui, default_settings

global_settings = {};

if __name__ == "__main__":

	# Create necessary directories.
	if not os.path.exists("./data/"):
		os.makedirs("./data");
	if not os.path.exists("./decks/"):
		os.makedirs("./decks/");

	# Load settings if they exist
	if os.path.exists("./config.json"):
		with open("./config.json") as f:
			global_settings = json.load(f);
	else:
		global_settings = default_settings.copy();

	pt = playback.PlaybackThread(global_settings);
	pt.start();
	show_ui(pt, global_settings);
