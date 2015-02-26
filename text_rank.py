import similarity
from math import fabs

def text_rank(sentences,threshold,damping_factor):
	num_sentences = len(sentences)
	initial_score = 1
	similarity_obj = similarity.Similarity()
	scores = [initial_score for x in range(num_sentences)]
	similarity_matrix = [[0 for y in range(num_sentences)] for x in range(num_sentences)]
	dissimilarity_matrix = [[0 for y in range(num_sentences)] for x in range(num_sentences)]

	for i in range(num_sentences):
		for j in range(i,num_sentences):
			similarity_matrix[i][j] = max(0.0, similarity_obj.get_sentence_similarity(sentences[i],sentences[j]))
			similarity_matrix[j][i] = similarity_matrix[i][j]
			dissimilarity_matrix[i][j] = 1-similarity_matrix[i][j]
			dissimilarity_matrix[j][i] = 1-similarity_matrix[i][j]


	#print similarity_matrix
	#print '\n'
	#print dissimilarity_matrix

	temp_scores = [initial_score for x in range(num_sentences)] # temp scores assigned to be 0
	minimumChange = True
	while minimumChange == True:
		minimumChange = False
		for i in range(num_sentences):

			sum_val = 0.0
			for j in range(num_sentences):
				edge_sum = 0
			
				if j!=i:
					for k in range(num_sentences):
						edge_sum = edge_sum + similarity_matrix[j][k]
					sum_val = sum_val + (1.0 * scores[j] * similarity_matrix[j][i])/edge_sum
			
			temp_scores[i] = (1-damping_factor) + (damping_factor * sum_val)
		for i in range(num_sentences):
			if fabs(scores[i]-temp_scores[i]) > threshold:
				minimumChange = True
			scores[i] = temp_scores[i]    # setting the new score calculated with each iteration

	# print scores
	return [scores] + [dissimilarity_matrix] # return a list containing scores and dissimilarity matrix
