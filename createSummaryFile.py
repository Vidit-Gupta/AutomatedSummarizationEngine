#!/usr/bin/python

def createSummaryFile(indices, filePath):
	indices.sort()
	combinedFile = open(filePath, 'r').readlines()
	systemSummary = open('./SummarizationRouge/system/news1_system1.txt', 'w')
	for index in indices:
		systemSummary.write(combinedFile[index])
	systemSummary.close()
