from TestCaseLauncher import TestCaseLauncher
from Parameters import Parameters
from Plotter import Plotter


def main():
    runTestsInPaperOrder(Parameters.STANDARD_ISOLATION_FOREST)


def runTestsInPaperOrder(classifierType, windowSize=None):
    tcl = TestCaseLauncher(Parameters.N_ESTIMATORS, Parameters.MAX_SAMPLES, Parameters.CONTAMINATION, Parameters.NORMAL_TRAFFIC_SIZE, Parameters.CONSTANT_JAMMING_SIZE, Parameters.PERIODIC_JAMMING_SIZE, classifierType, windowSize)

    #tcl.inputTest(Parameters.CONSTANT_JAMMING)

    #tcl.increasingMetricParameterTest(Parameters.CONSTANT_JAMMING, Parameters.N_ESTIMATORS_ID, Parameters.START_ESTIMATORS, Parameters.END_ESTIMATORS, Parameters.STEP_SIZE_ESTIMATORS, True, True)
    #tcl.increasingMetricTimeTest(Parameters.CONSTANT_JAMMING, Parameters.N_ESTIMATORS_ID, Parameters.START_ESTIMATORS, Parameters.END_ESTIMATORS, Parameters.STEP_SIZE_ESTIMATORS, True, True)

    #tcl.increasingMetricParameterTest(Parameters.CONSTANT_JAMMING, Parameters.MAX_SAMPLES_ID, Parameters.START_MAX_SAMPLES, Parameters.END_MAX_SAMPLES, Parameters.STEP_SIZE_MAX_SAMPLES, True, True)
    #tcl.increasingMetricTimeTest(Parameters.CONSTANT_JAMMING, Parameters.MAX_SAMPLES_ID, Parameters.START_MAX_SAMPLES, Parameters.END_MAX_SAMPLES, Parameters.STEP_SIZE_MAX_SAMPLES, True, True)

    #tcl.increasingMetricParameterTest(Parameters.CONSTANT_JAMMING, Parameters.CONTAMINATION_ID, Parameters.START_CONTAMINATION, Parameters.END_CONTAMINATION, Parameters.STEP_SIZE_CONTAMINATION, True, True)
    #tcl.increasingMetricTimeTest(Parameters.CONSTANT_JAMMING, Parameters.CONTAMINATION_ID, Parameters.START_CONTAMINATION, Parameters.END_CONTAMINATION, Parameters.STEP_SIZE_CONTAMINATION, True, True)


    #tcl.basicNormalJammingConcatenatedTest(Parameters.CONSTANT_JAMMING, True, False)
    Parameters.N_ESTIMATORS = 15
    Parameters.MAX_SAMPLES = 10
    Parameters.CONTAMINATION = 0.09

    tcl = TestCaseLauncher(Parameters.N_ESTIMATORS, Parameters.MAX_SAMPLES, Parameters.CONTAMINATION, Parameters.NORMAL_TRAFFIC_SIZE, Parameters.CONSTANT_JAMMING_SIZE, Parameters.PERIODIC_JAMMING_SIZE, classifierType, windowSize)

    #tcl.basicNormalJammingConcatenatedTest(Parameters.CONSTANT_JAMMING, True, True)

    classifierType = Parameters.MAJORITY_RULE_ISOLATION_FOREST
    windowSize = Parameters.WINDOW_SIZE

    tcl = TestCaseLauncher(Parameters.N_ESTIMATORS, Parameters.MAX_SAMPLES, Parameters.CONTAMINATION, Parameters.NORMAL_TRAFFIC_SIZE, Parameters.CONSTANT_JAMMING_SIZE, Parameters.PERIODIC_JAMMING_SIZE, classifierType, windowSize)

    #tcl.increasingMetricParameterTest(Parameters.CONSTANT_JAMMING, Parameters.WINDOW_SIZE_ID, Parameters.START_WINDOW_SIZE, Parameters.END_WINDOW_SIZE, Parameters.STEP_SIZE_WINDOW_SIZE, True, True)

    #tcl.basicNormalJammingConcatenatedTest(Parameters.CONSTANT_JAMMING, True, True)
    #tcl.basicNormalJammingConcatenatedTest(Parameters.PERIODIC_JAMMING, True, True)
    
    #tcl.compareModels(Parameters.CONSTANT_JAMMING, Parameters.TESTING_SAMPLES_SIZE_ID, Parameters.START_TESTING_SAMPLES_SIZE, Parameters.END_TESTING_SAMPLES_SIZE, Parameters.STEP_SIZE_TESTING_SAMPLES_SIZE, [Parameters.STANDARD_ISOLATION_FOREST, Parameters.MAJORITY_RULE_ISOLATION_FOREST], ['r', 'b'], True, True)

    Parameters.NORMAL_TRAFFIC_SIZE = 10000
    Parameters.CONSTANT_JAMMING_SIZE = 10000
    Parameters.PERIODIC_JAMMING_SIZE = 10000
    
    tcl = TestCaseLauncher(Parameters.N_ESTIMATORS, Parameters.MAX_SAMPLES, Parameters.CONTAMINATION, Parameters.NORMAL_TRAFFIC_SIZE, Parameters.CONSTANT_JAMMING_SIZE, Parameters.PERIODIC_JAMMING_SIZE, classifierType, windowSize)

    #tcl.basicOnlyJammingTest(Parameters.CONSTANT_JAMMING, True, True)
    #tcl.basicOnlyJammingTest(Parameters.PERIODIC_JAMMING, True, True)    
    #tcl.basicOnlyNormalTrafficTest(True, True)

    Parameters.NORMAL_TRAFFIC_SIZE = 20000
    Parameters.CONSTANT_JAMMING_SIZE = 2000

    tuned_IF = [[1997, 3], [1565, 18435]]
    standard_IF = [[2000, 0], [1993, 18007]]
    majorityRule_IF = [[1982,18],[27, 19973]]

    plotConfusionMatrix(standard_IF, 'Standard Isolation Forest')
    plotConfusionMatrix(tuned_IF, 'Tuned Isolation Forest')
    plotConfusionMatrix(majorityRule_IF, 'Majority Rule Isolation Forest')
    

def plotConfusionMatrix (matrix, title):
    axisLabels = ['Predicted Class', 'True Class']
    classificationLabels = [['Jamming','Normal Traffic'], ['Jamming', 'Normal Traffic']]
    Plotter.plotConfusionMatrix(getPercentagesMatrix(matrix), title, axisLabels, classificationLabels)

def getPercentagesMatrix(confusion_matrix):
    total_tp = confusion_matrix[0][0] + confusion_matrix[0][1]  # Total for 'Jamming'
    total_fp = confusion_matrix[1][0] + confusion_matrix[1][1]  # Total for 'Normal Traffic'
    
    percentages_matrix = [[(confusion_matrix[0][0] / total_tp),(confusion_matrix[0][1] / total_tp)],[(confusion_matrix[1][0] / total_fp),(confusion_matrix[1][1] / total_fp)]]
    
    return percentages_matrix

if __name__ == '__main__':
    main()
