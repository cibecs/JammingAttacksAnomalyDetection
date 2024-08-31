import numpy as np

from Constants import Constants
from ParametersBasedTestRunner import ParametersBasedTestRunner
from FileHandler import FileHandler
from Plotter import Plotter

#---- PARAMETERS ----#

#---- DATA ----#
NORMAL_TRAFFIC_SIZE = 40000
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
START_CONTAMINATION = 0.1
END_CONTAMINATION = 0.2
STEP_SIZE_CONTAMINATION = 0.1


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
    def getNormalTrafficGroundTruth(self): 
        return Constants.INLIERS * np.ones(len(self.__normalTraffic))
    def getConstantJammingGroundTruth(self): 
        return Constants.OUTLIERS * np.ones(len(self.__constantJamming))
    def getPeriodicJammingGroundTruth(self): 
        raise Exception('Not implemented')
    
    def getJammingSignalAndGroundTruth(self, signalType):
        if signalType == Constants.CONSTANT_JAMMING: 
            return self.__constantJamming, self.getConstantJammingGroundTruth()
        elif signalType == Constants.PERIODIC_JAMMING: 
            return self.__periodicJamming, self.getPeriodicJammingGroundTruth()
        else: 
            raise Exception('Invalid signal type')

    #Splits the data points based on the classification results
    def separateInliersFromOutliers (self, inputData, classificationResults): 
        x = range(len(inputData))
        normal_x = [x[i] for i in range(len(x)) if classificationResults[i] == 1]
        normal_y = [inputData[i] for i in range(len(inputData)) if classificationResults[i] == 1]
        jamming_x = [x[i] for i in range(len(x)) if classificationResults[i] == -1]
        jamming_y = [inputData[i] for i in range(len(inputData)) if classificationResults[i] == -1]
        return [normal_x, jamming_x], [normal_y, jamming_y]
    
    #Simple normal traffic concatenated with constant jamming test
    def basicNormalJammingConcatenatedTest(self, jammingType, displayResultMetrics = True, displayPlot = True ): 
        trainingSample = self.__normalTraffic
        jammingTestInput, jammingGroundTruth = self.getJammingSignalAndGroundTruth(jammingType)
        testInput = np.concatenate((self.__normalTraffic, jammingTestInput))
        groundTruth = np.concatenate((self.getNormalTrafficGroundTruth(), jammingGroundTruth))
        self.__pbtr = ParametersBasedTestRunner(trainingSample, testInput, groundTruth, self.__nEstimators, self.__contamination, self.__maxSamples)
        result = self.__pbtr.runTest()
        if displayResultMetrics: 
            print(result)
        if displayPlot:
            x,y = self.separateInliersFromOutliers(result.inputData, result.classification)
            Plotter.scatterPlot(x, y, ['Normal Traffic', 'Jamming'], ["b", "r"], 'Normal Traffic and Constant Jamming Concatenated Test', ['Samples', 'RSSI[dBm]'])
    
    #Runs increasing contamination test and analyzes the result metrics (accuracy, precision, recall, f1, confusion matrix)


