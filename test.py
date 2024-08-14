from __future__ import division
import string
import math

tokenize = lambda doc: doc.lower().split(" ")

document0 = "China has a strong economy that is growing at a rapid pace. However politically it differs greatly from the US Economy." 
document1 = "At last, China seems serious about confronting an endemic problem: domestic violence and corruption." 
document2 = "Japan's prime minister, Shinzo Abe, is working towards healing the economic turmoil in his own country for his view on the future of his people." 
document3 = "Vladimir Putin is working hard to fix the economy in Russia as the Ruble has tumbled." 
document4 = "What's the future of Abenomics? We asked Shinzo Abe for his views" 
document5 = "Obama has eased sanctions on Cuba while accelerating those against the Russian Economy, even as the Ruble's value falls almost daily." 
document_6 = "Vladimir Putin is riding a horse while hunting deer. Vladimir Putin always seems so serious about things - even riding horses. Is he crazy?"

all_documents = document0, document1, document2, document3, document4, document5, document_6

def jaccard_similarity(query, document): 
    intersection = set(query).intersection(set(document)) 
    union = set(query).union(set(document)) 
    return len(intersection)/len(union)


def termfrequency(term, tokenizeddocument): 
    return tokenizeddocument.count(term)

def sublineartermfrequency(term, tokenizeddocument): 
    count = tokenizeddocument.count(term) 
    if count == 0: 
        return 0 
    return 1 + math.log(count)


def augmentedtermfrequency(term, tokenizeddocument): 
    maxcount = max(termfrequency(t, tokenizeddocument) for t in tokenizeddocument) 
    return (0.5 + ((0.5 * termfrequency(term, tokenizeddocument))/maxcount))

def inversedocumentfrequencies(tokenizeddocuments): 
    idfvalues = {} 
    alltokensset = set(item for sublist in tokenizeddocuments for item in sublist) 
    for tkn in alltokensset: 
        containstoken = map(lambda doc: tkn in doc, tokenizeddocuments) 
        idfvaluestkn = 1 + math.log(len(tokenizeddocuments)/(sum(containstoken))) 
        return idf_values
    
def tfidf(documents): 
    tokenizeddocuments = tokenize(d) for d in documents:
    idf = inversedocumentfrequencies(tokenizeddocuments)
    tfidfdocuments = for document in tokenizeddocuments: 
    doctfidf = for term in idf.keys(): 
    tf = sublineartermfrequency(term, document) doctfidf.append(tf * idfterm) tfidfdocuments.append(doctfidf) 
    return tfidf_documents
