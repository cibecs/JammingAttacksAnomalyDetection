
from TestCaseLauncher import TestCaseLauncher
from Constants import Constants

from tmp import tmp



#---- MODEL ----#
N_ESTIMATORS = 100
MAX_SAMPLES = 1.0
CONTAMINATION = 0.1

NORMAL_TRAFFIC_SIZE = 100000
CONSTANT_JAMMING_SIZE = 2000
PERIODIC_JAMMING_SIZE = 2000

#---- CONTAMINATION TEST ----#
START_CONTAMINATION = 0.01
END_CONTAMINATION = 0.5
STEP_SIZE_CONTAMINATION = 0.01

#---- ESTIMATORS TEST ----#
START_ESTIMATORS = 1
END_ESTIMATORS = 150
STEP_SIZE_ESTIMATORS = 10

#---- MAX SAMPLES TEST ----#
START_MAX_SAMPLES = 1
END_MAX_SAMPLES = NORMAL_TRAFFIC_SIZE
STEP_SIZE_MAX_SAMPLES = 10



def main():
    tcl = TestCaseLauncher(N_ESTIMATORS, MAX_SAMPLES, CONTAMINATION, NORMAL_TRAFFIC_SIZE, CONSTANT_JAMMING_SIZE, PERIODIC_JAMMING_SIZE)

    # tcl.increasingMetricParameterTest(Constants.PERIODIC_JAMMING, Constants.CONTAMINATION_ID, START_CONTAMINATION, END_CONTAMINATION, STEP_SIZE_CONTAMINATION)
    # tcl.increasingMetricParameterTest(Constants.CONSTANT_JAMMING, Constants.CONTAMINATION_ID, START_CONTAMINATION, END_CONTAMINATION, STEP_SIZE_CONTAMINATION)

    # tcl.increasingMetricParameterTest(Constants.PERIODIC_JAMMING, Constants.N_ESTIMATORS_ID ,START_ESTIMATORS, END_ESTIMATORS, STEP_SIZE_ESTIMATORS)
    # tcl.increasingMetricParameterTest(Constants.CONSTANT_JAMMING, Constants.N_ESTIMATORS_ID ,START_ESTIMATORS, END_ESTIMATORS, STEP_SIZE_ESTIMATORS)

    # tcl.increasingMetricTimeTest(Constants.PERIODIC_JAMMING, Constants.N_ESTIMATORS_ID, START_ESTIMATORS, END_ESTIMATORS, STEP_SIZE_ESTIMATORS)
    # tcl.increasingMetricTimeTest(Constants.CONSTANT_JAMMING, Constants.N_ESTIMATORS_ID, START_ESTIMATORS, END_ESTIMATORS, STEP_SIZE_ESTIMATORS)

    #tcl.groundTruthTest(Constants.CONSTANT_JAMMING)
    tcl.basicNormalJammingConcatenatedTest(Constants.CONSTANT_JAMMING)
    #tcl.groundTruthTest(Constants.PERIODIC_JAMMING)
    tcl.basicNormalJammingConcatenatedTest(Constants.PERIODIC_JAMMING)

    # tcl.increasingMetricParameterTest(Constants.PERIODIC_JAMMING, Constants.MAX_SAMPLES_ID, START_MAX_SAMPLES, END_MAX_SAMPLES, STEP_SIZE_MAX_SAMPLES, False)
    # tcl.increasingMetricParameterTest(Constants.CONSTANT_JAMMING, Constants.MAX_SAMPLES_ID, START_MAX_SAMPLES, END_MAX_SAMPLES, STEP_SIZE_MAX_SAMPLES, False)
    
    # tcl.increasingMetricTimeTest(Constants.PERIODIC_JAMMING, Constants.MAX_SAMPLES_ID, START_MAX_SAMPLES, END_MAX_SAMPLES, STEP_SIZE_MAX_SAMPLES)
    # tcl.increasingMetricTimeTest(Constants.CONSTANT_JAMMING, Constants.MAX_SAMPLES_ID, START_MAX_SAMPLES, END_MAX_SAMPLES, STEP_SIZE_MAX_SAMPLES)

    # #jamming size = 1 to evaluate classification time against a single data point
    # jamming_traffic_size = 1

    # tcl = TestCaseLauncher(N_ESTIMATORS, MAX_SAMPLES, CONTAMINATION, NORMAL_TRAFFIC_SIZE, jamming_traffic_size, jamming_traffic_size)

    # tcl.increasingMetricTimeTest(Constants.PERIODIC_JAMMING, Constants.MAX_SAMPLES_ID, START_MAX_SAMPLES, END_MAX_SAMPLES, STEP_SIZE_MAX_SAMPLES)
    # tcl.increasingMetricTimeTest(Constants.CONSTANT_JAMMING, Constants.MAX_SAMPLES_ID, START_MAX_SAMPLES, END_MAX_SAMPLES, STEP_SIZE_MAX_SAMPLES)



if __name__ == '__main__':
    main()