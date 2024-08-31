
class TestResult: 
    def __init__ (self, inputData, n_estimators, contamination, max_samples, classification, resultMetrics): 
        self.inputData = inputData
        self.n_estimators = n_estimators
        self.contamination = contamination
        self.max_samples = max_samples
        self.classification = classification
        self.resultMetrics = resultMetrics
    
    def __str__(self):
        return f"n_estimators: {self.n_estimators}, contamination: {self.contamination}, testing_size: {len(self.classification)} resultMetrics: {self.resultMetrics}"


