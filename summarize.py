import sys, math, operator

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
sentences=[]
for sentence in article:
	sentences.append(sentence)
sentences = map(lambda x: x.strip(), sentences)

totalSentences = len(sentences)
print totalSentences

# Array initializations
currentScore = [0]*totalSentences
selected = [0]*totalSentences
selectedSentences = []
scores = [1,1,2,1,1,1,1,1,1]

# Picking out first sentence
maxScore = max(scores)
maxIndex = scores.index(maxScore)
selectedSentences.append([sentences[maxIndex], maxIndex])
selected[maxIndex] = 1

# Taking 1/4th senteces for summarization
sentencesToSelect = int(math.ceil(0.25*totalSentences))-1 #Subtracting 1 because initial sentece selected separately
print sentencesToSelect

#Selecting the sentences
for k in range(sentencesToSelect):
	for i in range(totalSentences):
		dissimilarityScore = 0.0
		"""for sentence in selectedSentences:
			dissimilarityScore += dissimilarity[i][sentence[1]]"""
		dissimilarityScore /= len(selectedSentences)
		currentScore[i] = alpha*scores[i] + (1-alpha)*dissimilarityScore
		
		maxIndex = getMaximumAvailable()
	selectedSentences.append([sentences[maxIndex],maxIndex])
	selected[maxIndex] = 1

selectedSentences.sort(key=operator.itemgetter(1)) #Sorting selected sentences according to order in the actual article

#actualArticle = open('./')

# Printing out the sentences
for sentence in selectedSentences:
	print sentence[0] + ".",
