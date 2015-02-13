import os, math

directory = './dataset/train'
vocab = open('vocab.txt', 'r').read().split('\n')
dictionary = {}
vocab.remove('')
i = 0
for word in vocab:
	dictionary[word] = i
	i += 1
totalWords = len(vocab)
totalFiles = 1.0*int(open('parameters.txt','r').readlines()[0].strip())
idf = [0 for x in range(totalWords)]

for filename in os.listdir(directory):
	temp = {}
	data = open(directory + '/' + filename)
	for line in data:
		lis = line.split()
		for word in lis:
			if word in dictionary:
				temp[word]=1
	for word in temp:
		idf[dictionary[word]] += 1
		i += 1
idf = map(lambda x: str(math.log(totalFiles/x)), idf)
idfFile = open('./idf.txt', 'w')
idfFile.write(' '.join(idf))
idfFile.close()
