# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 16:07:25 2018

@author: Yigao
"""

import re
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt

## create a tokenizer
hfilename = "file.txt"
linecount=0
hashcount=0
wordcount=0
BagOfWords=[]
BagOfHashes=[]
BagOfLinks=[]
with open(hfilename, "r") as file:
    for line in file:
        #print(line,"\n")
        tweetSplitter = TweetTokenizer(strip_handles=True, reduce_len=True)
        WordList=tweetSplitter.tokenize(line)
        #WordList2=word_tokenize(line)
        #linecount=linecount+1
        #print(WordList)
        #print(len(WordList))
        #print(WordList[0])
        #print(WordList2)
        #print(len(WordList2))
        #print(WordList2[3:6])
        #print("NEXT..........\n")
        regex1=re.compile('^#.+')
        regex2=re.compile('[^\W\d]') #no numbers
        regex3=re.compile('^http*')
        regex4=re.compile('.+\..+')
        for item in WordList:
            if(len(item)>2):
                if((re.match(regex1,item))):
                    #print(item)
                    newitem=item[1:] #remove the hash
                    BagOfHashes.append(newitem)
                    hashcount=hashcount+1
                elif(re.match(regex2,item)):
                    if(re.match(regex3,item) or re.match(regex4,item)):
                        BagOfLinks.append(item)
                    else:
                        BagOfWords.append(item)
                        wordcount=wordcount+1
                else:
                    pass
            else:
                pass
#print(linecount)            
#print(BagOfWords)
#print(BagOfHashes)
#print(BagOfLinks)
BigBag=BagOfWords+BagOfHashes

## create Word Cloud
IgnoreThese=[] #other irrelevant words
filtered_words = [] #list of words ready for wordcloud
for word in BigBag:
    if (word.lower() not in stopwords.words()) and (word.lower() not in IgnoreThese):
        filtered_words.append(word.lower())
word_string = " ".join(filtered_words)
with open("wordcloud.txt", "w") as f:
    f.write(word_string)
with open("tableau.txt", "w") as f:
    for s in filtered_words:
        f.write("%s\n" % s)
TwitterWordCloud = WordCloud(width = 800, height = 800, background_color = "white", stopwords = None,
                             min_font_size = 10).generate(word_string)
plt.figure(figsize = (8,8), facecolor = None)
plt.imshow(TwitterWordCloud)
plt.axis("off")
plt.tight_layout(pad = 0)
plt.show()