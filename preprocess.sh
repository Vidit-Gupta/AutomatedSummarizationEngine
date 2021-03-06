cd dataset;
mkdir train;
mkdir test;
cd ..;
mkdir temp;
echo "Created test, train and temp folders";
python parse_crisis.py;
echo "Executed parsing file";
python make_vocabulary.py;
echo "Created Vocabulary";
python idf.py;
echo "Created idf";
python test_gensim.py;
echo "Trained word2vec model";
