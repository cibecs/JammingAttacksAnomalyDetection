
from TestCaseLauncher import TestCaseLauncher
from Constants import Constants

#---- MODEL ----#
N_ESTIMATORS = 100
MAX_SAMPLES = 1.0
CONTAMINATION = 0.1
WINDOW_SIZE = 20

NORMAL_TRAFFIC_SIZE = 10000
CONSTANT_JAMMING_SIZE = 1000
PERIODIC_JAMMING_SIZE = 2000

#---- CONTAMINATION TEST ----#
START_CONTAMINATION = 0.01
END_CONTAMINATION = 0.5
STEP_SIZE_CONTAMINATION = 0.1

#---- ESTIMATORS TEST ----#
START_ESTIMATORS = 1
END_ESTIMATORS = 150
STEP_SIZE_ESTIMATORS = 10

#---- MAX SAMPLES TEST ----#
START_MAX_SAMPLES = 1
END_MAX_SAMPLES = NORMAL_TRAFFIC_SIZE
STEP_SIZE_MAX_SAMPLES = 100

#---- TESTING SAMPLES SIZE TEST ----#
START_TESTING_SAMPLES_SIZE = 100
END_TESTING_SAMPLES_SIZE = 10000
STEP_SIZE_TESTING_SAMPLES_SIZE = 100

#---- TRAINING SAMPLES SIZE TEST ----#

START_TRAINING_SAMPLES_SIZE = 100
END_TRAINING_SAMPLES_SIZE = 10000
STEP_SIZE_TRAINING_SAMPLES_SIZE = 100

#---- WINDOW SIZE TEST ----#
START_WINDOW_SIZE = 1
END_WINDOW_SIZE = 100
STEP_SIZE_WINDOW_SIZE = 1


def main():
    tcl = TestCaseLauncher(N_ESTIMATORS, MAX_SAMPLES, CONTAMINATION, NORMAL_TRAFFIC_SIZE, CONSTANT_JAMMING_SIZE, PERIODIC_JAMMING_SIZE, Constants.MAJORITY_RULE_ISOLATION_FOREST, WINDOW_SIZE)
    tcl.increasingMetricParameterTest(Constants.CONSTANT_JAMMING, Constants.WINDOW_SIZE_ID, START_WINDOW_SIZE, END_WINDOW_SIZE, STEP_SIZE_WINDOW_SIZE, True, True)





def runBasicTests(testType,logResults, plotResults, classifierType, windowSize = None):
    tcl = TestCaseLauncher(N_ESTIMATORS, MAX_SAMPLES, CONTAMINATION, NORMAL_TRAFFIC_SIZE, CONSTANT_JAMMING_SIZE, PERIODIC_JAMMING_SIZE, classifierType, windowSize)

    tcl.basicNormalJammingConcatenatedTest(testType, logResults, plotResults)

def runGroundTruthTests(testType):
    tcl = TestCaseLauncher(N_ESTIMATORS, MAX_SAMPLES, CONTAMINATION, NORMAL_TRAFFIC_SIZE, CONSTANT_JAMMING_SIZE, PERIODIC_JAMMING_SIZE)

    tcl.groundTruthTest(testType)

def runMetricsTests(testType, logResults, plotResults):
    tcl = TestCaseLauncher(N_ESTIMATORS, MAX_SAMPLES, CONTAMINATION, NORMAL_TRAFFIC_SIZE, CONSTANT_JAMMING_SIZE, PERIODIC_JAMMING_SIZE)

    tcl.increasingMetricParameterTest(testType, Constants.CONTAMINATION_ID, START_CONTAMINATION, END_CONTAMINATION, STEP_SIZE_CONTAMINATION, logResults, plotResults)
    tcl.increasingMetricParameterTest(testType, Constants.N_ESTIMATORS_ID ,START_ESTIMATORS, END_ESTIMATORS, STEP_SIZE_ESTIMATORS, logResults, plotResults)
    tcl.increasingMetricParameterTest(testType, Constants.MAX_SAMPLES_ID, START_MAX_SAMPLES, END_MAX_SAMPLES, STEP_SIZE_MAX_SAMPLES, logResults, plotResults)

