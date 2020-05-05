import nltk
from nltk.corpus import stopwords
import re

def prep_text(corpus_list, remove_list):
    """This function cleans and parses a given corpus and returns
    a cleaned corpus"""
    clean_text = []
    str_list = [str(sent) for sent in corpus_list]
    stopwords_list = list(set(nltk.corpus.stopwords.words('english'))) + remove_list

    def has_at(inputstring):
        return ('@' in inputstring)

    def has_link(inputstring):
        return ('https' in inputstring)

    for sentence in str_list:
        sentence = sentence.lower() #Lowercase text
        sentence = sentence.split()
        sentence = [term for term in sentence if has_at(term) == False] #Remove @nametag
        sentence = [term for term in sentence if has_link(term) == False]
        sentence = [term for term in sentence if term not in stopwords_list] #Remove stopwords
        #sentence = [ps.stem(word) for word in sentence] #Stem words
        sentence = ' '.join(sentence)
        sentence = re.sub('[^A-Za-z0-9\#]', ' ', sentence) #Remove special characters
        sentence = re.sub(' +', ' ', sentence)
        sentence = sentence.strip()
        clean_text.append(sentence)
    clean_corpus = clean_text
    return clean_corpus
