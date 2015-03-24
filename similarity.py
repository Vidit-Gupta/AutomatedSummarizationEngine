import gensim

class Similarity:

	def __init__(self):
		self.model = gensim.models.Word2Vec.load('./wordSimilarityModel')
		self.idf_vals = open('idf.txt','r').read().split(' ')
		self.idf_vals = map(lambda x: float(x), self.idf_vals)
		self.words_vals = open('vocab.txt','r').readlines()
		self.words_vals = map(lambda x: x.strip(), self.words_vals)
		self.idf = dict(zip(self.words_vals, self.idf_vals))

	def get_word_simlarity(self,word1,word2): #should return word2vec similarity of two words
		#print self.model.similarity(word1, word2), word1, word2
		return self.model.similarity(word1, word2)

	def get_sentence_similarity(self,sentence1,sentence2): #sentences as list of words
		sim_1 = 0
		sentence1 = sentence1.split(' ')
		sentence2 = sentence2.split(' ')
		idfSum = 0.0
		for i in range(len(sentence1)):
			if(sentence1[i] not in self.idf):
				continue
			idfSum += self.idf[sentence1[i]]
			#print sentence1[i]
			max_sim = -10000000
			for j in range(len(sentence2)):
				if(sentence2[j] not in self.idf):
					continue
				#print sentence2[j]
				val = self.get_word_simlarity(sentence1[i],sentence2[j])
				if(val > max_sim):
					max_sim = val
			sim_1+= self.idf[sentence1[i]]*max_sim
			#print '\n'
		if idfSum == 0:
			sim_1 = 0
		else:
			sim_1 = sim_1*1.0/idfSum
		
		sim_2 = 0
		idfSum = 0.0
		for i in range(len(sentence2)):
			
			if(sentence2[i] not in self.idf):
				continue
			idfSum += self.idf[sentence2[i]]
			max_sim = -10000000
			for j in range(len(sentence1)):
				if(sentence1[j] not in self.idf):
					continue
				val = self.get_word_simlarity(sentence1[j],sentence2[i])
				if(val > max_sim):
					max_sim = val
			sim_2+= self.idf[sentence2[i]] * max_sim
		if idfSum == 0:
			sim_2 = 0
		else:
			sim_2 = sim_2*1.0/idfSum
		return ((sim_1 + sim_2))/2.0
