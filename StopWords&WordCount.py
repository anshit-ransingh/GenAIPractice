# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 10:01:05 2023

@author: ANSHIT
"""

import nltk

def RemoveStopWords(FilePath):
    FileData = open(FilePath)
    AllWords = []
    EnglishStopWords = nltk.corpus.stopwords.words('english')
    for Data in FileData:   
        for Word in Data.split():
            if Word.lower() not in EnglishStopWords:
                AllWords.append(Word)      
    return AllWords


def WordCount(AllWords):
    AllWordCount = {}
    for Word in AllWords:
        if Word in AllWordCount:
            AllWordCount[Word] += 1
        else:
            AllWordCount[Word] = 1
    # print(AllWordCount)
    return AllWordCount


FilePath = 'C:/Users/ANSHIT/Desktop/space.txt'

AllWords = RemoveStopWords(FilePath)
AllWordCount = WordCount(AllWords)
print(AllWordCount)