#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import csv
import nltk
import re
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.data import load
from nltk.stem import SnowballStemmer
from string import punctuation

#stopword list to use
spanish_stopwords = stopwords.words('spanish')

#spanish stemmer
stemmer = SnowballStemmer('spanish')

#punctuation to remove
non_words = list(punctuation)
#we add spanish punctuation
non_words.extend(['¿', '¡'])
non_words.extend(map(str,range(10)))


def stem_tokens(tokens, stemmer):
	stemmed = []
	for item in tokens:
		stemmed.append(stemmer.stem(item))
	return stemmed

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
	# stem
#	try:
#		stems = stem_tokens(tokens, stemmer)
#	except Exception as e:
#		print(e)
#		stems = ['']
#        return stems
	return final_words                                    

with open('dataset_bulling_demo.xlsx - dataset.csv', 'r') as csvFile:
	    reader = csv.reader(csvFile)
	    for row in reader:
	        phrase=row[4]
		print(tokenize(phrase))
csvFile.close()

