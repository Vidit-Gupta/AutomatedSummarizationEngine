import sys, math, operator
from text_rank import text_rank
#from evaluate import evaluate
from createSummaryFile import createSummaryFile
from rouge_evaluate import rouge_evaluate


# Function to get sentece with max score that has not been selected so far
def getMaximumAvailable(selected, currentScore):
	mx = -10
	mxidx = -1
	for i in range(totalSentences):
		if selected[i] == 0:
			if currentScore[i] > mx:
				mx = currentScore[i]
				mxidx = i
	return mxidx


def summarize(alpha, beta, gamma, showSummary):
	# Array initializations
	currentScore 	  = [0]*totalSentences
	selected 		  = [0]*totalSentences
	selectedSentences = []

	chronologicalImportanceNormalization = 0.0
	for i in range(totalSentences):
		chronologicalImportanceNormalization += (beta**(-i))

	#Selecting the sentences
	for k in range(sentencesToSelect):
		for i in range(totalSentences):
			minDissimilarityScore = -1.0 
			for sentence in selectedSentences:
				minDissimilarityScore = min(minDissimilarityScore, dissimilarity[i][sentence[1]])
			minDissimilarityScore   = max(minDissimilarityScore, 0.0)
			chronologicalImportance = (beta**(-i))/chronologicalImportanceNormalization
			#print chronologicalImportance, scores[i]
			currentScore[i] 		= gamma*scores[i] + (1-gamma)*chronologicalImportance
			currentScore[i] 		=  (alpha*currentScore[i] + (1-alpha)*minDissimilarityScore)
			
		maxIndex = getMaximumAvailable(selected, currentScore)
		selectedSentences.append([sentences[maxIndex],maxIndex])
		selected[maxIndex] = 1

	selectedSentences.sort(key=operator.itemgetter(1)) #Sorting selected sentences according to order in the actual article
	indices = []
	# Printing out the sentences
	for sentence in selectedSentences:
		indices.append(sentence[1])
		if showSummary is True:
			print sentence[0]
			print '\n'
	print indices
	return indices

#########
# Main
#########
scoresAndDissimilarityMap = {}
for gamma in range(0,11):
	gamma /= 10.0
	for articleNumber in range(1, 60):
	# Getting data
		article = open('./temp/combinedProcessed'+str(articleNumber)+'.txt', 'r')

		sentences = []
		for sentence in article:
			sentences.append(sentence)
		sentences = map(lambda x: x.strip(), sentences)

		totalSentences = len(sentences)
		if articleNumber not in scoresAndDissimilarityMap:
			scoresAndDissimilarityMap[articleNumber] = text_rank(sentences, 0.1, 0.85)
		scoresAndDissimilarity = scoresAndDissimilarityMap[articleNumber]
		scores 				   = scoresAndDissimilarity[0]
		dissimilarity 		   = scoresAndDissimilarity[1]

		# Taking 1/4th senteces for summarization
		sentencesToSelect = int(math.ceil(0.25*totalSentences))
		sentencesToSelect = 10
		mxF1 			  = -1.0
		optimal = []
		beta = 1.5; alpha = 0.7
		#for alpha in range(0,11):
		#	alpha /= 10.0
			#for beta in range(1,10):
			#	beta = 1+beta/10.0
				#for gamma in range(0,11):
					#gamma /= 10.0

		indicesSelected = summarize(alpha, beta, gamma, False)
		createSummaryFile(indicesSelected, './temp/combinedRaw'+str(articleNumber)+'.txt')
		evaluationResults  = rouge_evaluate('./rouge2.0-distribution/')
		#evaluationResults = evaluate(indicesSelected, './temp/actualSummary.txt', './temp/combinedRaw.txt')
		#print evaluationResults[0],evaluationResults[1],evaluationResults[2]
		if(evaluationResults >= mxF1):
			if(evaluationResults > mxF1):
				optimal = []
			optimal.append([alpha, beta, gamma])
			mxF1 	  = evaluationResults
			alphaStar = alpha
			betaStar  = beta
			gammaStar = gamma
		#indicesSelected = summarize(alphaStar, betaStar, gammaStar, True)
		#createSummaryFile(indicesSelected, './temp/combinedRaw.txt')
		#print alphaStar, betaStar, gammaStar
		print '------------------------'
		print 'article ', articleNumber
		print mxF1
		for lis in optimal:
			print lis
		print '------------------------'