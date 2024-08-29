

class ResultMetrics: 
    def __init__(self, accuracy, precision, recall, f1, confusionMatrix): 
        self.accuracy = accuracy
        self.precision = precision
        self.recall = recall
        self.f1 = f1
        self.tn, self.fp, self.fn, self.tp = confusionMatrix.ravel()
    
    def __str__(self):
        return f"Accuracy: {self.accuracy}, Precision: {self.precision}, Recall: {self.recall}, F1: {self.f1}, Confusion Matrix: {self.tn, self.fp, self.fn, self.tp}"
    

    