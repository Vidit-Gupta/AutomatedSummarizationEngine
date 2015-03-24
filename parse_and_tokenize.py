from bs4 import BeautifulSoup
from nltk import data, word_tokenize
import random, re

tokenizer = data.load('tokenizers/punkt/english.pickle')

dataset = open('dataset/nysk.xml', 'r').read()
soup = BeautifulSoup(dataset)

totalFiles = int(open('parameters.txt','r').readlines()[0].strip())
testCount = min(100, totalFiles*1/100)
fileNumber = 0
test = set(random.sample(list(xrange(totalFiles)), testCount))

for node in soup.findAll('text'):
	fileNumber += 1
	if fileNumber in test:
		textdata = open('dataset/test/'+str(fileNumber)+'.txt', 'w')
	else:
		textdata = open('dataset/train/'+str(fileNumber)+'.txt', 'w')
	text =  node.text.encode('ascii', 'ignore')
	text = text.decode('utf-8')
	text = text.replace('\n', '')
	sentences = tokenizer.tokenize(text)
	for sentence in sentences:
		sentence = sentence.replace('.', '')
		sentence = re.sub("&apos;","'",sentence)
		sentence = re.sub("[^\w\s']|_","",sentence)
		sentence = re.sub(' +',' ',sentence)
		sentence = sentence.lower()
		textdata.write(sentence+'\n')
	textdata.close()
