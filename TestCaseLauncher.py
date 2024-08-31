import numpy as np

from Constants import Constants
from ParametersBasedTestRunner import ParametersBasedTestRunner
from FileHandler import FileHandler
from Plotter import Plotter

#---- PARAMETERS ----#

#---- DATA ----#
NORMAL_TRAFFIC_SIZE = 2000
NORMAL_TRAFFIC_FILE = 'data/normal_traffic.txt'

CONSTANT_JAMMING_SIZE = 2000
CONSTANT_JAMMING_FILE = 'data/constant_jammer.txt'

PERIODIC_JAMMING_SIZE = 2000
PERIODIC_JAMMING_FILE = 'data/periodic_jammer.txt'

#---- MODEL ----#
N_ESTIMATORS = 100
MAX_SAMPLES = 1.0
CONTAMINATION = 0.1



#---- CONTAMINATION TEST ----#
START_CONTAMINATION = 0.01
END_CONTAMINATION = 0.5
STEP_SIZE_CONTAMINATION = 0.01


#This class launches the test cases by setting the parameters and plots the results
class TestCaseLauncher: 

    def __init__(self): 
        self.__normalTraffic = FileHandler.readAndParseFile(NORMAL_TRAFFIC_FILE, NORMAL_TRAFFIC_SIZE)
        self.__constantJamming = FileHandler.readAndParseFile(CONSTANT_JAMMING_FILE, CONSTANT_JAMMING_SIZE)
        self.__periodicJamming = FileHandler.readAndParseFile(PERIODIC_JAMMING_FILE, PERIODIC_JAMMING_SIZE)
        self.__nEstimators = N_ESTIMATORS
        self.__maxSamples = MAX_SAMPLES
        self.__contamination = CONTAMINATION
        self.__pbtr = None
    
    #returns the ground truth for the various types of data
    def __getNormalTrafficGroundTruth(self): 
        return Constants.INLIERS * np.ones(len(self.__normalTraffic))
    def __getConstantJammingGroundTruth(self): 
        return Constants.OUTLIERS * np.ones(len(self.__constantJamming))
    def __getPeriodicJammingGroundTruth(self): 
        raise Exception('Not implemented')
    
    def __getJammingSignalAndGroundTruth(self, signalType):
        if signalType == Constants.CONSTANT_JAMMING: 
            return self.__constantJamming, self.__getConstantJammingGroundTruth()
        elif signalType == Constants.PERIODIC_JAMMING: 
            return self.__periodicJamming, self.__getPeriodicJammingGroundTruth()
        else: 
            raise Exception('Invalid signal type')
    
    #Prepares the model for the test
    def __prepareModel(self, jammingType):
        trainingSample = self.__normalTraffic
        jammingTestInput, jammingGroundTruth = self.__getJammingSignalAndGroundTruth(jammingType)
        testInput = np.concatenate((self.__normalTraffic, jammingTestInput))
        groundTruth = np.concatenate((self.__getNormalTrafficGroundTruth(), jammingGroundTruth))
        self.__pbtr = ParametersBasedTestRunner(trainingSample, testInput, groundTruth, self.__nEstimators, self.__contamination, self.__maxSamples)

    #Splits the data points based on the classification results
    def __separateInliersFromOutliers (self, inputData, classificationResults): 
        x = range(len(inputData))
        normal_x = [x[i] for i in range(len(x)) if classificationResults[i] == 1]
        normal_y = [inputData[i] for i in range(len(inputData)) if classificationResults[i] == 1]
        jamming_x = [x[i] for i in range(len(x)) if classificationResults[i] == -1]
        jamming_y = [inputData[i] for i in range(len(inputData)) if classificationResults[i] == -1]
        return [normal_x, jamming_x], [normal_y, jamming_y]
    
    #Plotting function for the scatter plot of inliers and outliers (shows the model classification)
    def __plotInliersOutliers (self, result, labels, colors, title, axisLabels):
            x,result = self.__separateInliersFromOutliers(result.inputData, result.classification)
            Plotter.scatterPlot(x, result, labels, colors, title, axisLabels)
    
    def __plotMetrics (self, x, results, labels, colors, title, axisLabels): 
            accuracy = [result.resultMetrics.accuracy for result in results]
            precision = [result.resultMetrics.precision for result in results]
            recall = [result.resultMetrics.recall for result in results]
            f1 = [result.resultMetrics.f1 for result in results]
            Plotter.plotInSameGraph(x, [accuracy, precision, recall, f1], labels, colors, title, axisLabels)

    #Simple normal traffic concatenated with constant jamming test
    def basicNormalJammingConcatenatedTest(self, jammingType, displayResultMetrics = True, displayPlot = True ): 
        self.__prepareModel(jammingType)
        result = self.__pbtr.runTest()
        if displayResultMetrics: 
            print(result)
        if displayPlot:
            self.__plotInliersOutliers(result, ['Normal Traffic', 'Jamming Signal'], ['b', 'r'], 'Basic Normal Traffic and Jamming Signal Concatenated Test', ['Data Point', 'RSSI[dBm]'])
    
    #Runs increasing contamination test and analyzes the result metrics (accuracy, precision, recall, f1, confusion matrix)
    def increasingContaminationTest (self, jammingType, displayResultMetrics = True, displayPlot = True):
        self.__prepareModel(jammingType)
        results = self.__pbtr.variableContaminationTest(START_CONTAMINATION, END_CONTAMINATION, STEP_SIZE_CONTAMINATION)
        if displayResultMetrics: 
            for result in results: 
                print(result)
        if displayPlot:
            x = np.arange(START_CONTAMINATION, END_CONTAMINATION, STEP_SIZE_CONTAMINATION)
            self.__plotMetrics(x, results, ['Accuracy', 'Precision', 'Recall', 'F1'], ['b', 'r', 'g', 'm'], 'Increasing Contamination Test', ['Contamination', 'Metric Value'])

    #Runs increasing number of estimators test and analyzes the result metrics 
