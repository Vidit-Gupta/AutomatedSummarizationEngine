import logging, os, gensim
from collections import defaultdict
import re

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
directory = './dataset/train'
class MySentences(object):
	def __iter__(self):
		for filename in os.listdir(directory):
			data = open(directory+'/'+filename)
			for line in data:
				yield line.split()

sentences = MySentences()
model = gensim.models.Word2Vec(sentences)
model.save('./wordSimilarityModel')
#model = gensim.models.Word2Vec.load('./wordSimilarityModel')
#print model
#while 1:
#	print """
#	1. for word similarity
#	2. for relationships
#	3. exit
#	"""
#	n = raw_input()
#	n = n.strip()
#	if n == '3':
#		break
#	s = raw_input()
#	s = s.strip()
#	s = s.split(' ')
#	if n == '1':
#		print model.similarity(s[0], s[1])
#	if n == '2':
#		print model.most_similar(positive=[s[2], s[1]], negative=[s[0]])

