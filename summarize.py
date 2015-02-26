import sys, math, operator
from text_rank import text_rank

# Function to get sentece with max score that has not been selected so far
def getMaximumAvailable():
	mx = -10
	mxidx = -1
	for i in range(totalSentences):
		if selected[i] == 0:
			if currentScore[i] > mx:
				mx = currentScore[i]
				mxidx = i
	return mxidx

# Getting data
directory = "./dataset/test"
article = open(directory+'/'+sys.argv[1], 'r')
alpha = float(sys.argv[2])
beta = float(sys.argv[3])
gamma = float(sys.argv[4])

sentences=[]
for sentence in article:
	sentences.append(sentence)
sentences = map(lambda x: x.strip(), sentences)

totalSentences = len(sentences)
#print totalSentences

scoresAndDissimilarity = text_rank(sentences, 0.05, 0.85)
scores = scoresAndDissimilarity[0]
dissimilarity = scoresAndDissimilarity[1]
print scores

# Array initializations
currentScore = [0]*totalSentences
selected = [0]*totalSentences
selectedSentences = []

# Taking 1/4th senteces for summarization
sentencesToSelect = int(math.ceil(0.25*totalSentences))
chronologicalImportanceNormalization = 0.0
for i in range(totalSentences):
	chronologicalImportanceNormalization += (beta**(-i))

#Selecting the sentences
for k in range(sentencesToSelect):
	for i in range(totalSentences):
		minDissimilarityScore = -1.0 
		for sentence in selectedSentences:
			minDissimilarityScore = min(minDissimilarityScore, dissimilarity[i][sentence[1]])
		minDissimilarityScore = max(minDissimilarityScore, 0.0)
		
		chronologicalImportance = (beta**(-i))/chronologicalImportanceNormalization
		print chronologicalImportance, scores[i]
		
		currentScore[i] = gamma*scores[i] + (1-gamma)*chronologicalImportance
		
		currentScore[i] =  (alpha*currentScore[i] + (1-alpha)*minDissimilarityScore)
		
	maxIndex = getMaximumAvailable()
	selectedSentences.append([sentences[maxIndex],maxIndex])
	selected[maxIndex] = 1

selectedSentences.sort(key=operator.itemgetter(1)) #Sorting selected sentences according to order in the actual article

# Printing out the sentences
for sentence in selectedSentences:
	print sentence[0]
	print '\n'
