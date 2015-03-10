from bs4 import BeautifulSoup
def evaluate(indicesCreated, actualSummaryPath, completeFilePath):
	truePositive = 0
	trueNegative = 0
	falsePositive = 0
	falseNegative = 0
	print indicesCreated
	actualSummary = open(actualSummaryPath, 'r').read()
	soup = BeautifulSoup(actualSummary)

	completeFile = open(completeFilePath, 'r').readlines()
	completeFile = map(lambda x: x.strip(), completeFile)
	indicesInActual = []
	for node in soup.findAll('s'):
		text = node.text.replace('\n','')
		text = text.strip()
		indicesInActual.append(completeFile.index(text))
	#indicesInCreated = set(IndicesInCreated)
	print indicesInActual
	totalSentencesInComplete = len(completeFile)
	for i in range(totalSentencesInComplete):
		if i in indicesCreated:
			if i in indicesInActual:
				truePositive += 1
			else:
				falsePositive += 1
		else:
			if i in indicesInActual:
				falseNegative += 1
			else:
				trueNegative += 1

	precision = 1.0*truePositive/(truePositive+falsePositive)
	recall = 1.0*truePositive/(truePositive+falseNegative)
	f1 = 2*precision*recall/(precision+recall)
	return [precision, recall, f1]
