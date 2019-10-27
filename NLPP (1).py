#!/usr/bin/env python
# coding: utf-8

# In[4]:


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 


# In[5]:


stop_words=set(stopwords.words('french'))


# In[6]:


sentence = open(r"FICHIER.txt")  
a=sentence.read()
print(a)


# In[7]:


def wcount(sentence):
    word_tokens = word_tokenize(a) 
    filtered_sentence = [w for w in word_tokens if not w in stop_words] 
  
    filtered_sentence = [] 
  
    for w in word_tokens: 
        if w not in stop_words: 
            filtered_sentence.append(w) 
    return(filtered_sentence)
  


# In[8]:


b=wcount(a)


# In[9]:


chn=" "
chn=chn.join(b)
print(chn)


# In[10]:


from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')

result = tokenizer.tokenize(chn)

print(result)


# In[11]:


chn=" "
chn=chn.join(result)
print(chn)


# In[12]:


nltk_tokens = nltk.word_tokenize(chn)  	

tokens=list(nltk.bigrams(nltk_tokens))


# In[13]:


tokenized=[('mot1','mot2'),('mot3','mot4')]
for token in tokens:
    if token in tokenized:
        print(token)


# In[14]:


resulta={}
tokenized=['mot1 mot2','mot3 mot4']
for token in tokens:
    chn=" "
    chn=chn.join(token) 
    if(chn in resulta and chn in tokenized):
        resulta[chn]=resulta[chn]+1
    elif(chn not in resulta and chn in tokenized):
        resulta[chn]=1
print(resulta)



        






