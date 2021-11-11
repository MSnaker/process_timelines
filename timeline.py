import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class TimeLine(object):
    def __init__(self, timestps, lbls, title, numplts):
        # super(TimeLine, self).__init__(timestps, lbls))
        self.timestamps = timestps
        self.labels = lbls
        self.name = title
        self.numplots = numplts
    
    def plot(self):
        # fig, axs = plt.subplots(figsize=(15, 4*self.numplots), constrained_layout=True,)
        fig, ax = plt.subplots(figsize=(15, 4), constrained_layout=True,)
        _ = ax.set_ylim(-2, 1.75)
        _ = ax.set_xlim(0, max(self.timestamps))
        _ = ax.axhline(0, xmin=0.05, xmax=0.95, c='deeppink', zorder=1)
        
        _ = ax.scatter(self.timestamps, np.zeros(len(self.timestamps)), s=120, c='palevioletred', zorder=2)
        _ = ax.scatter(self.timestamps, np.zeros(len(self.timestamps)), s=30, c='darkmagenta', zorder=3) 
        
        label_offsets = np.zeros(len(self.timestamps))
        label_offsets[::2] = 0.35
        label_offsets[1::2] = -0.7
        for i, (l, d) in enumerate(zip(self.labels, self.timestamps)):
            _ = ax.text(d, label_offsets[i], l, ha='center', fontfamily='serif', fontweight='bold', color='royalblue',fontsize=12)
        
        stems = np.zeros(len(self.timestamps))
        stems[::2] = 0.3
        stems[1::2] = -0.3   
        markerline, stemline, baseline = ax.stem(self.timestamps, stems, use_line_collection=True)
        _ = plt.setp(markerline, marker=',', color='darkmagenta')
        _ = plt.setp(stemline, color='darkmagenta')

        # hide lines around chart
        for spine in ["left", "top", "right", "bottom"]:
            _ = ax.spines[spine].set_visible(False)
        
        # hide tick self.labels
        _ = ax.set_xticks([])
        _ = ax.set_yticks([])
        
        _ = ax.set_title('Process Timeline', fontweight="bold", fontfamily='serif', fontsize=16, 
                        color='royalblue')

        plt.savefig(''.join([self.name,'.png']))

    