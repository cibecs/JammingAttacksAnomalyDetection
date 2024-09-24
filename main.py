from TestCaseLauncher import TestCaseLauncher
from Constants import Constants


def main():
    runTestsInPaperOrder(Constants.STANDARD_ISOLATION_FOREST)

def runBasicTests(testType, logResults, plotResults, classifierType, windowSize=None):
    tcl = TestCaseLauncher(Constants.N_ESTIMATORS, Constants.MAX_SAMPLES, Constants.CONTAMINATION, Constants.NORMAL_TRAFFIC_SIZE, Constants.CONSTANT_JAMMING_SIZE, Constants.PERIODIC_JAMMING_SIZE, classifierType, windowSize)
    tcl.basicNormalJammingConcatenatedTest(testType, logResults, plotResults)


def runGroundTruthTests(testType, classifierType, windowSize=None):
    tcl = TestCaseLauncher(Constants.N_ESTIMATORS, Constants.MAX_SAMPLES, Constants.CONTAMINATION, Constants.NORMAL_TRAFFIC_SIZE, Constants.CONSTANT_JAMMING_SIZE, Constants.PERIODIC_JAMMING_SIZE, classifierType, windowSize)
    tcl.groundTruthTest(testType)


def runMetricsTests(testType, logResults, plotResults, classifierType, windowSize=None):
    tcl = TestCaseLauncher(Constants.N_ESTIMATORS, Constants.MAX_SAMPLES, Constants.CONTAMINATION, Constants.NORMAL_TRAFFIC_SIZE, Constants.CONSTANT_JAMMING_SIZE, Constants.PERIODIC_JAMMING_SIZE, classifierType, windowSize)
    tcl.increasingMetricParameterTest(testType, Constants.CONTAMINATION_ID, Constants.START_CONTAMINATION, Constants.END_CONTAMINATION, Constants.STEP_SIZE_CONTAMINATION, logResults, plotResults)
    tcl.increasingMetricParameterTest(testType, Constants.N_ESTIMATORS_ID, Constants.START_ESTIMATORS, Constants.END_ESTIMATORS, Constants.STEP_SIZE_ESTIMATORS, logResults, plotResults)
    tcl.increasingMetricParameterTest(testType, Constants.MAX_SAMPLES_ID, Constants.START_MAX_SAMPLES, Constants.END_MAX_SAMPLES, Constants.STEP_SIZE_MAX_SAMPLES, logResults, plotResults)
    tcl.increasingMetricParameterTest(testType, Constants.WINDOW_SIZE_ID, Constants.START_WINDOW_SIZE, Constants.END_WINDOW_SIZE, Constants.STEP_SIZE_WINDOW_SIZE, logResults, plotResults)


def runTimeTests(testType, logResults, plotResults, classifierType, windowSize=None):
    tcl = TestCaseLauncher(Constants.N_ESTIMATORS, Constants.MAX_SAMPLES, Constants.CONTAMINATION, Constants.NORMAL_TRAFFIC_SIZE, Constants.CONSTANT_JAMMING_SIZE, Constants.PERIODIC_JAMMING_SIZE, classifierType, windowSize)
    tcl.increasingMetricTimeTest(testType, Constants.N_ESTIMATORS_ID, Constants.START_ESTIMATORS, Constants.END_ESTIMATORS, Constants.STEP_SIZE_ESTIMATORS, logResults, plotResults)
    tcl.increasingMetricTimeTest(testType, Constants.CONTAMINATION_ID, Constants.START_CONTAMINATION, Constants.END_CONTAMINATION, Constants.STEP_SIZE_CONTAMINATION, logResults, plotResults)
    tcl.increasingMetricTimeTest(testType, Constants.MAX_SAMPLES_ID, Constants.START_MAX_SAMPLES, Constants.END_MAX_SAMPLES, Constants.STEP_SIZE_MAX_SAMPLES, logResults, plotResults)
    tcl.increasingMetricTimeTest(testType, Constants.TESTING_SAMPLES_SIZE_ID, Constants.START_TESTING_SAMPLES_SIZE, Constants.END_TESTING_SAMPLES_SIZE, Constants.STEP_SIZE_TESTING_SAMPLES_SIZE, logResults, plotResults)
    tcl.increasingMetricTimeTest(testType, Constants.TRAINING_SAMPLES_SIZE_ID, Constants.START_TRAINING_SAMPLES_SIZE, Constants.END_TRAINING_SAMPLES_SIZE, Constants.STEP_SIZE_TRAINING_SAMPLES_SIZE, logResults, plotResults)

    # jamming_size = 1 to evaluate classification time against a single data point
    jamming_traffic_size = 1

    tcl = TestCaseLauncher(Constants.N_ESTIMATORS, Constants.MAX_SAMPLES, Constants.CONTAMINATION, Constants.NORMAL_TRAFFIC_SIZE, jamming_traffic_size, jamming_traffic_size, classifierType, windowSize)
    tcl.increasingMetricTimeTest(testType, Constants.MAX_SAMPLES_ID, Constants.START_MAX_SAMPLES, Constants.END_MAX_SAMPLES, Constants.STEP_SIZE_MAX_SAMPLES, logResults, plotResults)


def runTestsInPaperOrder(classifierType, windowSize=None):
    tcl = TestCaseLauncher(Constants.N_ESTIMATORS, Constants.MAX_SAMPLES, Constants.CONTAMINATION, Constants.NORMAL_TRAFFIC_SIZE, Constants.CONSTANT_JAMMING_SIZE, Constants.PERIODIC_JAMMING_SIZE, classifierType, windowSize)

    tcl.inputTest(Constants.CONSTANT_JAMMING)


    #tcl.increasingMetricParameterTest(Constants.CONSTANT_JAMMING, Constants.CONTAMINATION_ID, Constants.START_CONTAMINATION, Constants.END_CONTAMINATION, Constants.STEP_SIZE_CONTAMINATION, True, True)

if __name__ == '__main__':
    main()
