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
N_ESTIMATORS = 50
MAX_SAMPLES = 1.0
CONTAMINATION = 0.1



#---- CONTAMINATION TEST ----#
START_CONTAMINATION = 0.1
END_CONTAMINATION = 0.2
STEP_SIZE_CONTAMINATION = 0.1



class TestCaseLauncher: 

    def __init__(self): 
        self.__normalTraffic = FileHandler.readAndParseFile(NORMAL_TRAFFIC_FILE, NORMAL_TRAFFIC_SIZE)
        self.__constantJamming = FileHandler.readAndParseFile(CONSTANT_JAMMING_FILE, CONSTANT_JAMMING_SIZE)
        self.__periodicJamming = FileHandler.readAndParseFile(PERIODIC_JAMMING_FILE, PERIODIC_JAMMING_SIZE)
        self.__nEstimators = N_ESTIMATORS
        self.__maxSamples = MAX_SAMPLES
        self.__contamination = CONTAMINATION
        self.__pbtr = None

    def getNormalTrafficGroundTruth(self): 
        return Constants.INLIERS * np.ones(len(self.__normalTraffic))
    def getConstantJammingGroundTruth(self): 
        return Constants.OUTLIERS * np.ones(len(self.__constantJamming))
    def getPeriodicJammingGroundTruth(self): 
        raise Exception('Not implemented')
    
    def separateInliersFromOutliers (self, inputData, classificationResults): 
        x = range(len(inputData))
        normal_x = [x[i] for i in range(len(x)) if classificationResults[i] == 1]
        normal_y = [inputData[i] for i in range(len(inputData)) if classificationResults[i] == 1]
        jamming_x = [x[i] for i in range(len(x)) if classificationResults[i] == -1]
        jamming_y = [inputData[i] for i in range(len(inputData)) if classificationResults[i] == -1]
        return [normal_x, jamming_x], [normal_y, jamming_y]
    
    #Simple normal traffic concatenated with constant jamming test
    def basicNormalConstantConcatenatedTest(self, displayResultMetrics = True, displayPlot = True ): 
        trainingSample = self.__normalTraffic
        testInput = np.concatenate((self.__normalTraffic, self.__constantJamming))
        groundTruth = np.concatenate((self.getNormalTrafficGroundTruth(), self.getConstantJammingGroundTruth()))
        self.__pbtr = ParametersBasedTestRunner(trainingSample, testInput, groundTruth, self.__nEstimators, self.__contamination, self.__maxSamples)
        result = self.__pbtr.runTest()
        if displayResultMetrics: 
            print(result)
        if displayPlot:
            x,y = self.separateInliersFromOutliers(result.inputData, result.classification)
            Plotter.scatterPlot(x, y, ['Normal Traffic', 'Jamming'], ["b", "r"], 'Normal Traffic and Constant Jamming Concatenated Test', ['Samples', 'RSSI[dBm]'])
        

