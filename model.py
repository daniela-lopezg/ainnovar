#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import csv
import nltk
import re
import sys
from Child_data import *
from Province import *
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

# score that a phrase has to have to be negative
threshold = float(sys.argv[1])

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

def get_children(child_list, userid):
	index = 0
	for child in child_list:
		child_userid = child.getUserid()
		if(userid == child_userid):
			return index
		index = index + 1
	return -1

def increase_interactions(child_list, userid):
	index = get_children(child_list, userid)
	child_list[int(userid)].increase_interactions_total()
	print(child_list[int(userid)].getInteractions_total())	

def increase_bully_score(child_list,userid):
	index = get_children(child_list, userid)
	child_list[int(userid)].increase_interactions_bully()
	message = str(child_list[int(userid)].getFullname()) + " hace bullying"
	print(message)

def increase_bullied_score(child_list, userid):
	index = get_children(child_list, userid)
	child_list[int(userid)].increase_interactions_bullied()
	message = str(child_list[int(userid)].getFullname()) + " recibe bullying"
	print(message)

def increase_province_interactions(province_list, child_list, userid):
	index = int(get_children(child_list, userid))
	province_name = child_list[index].getProvince()
	for province in province_list:
		if(province.getName() == province_name):
			province.increaseInteractions()

negative_words = []
negative_words_value = []
with open('dataset_bulling_demo.xlsx - palabras.csv', 'r') as csvFile:
	reader = csv.reader(csvFile)
	for row in reader:
		negative_words.append(row[0])
		negative_words_value.append(row[1])
csvFile.close()

children_list = []
province_names = []

with open('dataset_bulling_demo.xlsx - personajes.csv', 'r') as csvFile:
	reader = csv.reader(csvFile)
	index = 0
	for row in reader:
		child = Child_data(row[0], row[1], row[2], row[3], row[4])
		children_list.append(child)
		province = child.getProvince()
		if(index == 0):
			index = -1
			continue
		if(province not in province_names):
			province_names.append(province)
csvFile.close()

province_list = []
for name in province_names:
	province = Province(name)
	province_list.append(province)

with open('dataset_bulling_demo.xlsx - dataset.csv', 'r') as csvFile:
	    reader = csv.reader(csvFile)
	    count = 0
	    for row in reader:
		if(count == 0):
			count = -1
			continue
		negative_phrase = False
	        phrase=row[4]
		emisor = int(row[5])
		tokenized_phrase = tokenize(phrase)
		phrase_score = 0.0;
		index = 0;
		for word in tokenized_phrase:
			if(index == 0):
				index +=1
				continue
			if word in negative_words:
				phrase_score = phrase_score + float(negative_words_value[index]);
			index += 1
		message = "En la frase \"" + phrase + "\""		
		print(message)
		increase_interactions(children_list, row[0])
		increase_province_interactions(province_list, children_list, row[0])
		if(phrase_score >= threshold):
			negative_phrase = True
		if(negative_phrase and emisor == 1):
			increase_bully_score(children_list, row[0])
		elif(negative_phrase and emisor == 0):
			increase_bullied_score(children_list, row[0])
		else:
			print("Nadie recibió bullying")
		message = "Frase \"" + phrase +  "\" es " + str(100*phrase_score/len(tokenized_phrase)) + "% negativa"
		print(message)
		print("#############################################################################")

csvFile.close()

for child in children_list:
	child.set_bully_score()
	child.set_bullied_score()
	child_bullied_score = child.getBullied_Score()
	child_bully_score = child.getBully_Score()
	if(child_bullied_score != 0.0):
		message = child.getFullname() + " recibe bullying con un puntaje de " + str(child_bullied_score*100) + "%"
		print(message)
	else:
		message = child.getFullname() + " no recibe bullying"
		print(message)
	if(child_bully_score != 0.0):
		message = child.getFullname() + " es un bully con un puntaje de " + str(child_bully_score*100) + "%"
		print(message)
	else:
		message = child.getFullname() + " no es un bully"
		print(message)

for province in province_list:
	message = "Total de interacciones en la comuna de: " + province.getName() + ": " + str(province.getInteractions())
	print(message)
