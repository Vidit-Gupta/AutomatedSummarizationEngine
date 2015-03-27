import sys, math, operator, pickle, os
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
			minDissimilarityScore = 1.0 
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

for alpha in range(0,11):
	alpha /= 10.0
	for articleNumber in range(1, 60):
	# Getting data
		article = open('./temp/combinedProcessed'+str(articleNumber)+'.txt', 'r')

		sentences = []
		for sentence in article:
			sentences.append(sentence)
		sentences = map(lambda x: x.strip(), sentences)

		totalSentences = len(sentences)
		"""
		scoresAndDissimilarity = text_rank(sentences, 0.1, 0.85)
		scores 				= scoresAndDissimilarity[0]
		dissimilarity 		    = scoresAndDissimilarity[1]
		pickle_file = open('./textRankResults/score'+str(articleNumber)+'.p', 'wb')
		pickle.dump(scores, pickle_file)
		pickle_file.close()
		pickle_file = open('./textRankResults/dissimilarity'+str(articleNumber)+'.p', 'wb')
		pickle.dump(dissimilarity, pickle_file)
		pickle_file.close()
		"""
		scores = pickle.load(open('./textRankResults/score' + str(articleNumber)+'.p'))
		dissimilarity = pickle.load(open('./textRankResults/dissimilarity' + str(articleNumber)+'.p'))

		# Taking 1/4th senteces for summarization
		sentencesToSelect = int(math.ceil(0.25*totalSentences))
		sentencesToSelect = 10
		mxF1 			  = -1.0
		optimal = []
		gamma = 0.2; beta = 1.5

		indicesSelected = summarize(alpha, beta, gamma, False)
		createSummaryFile(indicesSelected, './temp/combinedRaw'+str(articleNumber)+'.txt', articleNumber)
		#evaluationResults  = rouge_evaluate('./rouge2.0-distribution/')
		#evaluationResults = evaluate(indicesSelected, './temp/actualSummary.txt', './temp/combinedRaw.txt')
		#print evaluationResults[0],evaluationResults[1],evaluationResults[2]
		#if(evaluationResults >= mxF1):
		#	if(evaluationResults > mxF1):
		#		optimal = []
		#	optimal.append([alpha, beta, gamma])
		#	mxF1 	  = evaluationResults
		#	alphaStar = alpha
		#	betaStar  = beta
		#	gammaStar = gamma
		
		#indicesSelected = summarize(alphaStar, betaStar, gammaStar, True)
		#createSummaryFile(indicesSelected, './temp/combinedRaw.txt')
		#print alphaStar, betaStar, gammaStar
	evaluationResults  = rouge_evaluate('./rouge2.0-distribution/')
	print '------------------------'
	print 'alpha: ' + str(alpha)
	print evaluationResults
	print '------------------------' + '\n'

# The notifier function
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

# Calling the function
notify(title    = 'AutomatedSummarization notification',
       subtitle = 'with python',
       message  = 'Summarization task has completed')