# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 16:04:11 2021

@author: TUBA
"""


from nltk import sent_tokenize
import nltk
nltk.download('punkt')

nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

from nltk.corpus import stopwords
  
from datasets import load_dataset

dataset = load_dataset('cnn_dailymail', '3.0.0')

#https://pypi.org/project/py-rouge/
import re 
import os.path
import time

from sentenceRanking import allCorpusSentenceRanking, textSentenceCount
from graph import createGraph,findHighestSimilarityRank
from Evaluation import rougeEvaluation

def cleanDocument(document):
    sentences = sent_tokenize(document)
    cleanedDocument=[]
    for sentence in sentences:
        # Removing Paranthesis
        sentence =re.sub("[\(\[].*?[\)\]]", "", sentence)

        #Removing \
        sentence.replace('\\','')

        #Removing -- and before
        if "--" in sentence: 
            splitting=sentence.split("--")
            sentence =splitting[1]

        cleanedDocument.append(sentence)
    newCorpus = ' '.join(cleanedDocument)
    return newCorpus

def saveFile(directory,filename,document):
    #directory = '/content/drive/MyDrive/Colab Notebooks/CnnDailyDataset/MySummaries'
    #filename = "a.txt"
    file_path = os.path.join(directory, filename)
    if not os.path.isdir(directory):
        os.mkdir(directory)
    file = open(file_path, "w", encoding='utf-8')
    file.write(document)
    file.close()
    
    
def createSummary(sentences,sentencesRank,sentenceAmount):
    temp=sorted(sentencesRank)
    threshold=temp[-sentenceAmount]
    summarySentencesIndexes=[]

    for i in range(len(sentencesRank)):
        if sentencesRank[i]>=threshold:
            summarySentencesIndexes.append(i)

    #print(summarySentencesIndexes)
    summary=""
    for i in range(len(summarySentencesIndexes)):
        summary=summary + ' ' +sentences[summarySentencesIndexes[i]]
  
    return summary

def mainCreateSummaries(corpus):
    corpus=cleanDocument(corpus) # Clean Paranthesis
    sentences= sent_tokenize(corpus)
    
    initialRank=allCorpusSentenceRanking(sentences,corpus)

    similarityMatrix=createGraph(sentences) # create matrix ( Graph) shows similarities of sentences

    newRank=findHighestSimilarityRank(similarityMatrix, initialRank)

    #summaryPercentage=0.3
    #sentenceNumberInSummary=int(len(sentences)*summaryPercentage)
    sentenceNumberInSummary=1
    if len(sentences)>2:
        sentenceNumberInSummary=3


    lastSummary=createSummary(sentences,newRank,sentenceNumberInSummary)
    return lastSummary    

startTimeforOverall = time.time()
all_hypothesis=[]
all_references=[]

#documentNumber
N=10   ## How many documents do you want summarized over the CNN/Daily Mail dataset? Limit 11490
startN=0

for d in range(N):
    startTimeforDocument = time.time()
    corpus=dataset['test']['article'][startN+d]
    temp=mainCreateSummaries(corpus)
    print("Document:",startN+d+1)
    print("News sentence number:",textSentenceCount(corpus))
    #print("News: ",corpus)
    #print("------------")
    tempHighlight=dataset['test']['highlights'][startN+d].replace('\n',' ')
    print("Highlight sentence number:",textSentenceCount(tempHighlight))
    #print("Highlight: ",tempHighlight)
    #print("------------")
    print("Summary sentence number:",textSentenceCount(temp))
    #print("Summary: ", temp)
    elapsedTimeforDocument = time.time() - startTimeforDocument
    elapsedTimeforAll = time.time() - startTimeforOverall
    print('Document processing time: '+time.strftime("%M:%S", time.gmtime(elapsedTimeforDocument)))
    print('Total processing time: '+time.strftime("%d:%H:%M:%S", time.gmtime(elapsedTimeforAll)))
    print("###################################################")
    all_hypothesis.append(temp)
    all_references.append(tempHighlight)
    
    
directoryDocument='data/CnnDailyDataset/Documents'
directoryHighlights='data/CnnDailyDataset/Highlights' # references 
directoryMySummaries='data/CnnDailyDataset/MySummaries' # hypothesis

for p in range(N):
    temp=str(p+1)
    fileNameDocument='News'+temp+'.txt'
    fileNameHighlight='Highlight'+'.A.'+temp+'.txt' #model gold
    fileNameMySummary='MySummary.'+temp+'.txt' # system my 
    #saveFile(directoryDocument,fileNameDocument,dataset['train']['article'][p])
    #saveFile(directoryHighlights,fileNameHighlight,all_references[p])
    saveFile(directoryMySummaries,fileNameMySummary,all_hypothesis[p])
    print(p+1)

print("Files are ready")


rougeEvaluation(all_hypothesis, all_references)