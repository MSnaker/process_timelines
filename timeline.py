import matplotlib.pyplot as plt
import numpy as np
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
        fig, axes = plt.subplots(nrows = nplots, ncols = 1, sharex='all', figsize=(20/2.54, 10/2.54))

        levels = np.empty_like(self.timestamps, dtype=object)
        for curr in range(0,nplots):
            # Choose some nice levels
            levels[curr] = np.tile([-5, 5, -3, 3, -1, 1],
                            int(np.ceil(len(self.timestamps[curr])/6)))[:len(self.timestamps[curr])]
        np.ndarray.tolist(levels)

        for i, ax in enumerate(axes.flatten()):

            # Create figure and plot a stem plot with the date
            ax.set(title=None)
            ax.vlines(self.timestamps[i], 0, levels[i], linewidth=1, color="k")  # The vertical stems.
            ax.plot(self.timestamps[i], np.zeros_like(self.timestamps[i]), "-o",
                    color="k", markerfacecolor="w", markersize=3, linewidth=1)  # Baseline and markers on it.
            
            # annotate lines
            for d, l, r, handler in zip(self.timestamps[i], levels[i], self.labels[i], self.handlers[i]):
                timestring = ':'.join([str(int(d/60)).zfill(2),str(int(d%60)).zfill(2)])
                if handler == 'A':
                    ax.annotate(timestring + '\n' + r, xy=(d, l),
                                xytext=(-2, np.sign(l)*3), textcoords="offset points",
                                horizontalalignment="left",
                                verticalalignment="bottom" if l > 0 else "top",
                                color='red',
                                fontsize=3)
                else:
                    ax.annotate(timestring + '\n' + r, xy=(d, l),
                                xytext=(-2, np.sign(l)*3), textcoords="offset points",
                                horizontalalignment="left",
                                verticalalignment="bottom" if l > 0 else "top",
                                color='blue',
                                fontsize=3)

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

            ax.margins(y=0.40)
            # print(self.name)

        ax3 = fig.add_subplot(111, zorder=-1)
        for _, spine in ax3.spines.items():
            spine.set_visible(False)
        ax3.tick_params(labelleft=False, labelbottom=False, left=False, right=False )
        ax3.get_shared_x_axes().join(ax3,axes[0])
        ax3.grid(axis="x")

        plt.savefig(''.join([self.title,'.png']), dpi=300)
