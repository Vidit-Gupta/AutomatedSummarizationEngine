#!/usr/bin/python

def createSummaryFile(indices, filePath, articleNumber):
	indices.sort()
	combinedFile = open(filePath, 'r').readlines()
	systemSummary = open('./SummarizationRouge/system/news'+str(articleNumber)+'_system1.txt', 'w')
	for index in indices:
		systemSummary.write(combinedFile[index])
	systemSummary.close()
