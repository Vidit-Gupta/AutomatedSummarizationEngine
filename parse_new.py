from bs4 import BeautifulSoup
import re, os
path = "/Users/apple/Documents/8th sem/SMAI/dataset/nist_data/d061j/"

fileNumber = 0

cum_sentences = ""
for root, dirs, files in os.walk(path):
    for file_name in files:
    	dataset = open(path+file_name, 'r').read()
    	soup = BeautifulSoup(dataset)
    	for node in soup.findAll('s'):
			if node.parent.name=='text':
				sentence = node.text
				sentence = sentence[1:]
				sentence = sentence.replace('.', '')
				sentence = re.sub("[^\w\s']|_","",sentence)
				sentence = sentence.lower()
				sentence +="\n"
				cum_sentences += sentence
print cum_sentences