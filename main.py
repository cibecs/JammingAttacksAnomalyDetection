
from AnomalyClassifier import AnomalyClassifier
from FileHandler import FileHandler
from DataSequence import DataSequence
from Plotter import Plotter

def main():
    constantJammingFile = 'data/constant_jammer.txt'
    jamming = FileHandler.readAndParseFile(constantJammingFile, 1000)

    normalTrafficFile = 'data/normal_channel.txt'
    normalTraffic = FileHandler.readAndParseFile(normalTrafficFile, 1000)
    
    periodicJammingFile = 'data/periodic_jammer.txt'
    periodicJamming = FileHandler.readAndParseFile(periodicJammingFile, 1000)

    jammingGraph = DataSequence(jamming)
    normalTrafficGraph = DataSequence(normalTraffic)
    periodicJammingGraph = DataSequence(periodicJamming)




    Plotter.plotSideToSide([jammingGraph.getXAxis(), normalTrafficGraph.getXAxis(), periodicJammingGraph.getXAxis()], 
                           [[jammingGraph.getYAxis(), normalTrafficGraph.getYAxis()], [normalTrafficGraph.getYAxis()], [periodicJammingGraph.getYAxis(), normalTrafficGraph.getYAxis()]], 
                           [["constant jamming", "normal traffic"], ["normal traffic"], ["periodic jamming", "normal traffic"]], 
                           [['r', 'b'], ['b'], ['g', 'b']],
                           ["Constant Jamming vs Normal Traffic", "Normal Traffic", "Periodic Jamming vs Normal Traffic"], 
                           [["Time1", "Amplitude1"], ["Time2", "Amplitude2"], ["Time3", "Amplitude3"]])





if __name__ == '__main__':
    main()