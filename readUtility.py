import os
def readData(directory):
	for filename in os.listdir(directory):
		data = open(directory+'/'+filename)
		for line in data:
			yield line.split()
