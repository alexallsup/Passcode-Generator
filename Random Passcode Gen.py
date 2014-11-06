import string
from random import choice

easier_to_type = True
clump_length   = 3
# easy typing mode breaks the passcode into clumps where letters are all the same case
# and are located on either the left or right hand

code_length = input("How many characters would you like your code to be?")
def gen_code(code_length, upper=True, lower=True, numer=True, punct=True, easier_to_type=True, clump_length=3, avoid_left_upper=False):

	characters = ""
	if upper: characters += string.uppercase
	if lower: characters += string.lowercase
	if numer: characters += string.digits
	if punct: characters += "!@#$%^&*()-=+?~><;:"
	
	right_upper = "YUIOPHJKLBNM"
	right_lower = "yuiophjklbnm"
	left_lower = "asdfqwertgzxcv"
	left_upper = "ASDFQWERTGZXCV"

	code = ""
	if not easier_to_type:
		for i in xrange(code_length):
			code += choice(characters)
	if easier_to_type:
		sets = []
		if lower:
			sets.append(left_lower)
			sets.append(right_lower)
		if upper:
			if not avoid_left_upper:
				sets.append(left_lower)
			sets.append(right_upper)
		if numer:
			sets.append(string.digits)
		if punct:
			sets.append("!@#$%^&*()-=+?~><;:")
		for i in xrange(code_length / clump_length):
			char_set = choice(sets)
			for i in xrange(clump_length):
				code += choice(char_set)
		char_set = choice(sets)
		for i in xrange(code_length % clump_length):
			code += choice(char_set)
	return code

print gen_code(code_length, punct=False, avoid_left_upper=True)
inp = raw_input("Press 1 + ENTER for another, ENTER to quit.")
while inp == "1":
	print gen_code(code_length, punct=False, avoid_left_upper=True)
	inp = raw_input("Press 1 + ENTER for another, ENTER to quit.")