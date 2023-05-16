import os, gdal

in_path = 'D:/TIFF DATA/SUMATERA/'
input_filename = 'L8_1-15_04_19.tif'

out_path = 'D:/TIFF DATA/SUMATERA/Out/'
output_filename = 'tile_'

tile_size_x = 50
tile_size_y = 70

ds = gdal.Open(in_path + input_filename)
band = ds.GetRasterBand(1)
xsize = band.XSize
ysize = band.YSize

for i in range(0, xsize, tile_size_x):
    for j in range(0, ysize, tile_size_y):
        com_string = "gdal_translate -of GTIFF -srcwin " + str(i)+ ", " + str(j) + ", " + str(tile_size_x) + ", " + str(tile_size_y) + " " + str(in_path) + str(input_filename) + " " + str(out_path) + str(output_filename) + str(i) + "_" + str(j) + ".tif"
        os.system(com_string)
        
        
        
#-------------------------- Text NLP
import nltk as lt
lt.download(['punkt','averaged_perceptron_tagger','maxent_ne_chunker','words'])

sentence = """We learn python every morning and Jhon didn't like it."""
tokens = lt.word_tokenize(sentence)
print(tokens)

tagged = lt.pos_tag(tokens)
print(tagged)

entities = lt.chunk.ne_chunk(tagged)
print(entities)

from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk

sentence = """We learn python every morning and Jhon didn't like it.
              Jhon as a programmer in UBM."""

tokens = word_tokenize(sentence)
pos_tags = pos_tag(tokens)
entities = ne_chunk(pos_tags)

for entity in entities:
    if hasattr(entity, 'label'):
        print(entity.label(), ' '.join(c[0] for c in entity))

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

docA = 'Manajemen transaksi logistik'
docB = 'Pengetahuan antar individu'
docC = 'Dalam manajemen pengetahuan terdapat transfer pengetahuan logistik'

bagOfWordsA = docA.split(' ')
bagOfWordsB = docB.split(' ')
bagOfWordsC = docC.split(' ')

uniqueWords = set(bagOfWordsA).union(set(bagOfWordsB).union(set(bagOfWordsC)))
print(uniqueWords)

numOfWordsA = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsA:
    numOfWordsA[word] += 1

numOfWordsB = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsB:
    numOfWordsB[word] += 1
    
numOfWordsC = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsC:
    numOfWordsB[word] += 1

def computeTF(wordDict, bagOfWords):
    tfDict = {}
    bagOfWordsCount = len(bagOfWords)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsCount)
    return tfDict

tfA = computeTF(numOfWordsA, bagOfWordsA)
tfB = computeTF(numOfWordsB, bagOfWordsB)
tfC = computeTF(numOfWordsC, bagOfWordsC)

print('Trem Frekuensi 1: ', tfA)
print('Trem Frekuensi 2: ', tfB)
print('Trem Frekuensi 3: ', tfC)

from pandas._libs.lib import indices_fast
def computeIDF(documents):
    import math
    N = len(documents)
    
    idfDict = dict.fromkeys(documents[0].keys(), 0)
    for document in documents:
        for word, val in document.items():
            if val > 0:
                idfDict[word] += 1
    
    for word, val in idfDict.items():
        idfDict[word] = math.log(N / float(val))
    return idfDict

idfs = computeIDF([numOfWordsA, numOfWordsB, numOfWordsC])
print(idfs)

def computeTFIDF(tfBagOfWords, idfs):
    tfidf = {}
    for word, val in tfBagOfWords.items():
        tfidf[word] = val * idfs[word]
    return tfidf

tfidfA = computeTFIDF(tfA, idfs)
tfidfB = computeTFIDF(tfB, idfs)
tfidfC = computeTFIDF(tfC, idfs)

df = pd.DataFrame([tfidfA, tfidfB, tfidfC])
print(df)

vectorizer = TfidfVectorizer() # Coba pake modul sklearn
vectors = vectorizer.fit_transform([docA, docB, docC])
feature_names = vectorizer.get_feature_names_out()
dense = vectors.todense()
denselist = dense.tolist()
df = pd.DataFrame(denselist, columns=feature_names)
print(df)

###--------- CV
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from google.colab import drive
drive.mount('/content/drive')

path = 'drive/MyDrive/DataImage'
load_im = cv.imread(path + '/IMG00007.JPG')

plt.imshow(cv.cvtColor(load_im, cv.COLOR_BGR2RGB))
# plt.imshow(load_im)
plt.show()

import numpy as np

pixels = load_im.reshape(-1, load_im.shape[-1])
histograms = [np.histogram(channel, bins=256, range=[0, 256])[0] for channel in pixels.T]

# Plot the histograms for each channel
plt.figure()
plt.title('Image Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

colors = ['red', 'green', 'blue']  # Customize the colors for each channel
for histogram, color in zip(histograms, colors):
    plt.plot(histogram, color=color)

plt.show()
