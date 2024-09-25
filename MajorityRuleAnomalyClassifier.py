from AnomalyClassifier import AnomalyClassifier

from Parameters import Parameters


#This class extends the AnomalyClassifier class and implements the majority rule

class MajorityRuleAnomalyClassifier(AnomalyClassifier):
    def __init__(self, trainingSample, n_estimators, contamination, max_samples, window_size):
        super().__init__(trainingSample, n_estimators, contamination, max_samples)
        self.__windowSize = window_size

    def __majorityRule(self, classification):
        window = []
        for index in range (len(classification)): 
            if (len(window) == self.__windowSize): 
                window.pop(0)
            window.append(classification[index])
            if (classification[index] == Parameters.OUTLIERS and window.count(Parameters.OUTLIERS) <= self.__windowSize // 2): 
                classification[index] = Parameters.INLIERS
        return classification
                

    def classify(self, data): 
        classification = super().classify(data)
        return self.__majorityRule(classification)