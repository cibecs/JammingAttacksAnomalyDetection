import matplotlib.pyplot as plt


class Plotter: 

    def labelGraph (xLabel, yLabel, graphLabels, graphTitle): 
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.title(graphTitle)
        plt.legend(graphLabels)
        plt.show()

    def plotGraphs(x, graphs, graphLabels, colors, graphTitle, axisLabels): 
        for i in range(len(graphs)): 
            plt.plot(x, graphs[i], color=colors[i])
        Plotter.labelGraph(axisLabels[0], axisLabels[1], graphLabels, graphTitle)
    