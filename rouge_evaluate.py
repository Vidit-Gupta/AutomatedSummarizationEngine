from subprocess import call

def rouge_evaluate(resultFilePath):
	PATH = resultFilePath # output file path
	call(["java", "-jar", "-Drouge.prop="+PATH+"rouge.properties",PATH + "rouge2.0.jar"])
	output_file = open(PATH+"results.csv",'r').readlines()
	line1 = output_file[0].split(",")
	index = 0
	for i in range(len(line1)):
		if(line1[i] == "Avg_F-Score"):
			index = i
			break
	F_SCORE = float(output_file[1].split(",")[index])
	return F_SCORE
	
