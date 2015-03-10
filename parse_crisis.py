#!/usr/bin/python

import os
import re, random
# traverse root directory, and list directories as dirs and files as files

totalFiles = int(open('parameters.txt','r').readlines()[0].strip())
testCount = min(100, totalFiles*1/100)
fileNumber = 0
test = set(random.sample(list(xrange(totalFiles)), testCount))

for root, dirs, files in os.walk("./dataset"):
    # path = root.split('/')
    for file_name in files:
        match = re.search(".cont",file_name)
        if match:
        	filePath = root+"/"+file_name
        	fileNumber+=1
        	sentences = open(filePath,'r').readlines()
        	if fileNumber in test:
        		newFile = open('./dataset/test/'+str(fileNumber)+'.txt','w')
        	else:
        		newFile = open('./dataset/train/'+str(fileNumber)+'.txt','w')
        	for sentence in sentences:
				sentence = sentence.replace('.', '')
				sentence = re.sub("&apos;","'",sentence)
				sentence = re.sub("[^\w\s']|_","",sentence)
				sentence = sentence.lower()
				newFile.write(sentence)
