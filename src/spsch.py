import json
import msgpack
import os
from collections import namedtuple
from datetime import date

def proc_string(s):
	new_s = [];
	for ch in s:
		if ch.isalpha():
			new_s.append(ch);
	return ''.join(new_s)

# Card Deck will be stored as Dict{'name':String, 'cards': List[{'name', 'pattern', 'notes'}]}
# Card Data will be stored as Dict(Id -> namedtuple(n, ef, i, last_review))

CardData = namedtuple("CardData", ['n', 'ef', 'I', 'last_review']);

class Scheduler:
	def __init__(self, deck_fpath):
		with open(deck_fpath) as f:
			self.deck = json.load(f, strict=False);
			self.savepath = "./data/" + os.path.basename(deck_fpath).replace('.json', '.dat');
			if os.path.exists(self.savepath):
				with open(self.savepath, 'rb') as f2:
					self.savedata = msgpack.load(f2, strict_map_key = False);
			else:
				self.savedata = {}
			self.scheduled_cards = [];
			self.last_card = None;
			for (key, value) in self.savedata.items():
				value = CardData(*value);
				if self.last_card is None or key > self.last_card:
					self.last_card = key
				self.savedata[key] = value;
				diff_in_days = (date.today() - date.fromisoformat(value.last_review)).days;
				if diff_in_days > value.I:
					self.scheduled_cards.append(key);
			self.iter_index = 0;

	def num_scheduled(self):
		return len(self.scheduled_cards);

	def poll_card(self):
		if self.iter_index >= len(self.scheduled_cards):
			return None;
		card_id = self.scheduled_cards[self.iter_index];
		ret = self.deck['cards'][card_id]
		self.iter_index += 1;
		return (card_id, ret);


	def record_response(self, idx, q):
		if idx in self.savedata:
			item = self.savedata[idx];
			n = item.n;
			ef = item.ef;
			I = item.I;
		else:
			n = 0;
			ef = 2.5;
			I = 0;

		if q <= 3:
			# Redo card
			self.scheduled_cards.append(idx);

		if q >= 3:
			if n == 0:
				I = 1;
			elif n == 1:
				I = 6;
			else:
				I = round(I * ef);
			n += 1;
		else:
			n = 0;
			I = 1;

		ef += (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02));
		if ef < 1.3:
			ef = 1.3;
		self.savedata[idx] = CardData(n, ef, I, date.today().isoformat());

	def schedule_new_cards(self, n):
		start = 0 if self.last_card is None else self.last_card+1;
		end = start + n;
		if end <= len(self.deck['cards']):
			self.scheduled_cards.extend(range(start, end));
			self.last_card = end -1;

	def get_study_info(self):
		return "Total cards: " + str(len(self.deck['cards'])) + ", For Review: " + str(len(self.scheduled_cards) - self.iter_index);

	def save_progress(self):
		with open(self.savepath, 'wb') as f:
			msgpack.dump(self.savedata, f);


if __name__ == "__main__":
	# Run tests.
	test_scheduler = Scheduler("./decks/basic_intervals.json");
	while (item := test_scheduler.poll_card()):
		test_scheduler.record_response(item[0], 5);
	print(test_scheduler.savedata);
	test_scheduler.save_progress();