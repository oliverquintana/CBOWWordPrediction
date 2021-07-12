from os.path import isfile, join
from os import system, name
from os import listdir
import pandas as pd
import numpy as np
import chardet
import math

def readFile(fname):
    try:
        f = open(fname, 'r')
        content = f.read()
        f.close()

    except:
        with open(fname, 'rb') as f:
            content_bytes = f.read()
        detected = chardet.detect(content_bytes)
        encoding = detected['encoding']

        f = open(fname, mode = 'r', encoding = encoding)
        content = f.read()
        f.close()

    return content

def distDocs(doc1, doc2):

    return np.sqrt(np.sum(np.power(doc1 - doc2, 2)))

def angleDocs(doc1, doc2):

    num = np.dot(doc1, doc2)
    den1 = np.sqrt(np.sum(np.power(doc1, 2)))
    den2 = np.sqrt(np.sum(np.power(doc2, 2)))

    return num / (den1 * den2)

def vectDocs(docs, docNames, printLen = True):

    alphabetLow  = ['á', 'é', 'í', 'ó', 'ú', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'j', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabetHigh = ['Á', 'É', 'Í', 'Ó', 'Ú', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    alphaHigh2Low = {
        'A' : 'a', 'B' : 'b', 'C' : 'c', 'D' : 'd', 'E' : 'e', 'F' : 'f', 'G' : 'g',
        'H' : 'h', 'I' : 'i', 'J' : 'j', 'K' : 'k', 'L' : 'l', 'M' : 'm', 'N' : 'n',
        'Ñ' : 'ñ', 'O' : 'o', 'P' : 'p', 'Q' : 'q', 'R' : 'r', 'S' : 's', 'T' : 't',
        'U' : 'u', 'V' : 'v', 'W' : 'w', 'X' : 'x', 'Y' : 'y', 'Z' : 'z', 'Á' : 'á',
        'É' : 'é', 'Í' : 'í', 'Ó' : 'ó', 'Ú' : 'ú'
    }


    # Diccionarios con frecuencia para cada documento
    dictsDocs = []
    for j, doc in enumerate(docs):
        dictsDocs.append({})
        word = ''
        lenDoc = len(doc)
        for i, char in enumerate(doc):
            if i == lenDoc - 1:
                word += char
                if word not in list(dictsDocs[j].keys()):
                    dictsDocs[j][word] = 1
                else:
                    dictsDocs[j][word] += 1

            elif char in alphabetHigh:
                char = alphaHigh2Low[char]
                word += char

            elif char in alphabetLow:
                word += char

            elif char == ' ' or char == '\n':
                if word not in list(dictsDocs[j].keys()):
                    dictsDocs[j][word] = 1
                else:
                    dictsDocs[j][word] += 1
                word = ''

        dictsDocs[j].pop('', None)
        if printLen:
            print('Doc {}. {} : {}'.format(j+1, docNames[j][:-4], np.sum(list(dictsDocs[j].values()))) )

    return dictsDocs

def printDict(dict):

    for key, value in dict.items():
        print('{} : {}'.format(key, value))


def vectDict(tokens_in):
    tokenDict = {}
    tokens = list(set(tokens_in))
    for i, token in enumerate(tokens):
        tokenDict[token] = i

    return tokenDict


