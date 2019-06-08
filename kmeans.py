#IMPLEMENTING K-MEANS ALGORITHM

import math
from math import *
import numpy as np
import random
import matplotlib.pyplot as plt


class mykmeans:

	def __init__(self, **kwargs):
        
		self.nCluster = 8 #Default number of clusters set to 8
		self.maxIter = 10 #Default number of iteration of the k-means algorithm set to 10 (can be changed to a bigger value)
		self.tol = 1e-4 #Default tolerance with regard to inertia to declare convergence set to 1e-4
		self.centroids = []
		self.data = {}
		
		for key,value in kwargs.items():
		    if key == 'nCluster':
		        self.nCluster = value
		    if key == 'maxIter':
		        self.maxIter = value
		    if key == 'tol':
		        self.tol = value
		    elif(key != 'nCluster' and key != 'maxIter' and key != 'tol'):
		        print("unknown parameter")
		        break
             
	def euclidianDist(self,X,Y):
		return math.sqrt((X[0]-Y[0])**2+(X[1]-Y[1])**2)
    	
	def fit(self,dataList):
		self.centroids = random.sample(dataList, self.nCluster)
		rep = 1
		while(rep<=self.maxIter):
			rep += 1
			oldCentroids = self.centroids
			for dataPoint in dataList:
				dist = math.inf
				dataCentroid = (0,0)
				for centroid in self.centroids:
					if (dist > self.euclidianDist(dataPoint,centroid)):
						dist = self.euclidianDist(dataPoint,centroid)
						dataCentroid = centroid
				self.data[dataPoint] = dataCentroid
				
			print(self.centroids, '1')
			#Now we compute the new centroids
			if(rep<self.maxIter):
				ind = 0
				for centroid in self.centroids:
					newcentroid = centroid
					number = 1
					for dataPoint in dataList:
						if self.data[dataPoint] == centroid:
							newcentroid = (newcentroid[0]+dataPoint[0], newcentroid[1]+dataPoint[1])
							number += 1 
					self.centroids[ind] = (newcentroid[0]/number,newcentroid[1]/number)	
					ind += 1
			#Now we check if the tolerance is satisfied
			toleranceSatisfied = 0
			for i in range(len(oldCentroids)):
				if self.euclidianDist(oldCentroids[i],self.centroids[i])<self.tol:
					toleranceSatisfied += 1
			#If the tolerance is satisfied for all the centroids we can get out of the loop
			#if toleranceSatisfied == len(self.centroids):
				#break
				
	def setOfclusterId(self):
		setOfcluster = {}
		Id = 1
		#print(self.data)
		#print(self.centroids, 'haha')
		for centroid in self.centroids:
			setOfcluster[Id] = []
			for dataPoint in self.data:
				if self.data[dataPoint] == centroid:
					setOfcluster[Id].append(dataPoint)	
			Id += 1
		return setOfcluster
		
	def setOfCentroids(self):
		return self.centroids


##Test

#This algorithm is generalizable to any number of cluster

#We choose randomly 2 sets of 50 points

L = [(random.uniform(1,4),random.uniform(1,4)) for i in range(50)]
M = [(random.uniform(16,20),random.uniform(16,20)) for i in range(50)]
Data = L+M
g = mykmeans(nCluster = 2, maxIter = 10, tol = 1e-4)
g.fit(Data)
centroids = g.setOfCentroids()
newL,newM = g.setOfclusterId()[1], g.setOfclusterId()[2]  

print(newL,'First Set')
print(newM, 'Second Set')
print(centroids, 'Centroids')

#Now we can have a look on the results of our kmeans algorithm

for i in newL:
    plt.scatter(i[0],i[1], color='b')
for j in newM:
    plt.scatter(j[0],j[1], color='r') 
for k in centroids:
	plt.scatter(k[0],k[1], color='y')  
