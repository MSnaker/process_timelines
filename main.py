from datetime import datetime
import numpy as np
import pandas as pd
from timeline import TimeLine
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
file_name = askopenfilename()
data = pd.read_excel(file_name, sheet_name='Sheet1')

l=0
datatimes,datalabels,datahandlers,datatitle = [],[],[],[]
while(l<len(data.columns)):

    # print('Numero ',str(int(l/3+1)))
    times,labels,handlers,title = [],[],[],[]
    for i, element in enumerate(data[data.columns[l]]):
        if not np.isnan(element):
            times.append(element)
            labels.append(data[data.columns[l+1]][i])
            handlers.append(data[data.columns[l+2]][i])
    
    datatimes.append(times)
    datalabels.append(labels)
    datahandlers.append(handlers)
    l+=3

for i in range(0,len(datatimes)):
    datatitle.append(''.join(["numero",str(int(i))]))

tl = TimeLine(datatimes,datalabels,datahandlers,datatitle, graph=datetime.now().strftime("%Y%m%d_%H%M%S") )
tl.plot()

