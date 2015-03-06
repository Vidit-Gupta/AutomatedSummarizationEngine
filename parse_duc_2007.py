#!/usr/bin/python

import os, re, random
from bs4 import BeautifulSoup
totalFiles = int(open('parameters.txt', 'r').readlines()[0].strip())
testCount = min(5, totalFiles*1/100)
test = set(random.sample(list(xrange(totalFiles)), testCount))
filenumber = 0

for root, dirs, files in os.walk("./dataset/duc_2007"):
	for filename in files:
		match = re.search(".S", filename)
		if match:
			filenumber += 1
			filePath = root + "/" + filename
			datafile = open(filePath, 'r').read()
			soup = BeautifulSoup(datafile)
			if filenumber in test:
				textdata = open('dataset/test/'+str(filenumber)+'.txt', 'w')
			else:
				textdata = open('dataset/train/'+str(filenumber)+'.txt', 'w')
			for node in soup.findAll('text'):
				for sentence in node.findAll('s'):
					text = sentence.text.encode('ascii', 'ignore')
					text = text.decode('utf-8')
					text = text.replace('\n', '')
					text = text.replace('.', '')
					text = re.sub("[^\w\s]|_","", text)
					text = re.sub(' _',' ',text)
					text = text.lower()
					textdata.write(text+'\n')
			textdata.close()
