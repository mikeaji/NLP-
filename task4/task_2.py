from nltk.corpus import wordnet as wn
from itertools import product
import os.path
from nltk.tokenize import RegexpTokenizer
import nltk.data
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')

lemmatizer = WordNetLemmatizer()


print('Reading file...')
f = open('text1.txt', "r",)#encoding="utf8")#
list_data = f.read()

print('Lemmatizing words...')
list_data = list_data.lower()  # lowercase for all letters
clean_text = " ".join([lemmatizer.lemmatize(i) for i in list_data.split()])  # lemmatize the words

print('Cleaning text')
clean_text = (clean_text.split())
for i in range(0,len(clean_text)-1):
    clean_text[i] = clean_text[i].replace('--', " ")
    clean_text[i] = clean_text[i].replace('-', "")
    clean_text[i] = clean_text[i].replace('_', " ")
clean_text = ' '.join(clean_text)

print('Tokenizing words & stopwords processing...')
tokenizer = RegexpTokenizer(r'\w+')
clean_text = tokenizer.tokenize(clean_text)
clean_text = list(dict.fromkeys(clean_text))
clean_text = [word for word in clean_text if word not in stopwords.words('english')]
list_word = []
for word in clean_text:
    list_word.append(tokenizer.tokenize(word))
list_word = [item for sublist in list_word for item in sublist]

print('Calculating path similarities...')
string_to_output = "word1\tword2\tSimilarity\n"  # add the header
i = 0 # track number of treated pairs
for word1 in list_word:  # loop in loop to cross check all the senses of the word1 and word2 to get the maximum path similarity
    for word2 in list_word:
        if word1 != word2:
            synset_w1 = wn.synsets(word1)
            synset_w2 = wn.synsets(word2)
            temp = []
            for syn1 in synset_w1:
                for syn2 in synset_w2:
                    similarity = wn.path_similarity(syn1, syn2)
                    if similarity == None:
                        temp.append(0)
                    else:
                        temp.append(similarity)
            if temp != []:
                path_similarity = max(temp)
            else:
                path_similarity = 0
            string_to_add =  word1 + '\t' + word2 + '\t' +  str(path_similarity) + '\n'
            string_to_output = string_to_output + string_to_add
        i = i + 1
        print('treated pairs : ' + str(100*i/(len(list_word)*len(list_word))) + '%')
        
output_path = 'original-pairs.txt'
with open(output_path, 'w') as f2:
    f2.write(string_to_output)
    f2.close()
