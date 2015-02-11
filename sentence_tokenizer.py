from nltk import data, pos_tag, word_tokenize

tokenizer = data.load('tokenizers/punkt/english.pickle')
fp = open('dataset/interm_dataset.txt')
data = fp.read().replace('\n', '')
sentences = tokenizer.tokenize(data)

final = open('dataset/dataset.txt', 'w')
for sentence in sentences:
	final.write(sentence.replace('.', '')+'\n')
	#words = word_tokenize(sentence)
	#print pos_tag(words)
