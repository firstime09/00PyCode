import cv2
import matplotlib.pyplot as plt

location_path = r"D:\00PyCode\Prak UBM\00_Image"
img_1 = cv2.imread(location_path + '/citrababon_bmp.bmp')
b, g, r = cv2.split(img_1)
histogram = cv2.calcHist([img_1], [0], None, [256], [0, 256])

cv2.imshow('Name_RGB', img_1)
cv2.imshow('Name_b', b)
cv2.imshow('Name_g', g)
cv2.imshow('Name_r', r)
plt.plot(histogram)
plt.show()

#Opsional
"""cv2.imshow('Name',img_1)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

## Materi Kecerdasan Buatan GA - Praktek
import random, datetime

def generateParent(length):
    genes = list("")
    for i in range(0,length):
        geneIndex = random.randint(0, len(geneset) -1);
        genes.append(geneset[geneIndex])
    return(''.join(genes))

def getFitness(candidate, target):
   fitness = 0
   for i in range(0, len(candidate)):
       if target[i] == candidate[i]:
           fitness += 1
   return(fitness)

def mutate(parent):
   geneIndex = random.randint(0, len(geneset) -1);
   index = random.randint(0, len(parent) - 1)
   genes = list(parent)
   genes[index] = geneset[geneIndex]
   return(''.join(genes))

def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    fitness = getFitness(candidate, target)
    print("%s\t%i\t%s" % (candidate, fitness, str(timeDiff)))
