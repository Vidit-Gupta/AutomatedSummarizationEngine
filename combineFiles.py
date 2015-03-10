import os, sys, re
from bs4 import BeautifulSoup

raw = open('./temp/combinedRaw.txt', 'w')
processed = open('./temp/combinedProcessed.txt', 'w')
for filename in os.listdir(sys.argv[1]):
	data = open(sys.argv[1]+'/'+filename, 'r').read()
	soup = BeautifulSoup(data)
	for node in soup.findAll('text'):
		for text in node.findAll('s'):
			raw.write(text.text+'\n')
			text = text.text.encode('ascii', 'ignore')
			text = text.decode('utf-8')
			text = text.replace('\n', '')
			text = text.replace('.', '')
			text = re.sub("[^\w\s]|_","", text)
			text = re.sub(' +',' ',text)
			text = text.lower()
			processed.write(text+'\n')
			
raw.close()
processed.close()
