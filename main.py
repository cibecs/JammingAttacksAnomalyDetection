import numpy as np

from AnomalyClassifier import AnomalyClassifier
from FileHandler import FileHandler
from DataSequence import DataSequence
from Plotter import Plotter

from ParametersBasedTestRunner import ParametersBasedTestRunner

from Constants import Constants

N_ESTIMATORS = 50
MAX_SAMPLES = 1.0
CONTAMINATION = 0.1

def main():

    normalTrafficFile = 'data/normal_channel.txt'
    normalTraffic = FileHandler.readAndParseFile(normalTrafficFile, 10000)

    constantJammingFilename = 'data/constant_jammer.txt'
    constantJamming = FileHandler.readAndParseFile(constantJammingFilename, 10000)

    

    testInput = np.concatenate((normalTraffic, constantJamming))

    groundTruth = np.concatenate((Constants.INLIERS * np.ones(len(normalTraffic)), Constants.OUTLIERS * np.ones(len(constantJamming))))

    tr = ParametersBasedTestRunner(normalTraffic[:2000], testInput, groundTruth, N_ESTIMATORS, CONTAMINATION, MAX_SAMPLES)

    results = tr.variableContaminationTest(0.1, 0.5, 0.1)

    for r in results: 
        print(r)







if __name__ == '__main__':
    main()