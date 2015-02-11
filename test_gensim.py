import logging, os, gensim
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class MySentences(object):
	def __init__(self,dirname):
		self.dirname = dirname
	def __iter__(self):
		for line in open(self.dirname+'/dataset.txt'):
			# assume there's one document per line, tokens separated by whitespace
			yield line.lower().split()

#sentences = MySentences('./dataset/')
#model = gensim.models.Word2Vec(sentences)
#model.save('./mymodel')
model = gensim.models.Word2Vec.load('./mymodel')

while 1:
	print """
	1. for word similarity
	2. for relationships
	3. exit
	"""
	n = raw_input()
	n = n.strip()
	if n == '3':
		break
	s = raw_input()
	s = s.strip()
	s = s.split(' ')
	if n == '1':
		print model.similarity(s[0], s[1])
	if n == '2':
		print model.most_similar(positive=[s[2], s[1]], negative=[s[0]])
		

