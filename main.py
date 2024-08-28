
from AnomalyClassifier import AnomalyClassifier
from FileHandler import FileHandler
from DataSequence import DataSequence
from Plotter import Plotter

def main():
    constantJammingFile = 'data/periodic_jammer.txt'
    jamming = FileHandler.readAndParseFile(constantJammingFile, 10000)
    

    jammingGraph = DataSequence(jamming)

    Plotter.plotGraphs(jammingGraph.getXAxis(), [jammingGraph.getYAxis()], ['Jamming'], ['r'], 'Jamming', ['Time', 'Amplitude'])








if __name__ == '__main__':
    main()