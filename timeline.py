from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
from numpy.core.numeric import empty_like
import pandas as pd
import warnings
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)

class TimeLine(object):
    def __init__(self, timestps, lbls, hands, title, graph):
        self.timestamps = timestps
        self.labels = lbls
        self.handlers = hands
        self.name = title
        self.title = graph
    
    def plot(self):
        nplots = len(self.timestamps)
        fig, axes = plt.subplots(nrows = nplots, ncols = 1, sharex='all', squeeze=True)
        # (figsize=(8.8, 4), constrained_layout=True)

        # print('Find a way to build an array of arrays of different lengths')
        # maxlen = max([len(timestp) for timestp in self.timestamps])
        # print(maxlen)
        # levels = np.zeros([nplots,maxlen])
        # print(levels)
        levels = np.empty_like(self.timestamps, dtype=object)
        for curr in range(0,nplots):
            # Choose some nice levels
            levels[curr] = np.tile([-5, 5, -3, 3, -1, 1],
                            int(np.ceil(len(self.timestamps[curr])/6)))[:len(self.timestamps[curr])]
        np.ndarray.tolist(levels)

        for i, ax in enumerate(axes.flatten()):
            # Create figure and plot a stem plot with the date
            ax.set(title=None)
            ax.vlines(self.timestamps[i], 0, levels[i], color="tab:red")  # The vertical stems.
            ax.plot(self.timestamps[i], np.zeros_like(self.timestamps[i]), "-o",
                    color="k", markerfacecolor="w")  # Baseline and markers on it.
            
            # annotate lines
            for d, l, r, handler in zip(self.timestamps[i], levels[i], self.labels[i], self.handlers[i]):
                if handler == 'A':
                    ax.annotate(r, xy=(d, l),
                                xytext=(-3, np.sign(l)*3), textcoords="offset points",
                                horizontalalignment="left",
                                verticalalignment="bottom" if l > 0 else "top",
                                color='red')
                else:
                    ax.annotate(r, xy=(d, l),
                                xytext=(-3, np.sign(l)*3), textcoords="offset points",
                                horizontalalignment="left",
                                verticalalignment="bottom" if l > 0 else "top",
                                color='blue')

            # remove y axis and spines
            ax.yaxis.set_visible(False)
            
            # if i != len(axes.flatten())-1:
            #     ax.xaxis.set_visible(False)
            #     ax.spines[["left", "top", "right","bottom"]].set_visible(False)
            # else:
            #     ax.spines[["left", "top", "right"]].set_visible(False)
            #     ax.set_xlabel('[s]')
            ax.spines[["left", "top", "right"]].set_visible(False)
            if i == len(axes.flatten())-1:
                ax.set_xlabel('[s]')
            ax.grid(True,axis="x")

            ax.margins(y=0.15)
            # print(self.name)

        ax3 = fig.add_subplot(111, zorder=-1)
        for _, spine in ax3.spines.items():
            spine.set_visible(False)
        ax3.tick_params(labelleft=False, labelbottom=False, left=False, right=False )
        ax3.get_shared_x_axes().join(ax3,axes[0])
        ax3.grid(axis="x")



        plt.savefig(''.join([self.title,'.png']))
