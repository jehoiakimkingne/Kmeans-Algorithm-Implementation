# Kmeans-Algorithm-Implementation
- This is my personal implementation of the kmeans algorithm with an example applied to a set of 2D data points.

- Launch your terminal and execute the python file, you will get a visualization of this kmeans algorithm on a set of 2D data points.

- Here I will give you some details on how to excecute this algorithm.

- For this algorithm, the interface is similar to python kmeans interface but with fewer methods (or functions).

- I impemented a class 'mykmeans' which will be used to apply kmeans algorithm on a set of data

  class mykmeans(nCluster = 8, maxIter=10, tol=1e-4) #Of course these values can be changed :
  
      - nCluster : The number of clusters to form as well as the number of centroids to generate
      - maxIter : Maximum number of iterations of the k-means algorithm for a single run, default : 10 
      - tol : Relative tolerance with regards to inertia to declare convergence, default : 1e-4 

- Example : Let's assume 'Data' is a list of variable number of 2D data points to which we would like to apply kmeans algorithm

      - First we initialize the clustering : g = mykmeans(nCluster = 2, maxIter = 10, tol = 1e-4)
      - Then we fit on the Data : g.fit(Data)
      - Finally we get the centroids and the set of clusters Id : clusters = g.setOfClusterId(), centroids = g.setOfCentroids()
      - We can visualize each of the data point using plt.scatter
