import math
import operator
from sklearn.cross_validation import train_test_split
import csv
from numpy import array
import sys
import numpy as np


# function to calcualte Euclidean distance between two instances
def euclidean_dist(instance1,instance2,length):
    distance=0
    for x in range(length):
        instance1[x]=int(instance1[x])
        instance2[x]=int(instance2[x])
        distance +=(pow((instance1[x]-instance2[x]),2))
    return int(math.sqrt(distance))

# Calculate the K-Nearest Neighbors
def getNeighbors(trainingSet,testInstance,k):
    distances=[]
    length=len(testInstance)-1
    for x in range(len(trainingSet)):
        dist=euclidean_dist(testInstance,trainingSet[x],length)
        distances.append((trainingSet[x],dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors=[]
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

def getResponses(neighbors):
    classVotes={}
    for x in range(len(neighbors)):
        response=neighbors[x][-1]
        if response in classVotes:
            classVotes[response]+=1
        else:
            classVotes[response]=1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]

def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0

def main():
    #filename = sys.argv[1]
    filename="C:\\Users\\AadarshSam\\Desktop\\0.spice.train.csv"
    lines = csv.reader(open(filename, "rb"))
    new_list = list(lines)
    count=0
    max_len=len(max(new_list,key=len))
    final_list=[[]for i in range(1,max_len)]
    for small_list in new_list:
        for i in range(1,max_len):
            if(len(small_list)==i):
                final_list[i-1].append(small_list)

    testdata=[[4,1,3,2,0]]
    testSet=np.array(testdata,dtype='|S4')
    testSet=testSet.astype(np.float)

    for list1 in testdata:
        my_length=len(list1)
    trainingSet=array(final_list[my_length-1],dtype='|S4')
    trainingSet=trainingSet.astype(np.float)

    print('Training set: ' + repr(len(trainingSet)))
    print('Test set: ' + repr(len(testSet)))
    predictions=[]
    k = 5
    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponses(neighbors)
        predictions.append(result)
        print(x)
        print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
    accuracy = getAccuracy(testSet, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')

main()
