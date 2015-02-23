num_sentences = 3
initial_score = 1
num_of_iterations = 1
damping_factor = 0.85

scores = [initial_score for x in range(num_sentences)]
similarity_matrix = [[0 for y in range(num_sentences)] for x in range(num_sentences)]

##############################
similarity_matrix[0][0] = 1
similarity_matrix[0][1] = 0.6
similarity_matrix[0][2] = 0.2
similarity_matrix[1][0] = 0.6
similarity_matrix[1][1] = 1
similarity_matrix[1][2] = 0.3
similarity_matrix[2][0] = 0.2
similarity_matrix[2][1] = 0.3
similarity_matrix[2][2] = 1



print similarity_matrix

temp_scores = [initial_score for x in range(num_sentences)] # temp scores assigned to be 0

for iter_no in range(num_of_iterations):	
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
		scores[i] = temp_scores[i]    # setting the new score calculated with each iteration
	print scores




# print scores


