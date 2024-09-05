from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import numpy as np
import timeit

from TestResult import TestResult
from AnomalyClassifier import AnomalyClassifier
from ResultMetrics import ResultMetrics
from Constants import Constants

from MajorityRuleAnomalyClassifier import MajorityRuleAnomalyClassifier


#This class runs the tests and returns the results
class TestRunner:
    def __init__(self, trainingSample, testingSample, groundTruth, n_estimators, contamination, max_samples): 
        self.__trainingSample = trainingSample
        self.__n_estimators = n_estimators
        self.__contamination = contamination
        self.__testingSample = testingSample
        self.__max_samples = max_samples
        self.__groundTruth = groundTruth
        self.__originalTestingSample = testingSample
        self.__originalTrainingSample = trainingSample
        self.__classifier = None

    #Calculates the result metrics based on the classification results
    def __calculateResultMetrics (self, classificationResults): 
        accuracy = accuracy_score(self.__groundTruth, classificationResults)
        precision = precision_score(self.__groundTruth, classificationResults, pos_label=Constants.OUTLIERS, zero_division=1)
        recall = recall_score(self.__groundTruth, classificationResults, pos_label=Constants.OUTLIERS, zero_division=1)
        f1 = f1_score(self.__groundTruth, classificationResults, pos_label=Constants.OUTLIERS, zero_division=1)
        confusionMatrix = confusion_matrix(self.__groundTruth, classificationResults, labels=[Constants.INLIERS, Constants.OUTLIERS])
        
        return ResultMetrics(accuracy, precision, recall, f1, confusionMatrix)

    #Prepares the test by training the model
    def __prepareTest(self): 
        self.__classifier = MajorityRuleAnomalyClassifier(self.__trainingSample, self.__n_estimators, self.__contamination, self.__max_samples)
        self.__classifier.trainModel()
    
    #Trains the model with the current parameters and classifies the testing sample
    def runTest (self): 
        self.__prepareTest()
        classificationResults = self.__classifier.classify(self.__testingSample)
        return TestResult(self.__testingSample, self.__n_estimators, self.__contamination, self.__max_samples, classificationResults, self.__calculateResultMetrics(classificationResults))
    
    #Sets the parameter to the value given
    def __setChosenParameter(self, parameter, value): 
        if parameter == Constants.N_ESTIMATORS_ID: 
            self.__n_estimators = value
        elif parameter == Constants.CONTAMINATION_ID: 
            self.__contamination = value
        elif parameter == Constants.MAX_SAMPLES_ID: 
            self.__max_samples = value
        elif parameter == Constants.TESTING_SAMPLES_SIZE_ID:
            self.__testingSample = self.__originalTestingSample[:value]
        elif parameter == Constants.TRAINING_SAMPLES_SIZE_ID:
            self.__trainingSample = self.__originalTrainingSample[:value]
        else: 
            raise Exception('Invalid test parameter chosen for testing')
    
    #Used to run all tests where a parameter is increased in a range
    def increasingParameterTest (self, startingValue, endingValue, stepSize, parameter): 
        results = []

        for i in np.arange(startingValue, endingValue, stepSize): 
            self.__setChosenParameter(parameter, i)
            result = self.runTest()
            results.append(result)

        return results

    #evaluates the training time needed for the model to be trained
    def evaluateTrainingTime (self): 
        self.__classifier = MajorityRuleAnomalyClassifier(self.__trainingSample, self.__n_estimators, self.__contamination, self.__max_samples)
        return timeit.timeit(self.__classifier.trainModel, number=1)

    #To evaluate the classification time of a single sample
    def evaluateClassificationTime (self): 
        testingSample = self.__testingSample
        return timeit.timeit(lambda: self.__classifier.classify(testingSample), number=1)
    
    def increasingTimeTest(self, startingValue, endingValue, stepSize, parameter): 
        results = []

        for i in np.arange(startingValue, endingValue, stepSize): 
            self.__setChosenParameter(parameter, i)
            trainingTime = self.evaluateTrainingTime()
            classificationTime = self.evaluateClassificationTime()
            result = TestResult(self.__testingSample, self.__n_estimators, self.__contamination, self.__max_samples, [], [], trainingTime, classificationTime)
            results.append(result)

        return results
