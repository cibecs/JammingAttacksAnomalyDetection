from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import numpy as np

from TestResult import TestResult
from AnomalyClassifier import AnomalyClassifier
from ResultMetrics import ResultMetrics



class ParametersBasedTestRunner:
    def __init__(self, trainingSample, testingSample, groundTruth, n_estimators, contamination, max_samples): 
        self.__trainingSample = trainingSample
        self.__n_estimators = n_estimators
        self.__contamination = contamination
        self.__testingSample = testingSample
        self.__max_samples = max_samples
        self.__groundTruth = groundTruth

    
    def variableContaminationTest (self, startingContaminationValue, endingContaminationValue, stepSize): 
        results = []
        
        for i in np.arange(startingContaminationValue, endingContaminationValue, stepSize): 
            classifier = AnomalyClassifier(self.__trainingSample, self.__n_estimators, i, self.__max_samples)
            classifier.trainModel()
            classificationResults = classifier.classify(self.__testingSample)
            results.append(TestResult(self.__testingSample, self.__n_estimators, i, self.__max_samples, classificationResults, self.calculateResultMetrics(classificationResults)))

        return results
    
    
    def calculateResultMetrics (self, classificationResults): 
        accuracy = accuracy_score(self.__groundTruth, classificationResults)
        precision = precision_score(self.__groundTruth, classificationResults)
        recall = recall_score(self.__groundTruth, classificationResults)
        f1 = f1_score(self.__groundTruth, classificationResults)
        confusionMatrix = confusion_matrix(self.__groundTruth, classificationResults, labels=[-1, 1])
        
        return ResultMetrics(accuracy, precision, recall, f1, confusionMatrix)