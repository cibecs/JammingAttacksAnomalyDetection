import matplotlib.pyplot as plt
import seaborn as sns

class Plotter: 

    def labelGraph (xLabel, yLabel, graphLabels, graphTitle): 
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.title(graphTitle)
        plt.legend(graphLabels, loc = 'lower right')
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
    
    def scatterPlot (xPoints, yPoints, graphLabels, colors, graphTitle, axisLabels): 
        for i in range(len(xPoints)): 
            plt.scatter(xPoints[i], yPoints[i], color=colors[i], label=graphLabels[i], s=2)
        Plotter.labelGraph(axisLabels[0], axisLabels[1], graphLabels, graphTitle)

    def plotSegmentedGraph(x, y, n, color1, color2, graphTitle, axisLabels, pointLabels):
        plt.scatter(x[:n], y[:n], color=color1, label=pointLabels[0], s=2)

        plt.scatter(x[n:], y[n:], color=color2, label=pointLabels[1], s=2)
        
        # Use the existing labelGraph function to set labels and display
        Plotter.labelGraph(axisLabels[0], axisLabels[1], pointLabels, graphTitle)
    
    def plotConfusionMatrix (matrixValues, graphTitle, axisLabels, classificationLabels): 
        sns.set_theme(font_scale=1.15)
        plt.figure()
        sns.heatmap(matrixValues, annot=True, fmt='.2%', cmap='Blues', xticklabels=classificationLabels[0], yticklabels=classificationLabels[1])
        plt.xlabel(axisLabels[0])
        plt.ylabel(axisLabels[1])
        plt.title(graphTitle)
        plt.show()

