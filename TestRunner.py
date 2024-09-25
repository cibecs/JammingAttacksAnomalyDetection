from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import numpy as np
import timeit

from TestResult import TestResult
from AnomalyClassifier import AnomalyClassifier
from ResultMetrics import ResultMetrics
from Parameters import Parameters

from MajorityRuleAnomalyClassifier import MajorityRuleAnomalyClassifier


#This class runs the tests and returns the results
class TestRunner:
    def __init__(self, trainingSample, testingSample, groundTruth, n_estimators, contamination, max_samples, classifierType, window_size): 
        self.__trainingSample = trainingSample
        self.__n_estimators = n_estimators
        self.__contamination = contamination
        self.__testingSample = testingSample
        self.__max_samples = max_samples
        self.__groundTruth = groundTruth
        self.__originalTestingSample = testingSample
        self.__originalTrainingSample = trainingSample
        self.__windowSize = window_size
        self.__classifierType = classifierType
        self.__classifier = None

    #Calculates the result metrics based on the classification results
    def __calculateResultMetrics (self, classificationResults): 
        groundTruth = self.__groundTruth[:len(classificationResults)]
        accuracy = accuracy_score(groundTruth, classificationResults)
        precision = precision_score(groundTruth, classificationResults, pos_label=Parameters.OUTLIERS, zero_division=1)
        recall = recall_score(groundTruth, classificationResults, pos_label=Parameters.OUTLIERS, zero_division=1)
        f1 = f1_score(groundTruth, classificationResults, pos_label=Parameters.OUTLIERS, zero_division=1)
        confusionMatrix = confusion_matrix(groundTruth, classificationResults, labels=[Parameters.INLIERS, Parameters.OUTLIERS])
        
        return ResultMetrics(accuracy, precision, recall, f1, confusionMatrix)

    def __getClassifier (self): 
        if self.__classifierType == Parameters.STANDARD_ISOLATION_FOREST: 
            return AnomalyClassifier(self.__trainingSample, self.__n_estimators, self.__contamination, self.__max_samples)
        elif self.__classifierType == Parameters.MAJORITY_RULE_ISOLATION_FOREST: 
            return MajorityRuleAnomalyClassifier(self.__trainingSample, self.__n_estimators, self.__contamination, self.__max_samples, self.__windowSize)
        else: 
            raise Exception('Invalid classifier type chosen for testing')
        

    #Prepares the test by training the model
    def __prepareTest(self): 
        self.__classifier = self.__getClassifier()
        self.__classifier.trainModel()
    
    #Sets the parameter to the value given
    def __setChosenParameter(self, parameter, value): 
        if parameter == Parameters.N_ESTIMATORS_ID: 
            self.__n_estimators = value
        elif parameter == Parameters.CONTAMINATION_ID: 
            self.__contamination = value
        elif parameter == Parameters.MAX_SAMPLES_ID: 
            self.__max_samples = value
        elif parameter == Parameters.TESTING_SAMPLES_SIZE_ID:
            self.__testingSample = self.__originalTestingSample[:value]
        elif parameter == Parameters.TRAINING_SAMPLES_SIZE_ID:
            self.__trainingSample = self.__originalTrainingSample[:value]
        elif parameter == Parameters.WINDOW_SIZE_ID:
            self.__windowSize = value
        else: 
            raise Exception('Invalid test parameter chosen for testing')
    
     #Trains the model with the current parameters and classifies the testing sample
    def runTest (self): 
        self.__prepareTest()
        classificationResults = self.__classifier.classify(self.__testingSample)
        return TestResult(self.__testingSample, self.__n_estimators, self.__contamination, self.__max_samples, classificationResults, self.__calculateResultMetrics(classificationResults))
    
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
        self.__classifier = self.__getClassifier()
        return timeit.timeit(self.__classifier.trainModel, number=1) * 1000

    #To evaluate the classification time of a single sample
    def evaluateClassificationTime (self): 
        testingSample = self.__testingSample
        return timeit.timeit(lambda: self.__classifier.classify(testingSample), number=1) * 1000
    
    #Evaluates training time with a parameter increased in a range
    def increasingTimeTest(self, startingValue, endingValue, stepSize, parameter): 
        results = []

        for i in np.arange(startingValue, endingValue, stepSize): 
            self.__setChosenParameter(parameter, i)
            trainingTime = self.evaluateTrainingTime()
            classificationTime = self.evaluateClassificationTime()
            result = TestResult(self.__testingSample, self.__n_estimators, self.__contamination, self.__max_samples, [], [], trainingTime, classificationTime)
            results.append(result)

        return results
