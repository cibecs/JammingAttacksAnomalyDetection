import numpy as np

from AnomalyClassifier import AnomalyClassifier
from FileHandler import FileHandler
from Plotter import Plotter

from ParametersBasedTestRunner import ParametersBasedTestRunner

from Constants import Constants

N_ESTIMATORS = 50
MAX_SAMPLES = 1.0
CONTAMINATION = 0.08

START_CONTAMINATION = 0.1
END_CONTAMINATION = 0.2
STEP_SIZE_CONTAMINATION = 0.1

def main():

    normalTrafficFile = 'data/normal_channel.txt'
    normalTraffic = FileHandler.readAndParseFile(normalTrafficFile, 2000)

    constantJammingFilename = 'data/constant_jammer.txt'
    constantJamming = FileHandler.readAndParseFile(constantJammingFilename, 2000)

    

    testInput = np.concatenate((normalTraffic, constantJamming))

    groundTruth = np.concatenate((Constants.INLIERS * np.ones(len(normalTraffic)), Constants.OUTLIERS * np.ones(len(constantJamming))))

    tr = ParametersBasedTestRunner(normalTraffic, testInput, groundTruth, N_ESTIMATORS, CONTAMINATION, MAX_SAMPLES)

    results = tr.variableContaminationTest(START_CONTAMINATION, END_CONTAMINATION, STEP_SIZE_CONTAMINATION)

            # Separate the data based on predictions

   

    for r in results: 
        print(r)
        y = r.inputData
        x = range(len(y))
        predictions = r.classification
        

        normal_x = [x[i] for i in range(len(x)) if predictions[i] == 1]
        normal_y = [y[i] for i in range(len(y)) if predictions[i] == 1]
        jamming_x = [x[i] for i in range(len(x)) if predictions[i] == -1]
        jamming_y = [y[i] for i in range(len(y)) if predictions[i] == -1]

        Plotter.scatterPlot([normal_x, jamming_x], [normal_y, jamming_y], ['Normal Traffic', 'Jamming'], ['blue', 'red'], 'Anomaly Detection', ['Time', 'Amplitude'])







if __name__ == '__main__':
    main()