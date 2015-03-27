import os, sys, re
from bs4 import BeautifulSoup

for articleNumber in range(1,60):
	filename = './temp/summary'+str(articleNumber)+'XML'
	filenumber = 1
	print filename+str(filenumber)+'.txt'
	while os.path.exists(filename+str(filenumber)+'.txt'):
		completeFile = open(filename+str(filenumber)+'.txt', 'r').read()
		summaryFile = open('./SummarizationRouge/reference/news'+str(articleNumber)+'_reference'+str(filenumber)+'.txt', 'w')
		soup = BeautifulSoup(completeFile)
		for node in soup.findAll('s'):
			text = node.text.replace('\n','')
			text = text.strip()
			summaryFile.write(text+'\n')
		summaryFile.close()
		filenumber += 1

articleNumber = 1
all_folders = [f for f in os.listdir(sys.argv[1]) if re.match(r'd[0-9]+.*', f)]
for folder in all_folders:
	raw = open('./temp/combinedRaw'+str(articleNumber) + '.txt', 'w')
	processed = open('./temp/combinedProcessed' + str(articleNumber) + '.txt', 'w')
	for filename in os.listdir(sys.argv[1]+'/'+folder):
		data = open(sys.argv[1]+'/'+folder+'/'+filename, 'r').read()
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
	articleNumber += 1
