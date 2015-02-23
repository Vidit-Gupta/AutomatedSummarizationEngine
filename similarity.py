idf = {} #should map string of word to its idf

def get_word_simlarity(word1,word2): #should return word2vec similarity of two words
	return 1

def get_sentence_similarity(sentence1,sentence2): #sentences as list of words
	
	sim_1 = 0
	for i in range(len(sentence1)):
		max_sim = -10000000
		for j in range(len(sentence2)):
			val = get_word_simlarity(sentence1[i],sentence2[j])
			if(val > max_sim):
				max_sim = val
		sim_1+= idf[sentence1[i]]*max_sim
	sim_1 = sim_1*1.0/len(sentence1)	
	
	sim_2 = 0
	for i in range(len(sentence2)):
		max_sim = -10000000
		for j in range(len(sentence1)):
			val = get_word_simlarity(sentence1[j],sentence2[i])
			if(val > max_sim):
				max_sim = val
		sim_2+= idf[sentence2[i]] * max_sim
	sim_2 = sim_2*1.0/len(sentence2)

	return ((sim_1 + sim_2)*1.0)/2






