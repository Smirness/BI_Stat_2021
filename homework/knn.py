import numpy as np
import heapq
import collections

class KNNClassifier:
    """
    K-neariest-neighbor classifier using L1 loss
    """
    
    def __init__(self, k=1):
        self.k = k
    

    def fit(self, X, y):
        self.train_X = X
        self.train_y = y

    def distances(self, X, n_loops=0):
        """
        X, np array (num_samples, num_features) - samples to run
        through the model
        num_loops, int - which implementation to use
        """

        if n_loops == 0:
            distances = self.compute_distances_no_loops(X)
        elif n_loops == 1:
            distances = self.compute_distances_one_loop(X)
        else:
            distances = self.compute_distances_two_loops(X)

        return distances
        pass


    def predict(self, distances):
        """
        Uses the KNN model to predict classes for the data samples provided
        Arguments:
        Returns:
        predictions, np array of ints (num_samples) - predicted class
           for each sample
        """

        if len(np.unique(self.train_y)) == 2:
            return self.predict_labels_binary(distances)
        else:
            return self.predict_labels_multiclass(distances)
        pass


    def compute_distances_two_loops(self, X):
        """
        Computes L1 distance from every sample of X to every training sample
        Uses simplest implementation with 2 Python loops

        Arguments:
        X, np array (num_test_samples, num_features) - samples to run
        
        Returns:
        distances, np array (num_test_samples, num_train_samples) - array
           with distances between each test and each train sample
        """
        n_train = self.train_X.shape[0]
        n_test = X.shape[0]
        dists = np.zeros((n_test, n_train))

        for i in range(n_test):
            for j in range(n_train):
                dists[i, j] = np.sum(np.abs(X[i] - self.train_X[j]))

        return dists
        pass


    def compute_distances_one_loop(self, X):
        """
        Computes L1 distance from every sample of X to every training sample
        Vectorizes some of the calculations, so only 1 loop is used

        Arguments:
        X, np array (num_test_samples, num_features) - samples to run
        
        Returns:
        distances, np array (num_test_samples, num_train_samples) - array
           with distances between each test and each train sample
        """
        n_train = self.train_X.shape[0]
        n_test = X.shape[0]
        dists = np.zeros((n_test, n_train))

        for i in range(n_test):
            dists[i] = np.sum(np.abs(X[i] - self.train_X), axis=1)

        return dists
        pass


    def compute_distances_no_loops(self, X):
        """
        Computes L1 distance from every sample of X to every training sample
        Fully vectorizes the calculations using numpy

        Arguments:
        X, np array (num_test_samples, num_features) - samples to run
        
        Returns:
        distances, np array (num_test_samples, num_train_samples) - array
           with distances between each test and each train sample
        """
        return np.sum(np.abs(X[:, np.newaxis] - self.train_X), axis=2)
        pass


    def predict_labels_binary(self, distances):
        """
        Returns model predictions for binary classification case
        
        Arguments:
        distances, np array (num_test_samples, num_train_samples) - array
           with distances between each test and each train sample
        Returns:
        pred, np array of bool (num_test_samples) - binary predictions 
           for every test sample
        """

        n_test = distances.shape[0]
        prediction = np.tile('', n_test)

        for i in range(n_test):
            min_dists = heapq.nsmallest(self.k, distances[i])

            min_dists_ind = []
            for dist in min_dists:
                min_dists_ind.append(np.where(distances[i] == dist))

            lst_nn = []
            for ind in min_dists_ind:
                lst_nn.append(self.train_y[ind][0][0])

            count_nn = collections.Counter(lst_nn)
            prediction[i] = max(count_nn, key=count_nn.get)

        return prediction
        pass


    def predict_labels_multiclass(self, distances):
        """
        Returns model predictions for multi-class classification case
        
        Arguments:
        distances, np array (num_test_samples, num_train_samples) - array
           with distances between each test and each train sample
        Returns:
        pred, np array of int (num_test_samples) - predicted class index 
           for every test sample
        """

        n_test = distances.shape[0]
        prediction = np.tile('', n_test)

        for i in range(n_test):
            min_dists = heapq.nsmallest(self.k, distances[i])

            min_dists_ind = []
            for dist in min_dists:
                min_dists_ind.append(np.where(distances[i] == dist))

            lst_nn = []
            for ind in min_dists_ind:
                lst_nn.append(self.train_y[ind][0][0])

            count_nn = collections.Counter(lst_nn)
            prediction[i] = max(count_nn, key=count_nn.get)

        return prediction
        pass

