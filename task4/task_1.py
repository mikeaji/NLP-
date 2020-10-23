from nltk.corpus import wordnet as wn
import re

f = open('SimLex999-100.txt','r')
data = f.readlines()
data = data[1:]

word1 = []
word2 = []
gold_similarity = []
path_similarity = []
string_to_output = 'word1\tword2\tGoldSimilarity\tWordNetSimiliarity\n'

for line in data:  # get w1, w2 in the lists along with the old similarity
    words = re.split('\s+',line)
    word1.append(words[0])
    word2.append(words[1])
    gold_similarity.append(words[2])

for i in range(0,len(data)):  # loop to check the senses of words and cross check the path similarity to get the maximum ones
    synset_w1 = wn.synsets(word1[i])
    synset_w2 = wn.synsets(word2[i])
    temp = []
    for syn1 in synset_w1:
        for syn2 in synset_w2:
            similarity = wn.path_similarity(syn1, syn2)
            if similarity == None:
                temp.append(0)
            else:
                temp.append(similarity)
    path_similarity.append(max(temp))
    string_to_output = string_to_output + word1[i] + '\t' + word2[i] + '\t' + str(gold_similarity[i]) + '\t' + str(path_similarity[i]) + '\n';

output_path = 'BioSim-100-predicted.txt'
with open(output_path, 'w') as f2:
    f2.write(string_to_output)
    f2.close()
