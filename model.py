#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import csv
import nltk
import re
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.data import load
from string import punctuation

#stopword list to use
spanish_stopwords = stopwords.words('spanish')

#punctuation to remove
non_words = list(punctuation)
#we add spanish punctuation
non_words.extend(['¿', '¡'])
non_words.extend(map(str,range(10)))


def tokenize(text):
	# remove links from tweets
	text = re.sub(r"http\S+", "https", text)
	# remove punctuation
	text = ''.join([c for c in text if c not in non_words])
	# remove repeated characters
	text = re.sub(r'(.)\1+', r'\1\1', text)
	# tokenize
	tokens =  word_tokenize(text)
	final_words = []
	for word in tokens:
		if not word in spanish_stopwords:
			final_words.append(word)
	return final_words                                    

negative_words = []
negative_words_value = []
with open('dataset_bulling_demo.xlsx - palabras.csv', 'r') as csvFile:
	reader = csv.reader(csvFile)
	for row in reader:
		negative_words.append(row[0])
		negative_words_value.append(row[1])
csvFile.close()

#print(negative_words)
#print(negative_words_value)

#print("#####################################")

with open('dataset_bulling_demo.xlsx - dataset.csv', 'r') as csvFile:
	    reader = csv.reader(csvFile)
	    for row in reader:
	        phrase=row[4]
		tokenized_phrase = tokenize(phrase)
		phrase_score = 0.0;
		index = 0;
		for word in tokenized_phrase:
			if word in negative_words:
				phrase_score = phrase_score + 1; #float(negative_words_value[index]);
			index += 1
		message = "Frase \"" + phrase +  "\" es " + str(100*phrase_score/len(tokenized_phrase)) + "% negativa"
		print(message)

csvFile.close()

