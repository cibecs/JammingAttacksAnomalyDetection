import numpy as np

from AnomalyClassifier import AnomalyClassifier
from FileHandler import FileHandler
from DataSequence import DataSequence
from Plotter import Plotter

from ParametersBasedTestRunner import ParametersBasedTestRunner

N_ESTIMATORS = 100
MAX_SAMPLES = 1
CONTAMINATION = 0.1

def main():

    normalTrafficFile = 'data/normal_channel.txt'
    normalTraffic = FileHandler.readAndParseFile(normalTrafficFile, 1000)

    periodicJammingFile = 'data/periodic_jammer.txt'
    periodicJamming = FileHandler.readAndParseFile(periodicJammingFile, 4000)

    groundTruth = np.ones(len (periodicJamming))

    tr = ParametersBasedTestRunner(normalTraffic, periodicJamming, groundTruth, N_ESTIMATORS, CONTAMINATION, MAX_SAMPLES)

    results = tr.variableContaminationTest(0.01, 0.5, 0.01)

    print(results)







if __name__ == '__main__':
    main()