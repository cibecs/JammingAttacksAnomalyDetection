from AnomalyClassifier import AnomalyClassifier

from Constants import Constants

WINDOW_SIZE = 20

#This class extends the AnomalyClassifier class and implements the majority rule

class MajorityRuleAnomalyClassifier(AnomalyClassifier):
    def __init__(self, trainingSample, n_estimators, contamination, max_samples):
        super().__init__(trainingSample, n_estimators, contamination, max_samples)
        self.__windowSize = WINDOW_SIZE

    def __majorityRule(self, predictions):
        window = []
        for index in range (len(predictions)): 
            if (len(window) == self.__windowSize): 
                window.pop(0)
            window.append(predictions[index])
            if (predictions[index] == Constants.OUTLIERS and window.count(Constants.OUTLIERS) <= self.__windowSize // 2): 
                predictions[index] = Constants.INLIERS
        return predictions
                

    def classify(self, data): 
        predictions = super().classify(data)
        return self.__majorityRule(predictions)