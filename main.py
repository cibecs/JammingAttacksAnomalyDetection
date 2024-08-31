
from TestCaseLauncher import TestCaseLauncher
from Constants import Constants

#---- CONTAMINATION TEST ----#
START_CONTAMINATION = 0.01
END_CONTAMINATION = 0.5
STEP_SIZE_CONTAMINATION = 0.01

#---- ESTIMATORS TEST ----#
START_ESTIMATORS = 1
END_ESTIMATORS = 150
STEP_SIZE_ESTIMATORS = 1

#---- MAX SAMPLES TEST ----#
START_MAX_SAMPLES = 1
END_MAX_SAMPLES = 1000
STEP_SIZE_MAX_SAMPLES = 1

def main():
    tcl = TestCaseLauncher()
    #tcl.basicNormalJammingConcatenatedTest(Constants.CONSTANT_JAMMING)
    #tcl.increasingMetricTest(Constants.CONSTANT_JAMMING, Constants.CONTAMINATION_ID, START_CONTAMINATION, END_CONTAMINATION, STEP_SIZE_CONTAMINATION)
    #tcl.increasingMetricTest(Constants.CONSTANT_JAMMING, Constants.N_ESTIMATORS_ID ,START_ESTIMATORS, END_ESTIMATORS, STEP_SIZE_ESTIMATORS)
    #tcl.increasingMetricTest(Constants.CONSTANT_JAMMING, Constants.MAX_SAMPLES_ID, START_MAX_SAMPLES, END_MAX_SAMPLES, STEP_SIZE_MAX_SAMPLES, False)
    tcl.groundTruthTest(Constants.PERIODIC_JAMMING)
    #tcl.basicNormalJammingConcatenatedTest(Constants.PERIODIC_JAMMING)

if __name__ == '__main__':
    main()