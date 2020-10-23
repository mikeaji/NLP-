import re
from nltk.corpus import wordnet as wn
import os.path
from itertools import product

f = open('original-pairs.txt','r')
data = f.readlines()
data = data[1:]

word1 = []
word2 = []
path_similarity = []

for line in data: 
    words = re.split('\s+',line)
    word1.append(words[0])
    word2.append(words[1])
    path_similarity.append(words[2])
    
hyp1, hyp2, hyp_similarity = [], [], []


string_to_output = "word1\tword2\tSimilarity1\thyp1\thyp2\tSimilarity2\n"

for i in range(0,len(data)):
    hypernym_1 = wn.synsets(word1[i])
    hypernym_2 = wn.synsets(word2[i])
    if hypernym_1:
        hypernym_1 = hypernym_1[0].hypernyms()
        if hypernym_1:
            hypernym_1 = hypernym_1[0].lemma_names()
            hyp1.append(hypernym_1[0])
    if hypernym_2:
        hypernym_2 = hypernym_2[0].hypernyms()
        if hypernym_2:
            hypernym_2 = hypernym_2[0].lemma_names()
            hyp2.append(hypernym_2[0])
    if not hypernym_1:
        hyp1.append("None")
    if not hypernym_2:
        hyp2.append("None")
    synset_w1 = wn.synsets(hyp1[i])
    synset_w2 = wn.synsets(hyp2[i])
    temp = []
    for syn1 in synset_w1:
        for syn2 in synset_w2:
            similarity = wn.path_similarity(syn1, syn2)
            if similarity == None:
                temp.append(0)
            else:
                temp.append(similarity)
    hyp_similarity.append(max(temp))
    string_to_add =  word1[i] + '\t' + word2[i] + '\t' +  str(path_similarity[i]) + '\t' +  hyp1[i] + '\t' + hyp2[i] + '\t' +  str(hyp_similarity[i]) +  '\n'
    string_to_output = string_to_output + string_to_add
    print("Treaded pairs : " + str(100*i/len(data)) + "%" )
            
output_path = 'original-pairs-hypernyms.txt'
with open(output_path, 'w') as f2:
    f2.write(string_to_output)
    f2.close()
