import numpy as np

class DataSequence: 

    def __init__(self, yAxis): 
        self.__yAxis = np.array(yAxis)
        self.__xAxis = np.array(range(len(yAxis)))
    
    def getXAxis(self):
        return self.__xAxis
    
    def getYAxis(self):
        return self.__yAxis
    
    
