#Q1: Returns a dictionary with the count of each letter in a string

def count_of_letters(string):
	letter_dictionary = {}
	for letter in string:
		#disregards any special characters
		if letter.isalpha():
			if letter.lower() not in letter_dictionary:
				letter_dictionary[letter.lower()] = 1
			else:
				letter_dictionary[letter.lower()] += 1
	return letter_dictionary

#testing on test.txt file:
with open("test.txt") as myfile:
	string = myfile.read()
	print "Letter dictionary: ", count_of_letters(string)
	print





#Q2 Counts how many times each word appears in a file

print "Select text entry method:"
print "1: From file"
print "2: Manual entry"
choice = int(raw_input())

if choice == 1: 
	filelocation = raw_input("Type in file path. eg. ""~/Desktop/text.txt \n")
	with open(filelocation) as myfile:
		paragraph = myfile.read()
elif choice == 2:
	paragraph = raw_input("Please enter text: \n")


def string_prep(paragraph):

	list_of_words = paragraph.split(" ")
	import string  #module for the string.punctuation function (list of all punctuation)
	#creates tuples of (Index, Word)
	for index, word in enumerate(list_of_words, 0):     
	 #replaces each word with a cleansed version: lower case, removing leading and trailing punctuation and invisible characters       
		list_of_words[index] = word.lower().strip(string.punctuation).strip()    
	return list_of_words

def count_of_words(list_of_words):
	word_dictionary = {}
	for item in list_of_words:
		if item.lower() not in word_dictionary:
			word_dictionary[item.lower()] = 1
		else:
			word_dictionary[item.lower()] += 1
	return word_dictionary

word_dictionary = count_of_words(string_prep(paragraph))

print word_dictionary