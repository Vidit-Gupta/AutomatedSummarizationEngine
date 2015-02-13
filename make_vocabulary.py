from collections import defaultdict
from readUtility import readData

sentences = readData('./dataset/train')
d = defaultdict(int)
for sentence in sentences:
	for word in sentence:
		d[word] += 1
vocab = open('vocab.txt','w')
ct = 0
words = []
for word in d:
	if(d[word] >= 5):
		words.append(word)
words.sort()
for word in words:
	vocab.write(word+'\n')
vocab.close()
