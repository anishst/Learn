import random

WORDS = ("python", "jumble", "easy", "difficult", "answer",  "xylophone")

sentence_length = 1000
sentence = ""

while len(sentence) < sentence_length:
	sentence += random.choice(WORDS) + " "


print(sentence)

