import numpy as np

from Constants import Constants
from TestRunner import TestRunner
from FileHandler import FileHandler
from Plotter import Plotter
from TestResult import TestResult

#---- DATA ----#

NORMAL_TRAFFIC_FILE = 'data/normal_traffic.txt'

CONSTANT_JAMMING_FILE = 'data/constant_jammer.txt'

PERIODIC_JAMMING_FILE = 'data/periodic_jammer.txt'



#Wrapper class for TestRunner
#This class launches the test cases by setting the parameters and plots the results
class TestCaseLauncher: 

    def __init__(self, n_estimators, max_samples, contamination, normal_traffic_size, constant_jamming_size, periodic_jamming_size, classifierType = Constants.STANDARD_ISOLATION_FOREST, windowSize = None): 
        self.__normalTraffic = FileHandler.readAndParseFile(NORMAL_TRAFFIC_FILE, normal_traffic_size)
        self.__constantJamming = FileHandler.readAndParseFile(CONSTANT_JAMMING_FILE, constant_jamming_size)
        self.__periodicJamming = FileHandler.readAndParseFile(PERIODIC_JAMMING_FILE, periodic_jamming_size)
        self.__nEstimators = n_estimators
        self.__maxSamples = max_samples
        self.__contamination = contamination
        self.__tr = None
        self.__classifierType = classifierType
        self.__windowSize = windowSize
    
    #returns the ground truth for the various types of data
    def __getNormalTrafficGroundTruth(self): 
        return Constants.INLIERS * np.ones(len(self.__normalTraffic))
    def __getConstantJammingGroundTruth(self): 
        return Constants.OUTLIERS * np.ones(len(self.__constantJamming))
    def __getPeriodicJammingGroundTruth(self): 
        start_offset = 293
        pause = 557
        jamming_time = 372
        
        samplesNumber = len(self.__periodicJamming)

        ground_truth = Constants.INLIERS * np.ones(samplesNumber)

        for i in range (0, int(samplesNumber/(jamming_time + pause)) + 1): 
            jamming_start = start_offset + i *(jamming_time + pause)
            jamming_end = jamming_start + jamming_time
            if (jamming_start >= samplesNumber):
                break
            if (jamming_end >= samplesNumber):
                jamming_end = samplesNumber
            ground_truth[jamming_start:jamming_end] = Constants.OUTLIERS
        return ground_truth
    
    def __getJammingSignalAndGroundTruth(self, signalType):
        if signalType == Constants.CONSTANT_JAMMING: 
            return self.__constantJamming, self.__getConstantJammingGroundTruth()
        elif signalType == Constants.PERIODIC_JAMMING: 
            return self.__periodicJamming, self.__getPeriodicJammingGroundTruth()
        else: 
            raise Exception('Invalid signal type')
    
    #Prepares the model for the test. Test input is the normal traffic concatenated with the jamming signal
    def __prepareModel(self, jammingType):
        trainingSample = self.__normalTraffic
        jammingTestInput, jammingGroundTruth = self.__getJammingSignalAndGroundTruth(jammingType)
        testInput = np.concatenate((trainingSample, jammingTestInput))
        groundTruth = np.concatenate((self.__getNormalTrafficGroundTruth(), jammingGroundTruth))
        self.__tr = TestRunner(trainingSample, testInput, groundTruth, self.__nEstimators, self.__contamination, self.__maxSamples, self.__classifierType, self.__windowSize)

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
        
    def __plotTime (self, x, results, labels, colors, title, axisLabels): 
            trainingTime = [result.trainingTime for result in results]
            classificationTime = [result.classificationTime for result in results]
            Plotter.plotInSameGraph(x, [trainingTime], [labels[0]], colors[0], title + labels[0], axisLabels)
            Plotter.plotInSameGraph(x, [classificationTime], [labels[1]], colors[1], title + labels[1], axisLabels)

    #Simple normal traffic concatenated with constant jamming test
    def basicNormalJammingConcatenatedTest(self, jammingType, displayResultMetrics = True, displayPlot = True ): 
        self.__prepareModel(jammingType)
        result = self.__tr.runTest()
        if displayResultMetrics: 
            print(result)
        if displayPlot:
            self.__plotInliersOutliers(result, ['Normal Traffic', 'Jamming Signal'], ['b', 'r'], 'Model classification of Normal Traffic concatenated with Jamming Signal', ['Data Point', 'RSS[dBm]'])

    #Runs tests where a parameter is increased in a range
    def increasingMetricParameterTest (self, jammingType, parameter_id, startValue, endValue, stepSize, displayResultMetrics = True, displayPlot = True):
        self.__prepareModel(jammingType)
        results = self.__tr.increasingParameterTest(startValue, endValue, stepSize, parameter_id)
        if displayResultMetrics: 
            for result in results: 
                print(result)
        if displayPlot:
            x = np.arange(startValue, endValue, stepSize)
            self.__plotMetrics(x, results, ['Accuracy', 'Precision', 'Recall', 'F1'], ['b', 'r', 'g', 'm'], 'Impact of ' + parameter_id + ' variation on performance metrics', [parameter_id, 'Metric Value'])
    
    def groundTruthTest (self, jammingType): 
        signal, groundTruth = self.__getJammingSignalAndGroundTruth(jammingType)
        r = TestResult (signal, 0, 0, 0, groundTruth, None)
        self.__plotInliersOutliers(r, ['Normal Traffic', 'Jamming Signal'], ['b', 'r'], 'Ground truth definition', ['Data Point', 'RSS[dBm]'])

    #time test with increasing metric value
    def increasingMetricTimeTest(self, jammingType, parameter_id, startValue, endValue, stepSize, displayResultMetrics = True, displayPlot = True): 
        self.__prepareModel(jammingType)
        results = self.__tr.increasingTimeTest(startValue, endValue, stepSize, parameter_id)
        if displayResultMetrics: 
            for result in results: 
                print(result)
            averageTrainingTime = np.mean([result.trainingTime for result in results])
            averageClassificationTime = np.mean([result.classificationTime for result in results])
            print(f"Average training time: {averageTrainingTime}ms")
            print(f"Average classification time: {averageClassificationTime}ms")
        if displayPlot:
            x = np.arange(startValue, endValue, stepSize)
            self.__plotTime(x, results, ['Training Time', 'Classification Time'], ['b', 'r'], 'Impact of ' + parameter_id + ' variation on ', [parameter_id, 'Time[ms]'])

            
