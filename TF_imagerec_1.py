##########################################
# image recognition - by sent dex
##########################################
# if you're on 32bit OS:
# import Image

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
from functools import reduce # reduce was moved to functools hence you need to import this
from collections import Counter

##########################################
# read all images -> save in txt
##########################################
def createExamples():
    numberArrayExamples = open('numArEx.txt', 'a')
    numbersWeHave = range(0,10)
    versionWeHave = range(1,10)
    for eachNum in numbersWeHave:
        for eachVer in versionWeHave:
            #print(str(eachNum)+'.'+str(eachNum))
            imgFilePath = 'images/numbers/'+str(eachNum)+'.'+str(eachVer)+'.png'
            ei = Image.open(imgFilePath)
            eiar = np.array(ei)
            eiar1 = str(eiar.tolist()) # type change: numpy array -> normal python list
            lineToWrite = str(eachNum)+'::'+eiar1+'\n'
            numberArrayExamples.write(lineToWrite)
    #help(eiar.tolist())

##########################################
# training function
##########################################
def threashold(imageArray):
    balanceAr=[]
    newAr=imageArray
    for eachRow in imageArray:
        for eachPix in eachRow:
            #print(eachPix)
            avgNum = reduce(lambda x,y: x+y, eachPix[:3]) / len(eachPix[:3])
            balanceAr.append(avgNum)
            #print(eachPix[:3])
            #time.sleep(5)
            balance = reduce(lambda x,y: x+y, balanceAr) / len(balanceAr)
    for eachRow in newAr:
        for eachPix in eachRow:
            if reduce(lambda x,y: x+y, eachPix[:3]) / len(eachPix[:3]) > balance:
                #255 black, 0 white
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                eachPix[3] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                eachPix[3] = 255
    return newAr

def whatNumIsThis(filePath):
    matchedAr = []
    loadExamps = open('c:/work/python/numArEx.txt', 'r').read()
    loadExamps = loadExamps.split('\n')
    i = Image.open(filePath)
    iar = np.array(i)
    iar1 = iar.tolist()
    isQuestion = str(iar1)
    for eachExample in loadExamps:
        if len(eachExample) > 3:
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]
            eachPixEx = currentAr.split('],')
            eachPixInQ = isQuestion.split('],')
            x=0
            while x < len(eachPixEx):
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedAr.append(int(currentNum))
                x += 1
    print(matchedAr)
    x = Counter(matchedAr)
    print(x)

    graphX = []
    graphY = []

    for eachThing in x:
        print(eachThing)
        graphX.append(eachThing)
        print(x[eachThing])
        graphY.append(x[eachThing])

    fig = plt.figure()
    ax1 = plt.subplot2grid((4,4), (0,0), rowspan=1, colspan=4)
    ax2 = plt.subplot2grid((4,4), (1,0), rowspan=3, colspan=4)
    ax1.imshow(iar)
    ax2.bar(graphX, graphY, align='center')
    plt.ylim(350)
    plt.show()

if __name__ == '__main__':
    #createExamples()

##    #read image as numpy type
##    i1=Image.open('c:/work/python/images/numbers/0.1.png')
##    iar1=np.array(i1)
##    i2=Image.open('c:/work/python/images/numbers/y0.4.png')
##    iar2=np.array(i2)
##    i3=Image.open('c:/work/python/images/numbers/y0.5.png')
##    iar3=np.array(i3)
##    i4=Image.open('c:/work/python/images/sentdex.png')
##    iar4=np.array(i4)
##
##    #threashold(iar1) -> this was not in the original code
##    #call threadshold 
##    threashold(iar2)
##    threashold(iar3)
##    threashold(iar4)
##
##    #shaping grid
##    fig=plt.figure()
##    ax1=plt.subplot2grid((8,6), (0,0), rowspan=4, colspan=3)
##    ax2=plt.subplot2grid((8,6), (4,0), rowspan=4, colspan=3)
##    ax3=plt.subplot2grid((8,6), (0,3), rowspan=4, colspan=3)
##    ax4=plt.subplot2grid((8,6), (4,3), rowspan=4, colspan=3)
##
##    #put each image in each grid
##    ax1.imshow(iar1)
##    ax2.imshow(iar2)
##    ax3.imshow(iar3)
##    ax4.imshow(iar4)
##
##    #display 
##    plt.show()

    #you draw numbers in test.png & read
    whatNumIsThis('c:/work/python/images/test.png')