def runTimeTests(testType, logResults, plotResults): 
    tcl = TestCaseLauncher(N_ESTIMATORS, MAX_SAMPLES, CONTAMINATION, NORMAL_TRAFFIC_SIZE, CONSTANT_JAMMING_SIZE, PERIODIC_JAMMING_SIZE)

    tcl.increasingMetricTimeTest(testType, Constants.N_ESTIMATORS_ID, START_ESTIMATORS, END_ESTIMATORS, STEP_SIZE_ESTIMATORS, logResults, plotResults)
    tcl.increasingMetricTimeTest(testType, Constants.CONTAMINATION_ID, START_CONTAMINATION, END_CONTAMINATION, STEP_SIZE_CONTAMINATION, logResults, plotResults)
    tcl.increasingMetricTimeTest(testType, Constants.MAX_SAMPLES_ID, START_MAX_SAMPLES, END_MAX_SAMPLES, STEP_SIZE_MAX_SAMPLES, logResults, plotResults)
    tcl.increasingMetricTimeTest(testType, Constants.TESTING_SAMPLES_SIZE_ID, START_TESTING_SAMPLES_SIZE, END_TESTING_SAMPLES_SIZE, STEP_SIZE_TESTING_SAMPLES_SIZE, logResults, plotResults)
    tcl.increasingMetricTimeTest(testType, Constants.TRAINING_SAMPLES_SIZE_ID, START_TRAINING_SAMPLES_SIZE, END_TRAINING_SAMPLES_SIZE, STEP_SIZE_TRAINING_SAMPLES_SIZE, logResults, plotResults)

    #jamming_size = 1 to evaluate classification time against a single data point
    jamming_traffic_size = 1

    tcl = TestCaseLauncher(N_ESTIMATORS, MAX_SAMPLES, CONTAMINATION, NORMAL_TRAFFIC_SIZE, jamming_traffic_size, jamming_traffic_size)

    tcl.increasingMetricTimeTest(testType, Constants.MAX_SAMPLES_ID, START_MAX_SAMPLES, END_MAX_SAMPLES, STEP_SIZE_MAX_SAMPLES, logResults, plotResults)

   


def runTestsInPaperOrder(): 
    tcl = TestCaseLauncher(N_ESTIMATORS, MAX_SAMPLES, CONTAMINATION, NORMAL_TRAFFIC_SIZE, CONSTANT_JAMMING_SIZE, PERIODIC_JAMMING_SIZE)

    tcl.increasingMetricParameterTest(Constants.PERIODIC_JAMMING, Constants.CONTAMINATION_ID, START_CONTAMINATION, END_CONTAMINATION, STEP_SIZE_CONTAMINATION)
    tcl.increasingMetricParameterTest(Constants.CONSTANT_JAMMING, Constants.CONTAMINATION_ID, START_CONTAMINATION, END_CONTAMINATION, STEP_SIZE_CONTAMINATION)

    tcl.increasingMetricParameterTest(Constants.PERIODIC_JAMMING, Constants.N_ESTIMATORS_ID ,START_ESTIMATORS, END_ESTIMATORS, STEP_SIZE_ESTIMATORS)
    tcl.increasingMetricParameterTest(Constants.CONSTANT_JAMMING, Constants.N_ESTIMATORS_ID ,START_ESTIMATORS, END_ESTIMATORS, STEP_SIZE_ESTIMATORS)

    tcl.increasingMetricTimeTest(Constants.PERIODIC_JAMMING, Constants.N_ESTIMATORS_ID, START_ESTIMATORS, END_ESTIMATORS, STEP_SIZE_ESTIMATORS)
    tcl.increasingMetricTimeTest(Constants.CONSTANT_JAMMING, Constants.N_ESTIMATORS_ID, START_ESTIMATORS, END_ESTIMATORS, STEP_SIZE_ESTIMATORS)

    tcl.groundTruthTest(Constants.CONSTANT_JAMMING)
    tcl.basicNormalJammingConcatenatedTest(Constants.CONSTANT_JAMMING)
    tcl.groundTruthTest(Constants.PERIODIC_JAMMING)
    tcl.basicNormalJammingConcatenatedTest(Constants.PERIODIC_JAMMING)

    tcl.increasingMetricParameterTest(Constants.PERIODIC_JAMMING, Constants.MAX_SAMPLES_ID, START_MAX_SAMPLES, END_MAX_SAMPLES, STEP_SIZE_MAX_SAMPLES, False)
    tcl.increasingMetricParameterTest(Constants.CONSTANT_JAMMING, Constants.MAX_SAMPLES_ID, START_MAX_SAMPLES, END_MAX_SAMPLES, STEP_SIZE_MAX_SAMPLES, False)
    
    tcl.increasingMetricTimeTest(Constants.PERIODIC_JAMMING, Constants.MAX_SAMPLES_ID, START_MAX_SAMPLES, END_MAX_SAMPLES, STEP_SIZE_MAX_SAMPLES)
    tcl.increasingMetricTimeTest(Constants.CONSTANT_JAMMING, Constants.MAX_SAMPLES_ID, START_MAX_SAMPLES, END_MAX_SAMPLES, STEP_SIZE_MAX_SAMPLES)

    #jamming size = 1 to evaluate classification time against a single data point
    jamming_traffic_size = 1

    tcl = TestCaseLauncher(N_ESTIMATORS, MAX_SAMPLES, CONTAMINATION, NORMAL_TRAFFIC_SIZE, jamming_traffic_size, jamming_traffic_size)

    tcl.increasingMetricTimeTest(Constants.PERIODIC_JAMMING, Constants.MAX_SAMPLES_ID, START_MAX_SAMPLES, END_MAX_SAMPLES, STEP_SIZE_MAX_SAMPLES)
    tcl.increasingMetricTimeTest(Constants.CONSTANT_JAMMING, Constants.MAX_SAMPLES_ID, START_MAX_SAMPLES, END_MAX_SAMPLES, STEP_SIZE_MAX_SAMPLES)

if __name__ == '__main__':
    main()