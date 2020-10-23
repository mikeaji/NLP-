import os.path
import random
import re
import operator

f = open('original-pairs.txt','r')
data = f.readlines()
data = data[1:]
data = random.sample(data, len(data))

word1 = []
word2 = []
path_similarity = []

for line in data:  # get w1, w2 in the lists along with the old similarity
    words = re.split('\s+',line)
    word1.append(words[0])
    word2.append(words[1])
    path_similarity.append(words[2])
top = sorted(range(len(path_similarity)), key=lambda i: path_similarity[i], reverse=True)[:10]

string_to_output = "word1\tword2\tSimilarity\n"
for i in range(0,9):
    string_to_output = string_to_output + word1[top[i]] + "\t" + word2[top[i]] + "\t" + path_similarity[top[i]] + "\n"

output_path = 'top.txt'
with open(output_path, 'w') as f2:
    f2.write(string_to_output)
    f2.close()
