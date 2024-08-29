import matplotlib.pyplot as plt


class Plotter: 

    def labelGraph (xLabel, yLabel, graphLabels, graphTitle): 
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.title(graphTitle)
        plt.legend(graphLabels)
        plt.show()

    def plotInSameGraph(x, graphs, graphLabels, colors, graphTitle, axisLabels): 
        for i in range(len(graphs)): 
            plt.plot(x, graphs[i], color=colors[i])
        Plotter.labelGraph(axisLabels[0], axisLabels[1], graphLabels, graphTitle)
    

    #plots side by side graphs containing multiple functions inside
    def plotSideToSide (xAxes, graphs, graphLabels, colors, graphTitle, axesLabels): 
        fig, axs = plt.subplots(1,len(graphs)) 
        for i in range (len(graphs)):
            for j in range (len(graphs[i])): 
                axs[i].plot(xAxes[i], graphs[i][j], color=colors[i][j], label = graphLabels[i][j])

            axs[i].set_xlabel(axesLabels[i][0])
            axs[i].set_ylabel(axesLabels[i][1])
            axs[i].set_title(graphTitle[i])
            axs[i].legend()
        plt.tight_layout()
        plt.show()
    
          

