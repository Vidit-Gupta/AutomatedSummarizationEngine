from bs4 import BeautifulSoup

dataset = open('dataset/nysk.xml', 'r').read()
soup = BeautifulSoup(dataset)

textdata = open('dataset/interm_dataset.txt', 'w')
for node in soup.findAll('text'):
	text =  node.text.encode('ascii', 'ignore')
	textdata.write(text)
	#print ''.join(findAll(text=True))

