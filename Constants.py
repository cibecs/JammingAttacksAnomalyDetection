class Constants: 
    #---- MODEL ----#
    N_ESTIMATORS = 100
    MAX_SAMPLES = 1.0
    CONTAMINATION = 0.1
    WINDOW_SIZE = 20

    NORMAL_TRAFFIC_SIZE = 20000
    CONSTANT_JAMMING_SIZE = 2000
    PERIODIC_JAMMING_SIZE = 2000

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
    END_MAX_SAMPLES = NORMAL_TRAFFIC_SIZE
    STEP_SIZE_MAX_SAMPLES = 500

    #---- TESTING SAMPLES SIZE TEST ----#
    START_TESTING_SAMPLES_SIZE = 100
    END_TESTING_SAMPLES_SIZE = 1000
    STEP_SIZE_TESTING_SAMPLES_SIZE = 100

    #---- TRAINING SAMPLES SIZE TEST ----#

    START_TRAINING_SAMPLES_SIZE = 100
    END_TRAINING_SAMPLES_SIZE = 1000
    STEP_SIZE_TRAINING_SAMPLES_SIZE = 100

    #---- WINDOW SIZE TEST ----#
    START_WINDOW_SIZE = 1
    END_WINDOW_SIZE = 100
    STEP_SIZE_WINDOW_SIZE = 10

    #---- MODEL LABELING ----#
    INLIERS = 1
    OUTLIERS = -1

    #---- JAMMING SIGNALS ----#
    CONSTANT_JAMMING = 1
    PERIODIC_JAMMING = 2

    #---- TESTED PARAMETERS ----#
    N_ESTIMATORS_ID = "n_estimators"
    CONTAMINATION_ID = "contamination"
    MAX_SAMPLES_ID = "max_samples"
    TESTING_SAMPLES_SIZE_ID = "testing_samples_size"
    TRAINING_SAMPLES_SIZE_ID = "training_samples_size"
    WINDOW_SIZE_ID = "window_size"

    #---- CLASSIFIER TYPES ----#
    STANDARD_ISOLATION_FOREST = 'Standard Isolation Forest'
    MAJORITY_RULE_ISOLATION_FOREST = 'Majority Rule Isolation Forest'
