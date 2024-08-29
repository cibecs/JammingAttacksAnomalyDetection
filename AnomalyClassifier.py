from sklearn.ensemble import IsolationForest

class AnomalyClassifier: 
    

    def __init__ (self, trainingSample, n_estimators, contamination, max_samples): 
        self.__trainingSample = trainingSample
        self.__n_estimators = n_estimators
        self.__contamination = contamination
        self.__max_samples = max_samples
        self.__model = None
    #trains the model on the parameters given in the constructor
    def trainModel (self):
        self.__model = IsolationForest(n_estimators=self.__n_estimators, contamination=self.__contamination, max_samples=self.__max_samples)
        self.__model.fit(self.__trainingSample)
    #classifies the passed data (the data should be a numpy array)

    def classify (self, data): 
        if (self.__model is None): 
            raise Exception('Model not trained')
        return self.__model.predict(data)
    
    def setTrainingSample (self, trainingSample): 
        self.__trainingSample = trainingSample
        self.trainModel()
    
    def setN_estimators (self, n_estimators): 
        self.__n_estimators = n_estimators
        self.trainModel()
    
    def setContamination (self, contamination):
        self.__contamination = contamination
        self.trainModel()
    