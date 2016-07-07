import matplotlib.pyplot as plt
import numpy as np

def plot_results(results, choice):

    fig, ax = plt.subplots()
    bins = np.arange(min(results),max(results),.03)
    
    plt.hist(results,bins,color=(31./255, 119./255, 180./255),linewidth=.4)  # plt.hist passes it's arguments to np.histogram
    #plt.xlabel('probability of winning car')
    
    title = 'distribution of probability of winning car when %s doors' % choice
    plt.title(title)  
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    #ax.yaxis.set_ticks_position(False)
    #ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, pos: ('%.0f')%(y*1e-3)))
    ax.set_ylabel(False)
    ax.yaxis.set_visible(False)
    
    return fig