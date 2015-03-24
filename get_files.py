import os, re
FOLDER_PATH = "./summaries"
OUTPUT_PATH = "./temp"
all_folders = [f for f in os.listdir(FOLDER_PATH) if re.match(r'd[0-9]+.*', f)]
# print all_folders
d = {}
count = 0
for i in range(len(all_folders)):
	folder = all_folders[i]
	number = int(folder[1:][:-2])
	# print number
	if number in d.keys():
		d[number]+=1
	else:
		d[number]=1
		count+=1
	files = os.listdir(FOLDER_PATH + "/" +folder)
	if "200e" in files:
		inp = open(FOLDER_PATH + "/" + folder + "/200e",'r').readlines() #some dont have 200e
		inp = map(lambda x: x.strip().encode('ascii', 'ignore').rstrip(), inp)
		inp = '\n'.join(inp)
		out = open(OUTPUT_PATH+ "/summarize"+str(count)+"XML" + str(d[number]) + '.txt','w').write(inp)
	else:
		d[number]-=1
