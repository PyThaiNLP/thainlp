# -*- coding: utf-8 -*-
import pythainlp
from pythainlp.transliterate import romanize as romanize_pythainlp
from collections import Counter
class WordList(list):
    def __init__(self, collection):
        super(WordList, self).__init__(collection)
    def __str__(self):
        return '|'.join(self)

class nlp(object):
    def __init__(self,text,dictlist=[]):
        self.text=text
        self.dictlist=dictlist
        if self.dictlist==[]:
            self.words=WordList(pythainlp.word_tokenize(self.text))
        else:
            self.dict=pythainlp.tokenize.dict_trie(self.dictlist)
            self.words=WordList(pythainlp.word_tokenize(self.text,self.dict))
        self.tags=pythainlp.pos_tag(self.words)
        self.romanize=[romanize_pythainlp(i) for i in self.words]
        self.word_counts=Counter(self.words)
    def change_word_tokenize(self,name):
        if self.dictlist==[]:
            self.words=WordList(pythainlp.word_tokenize(self.text,engine=name))
        else:
            self.words=WordList(pythainlp.word_tokenize(self.text,self.dict))
        self.tags=pythainlp.pos_tag(self.words)
    def change_pos_tag(self,name):
        self.tags=pythainlp.pos_tag(self.words,engine=name)
    def ngrams(self,n=1):
        return [tuple(self.words[i:i+n]) for i in range(len(self.words)-n+1)]
    def change_romanize(self,engine= 'royin'):
        self.romanize=[romanize_pythainlp(i,engine=engine) for i in self.words]