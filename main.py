from datetime import datetime
import numpy as np
import pandas as pd
from timeline import TimeLine
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

def openfile():
    global filename
    filename = askopenfilename()
    mylabel.config(text=filename)

def generate():
    
    data = pd.read_excel(filename, sheet_name='Sheet1')
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

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()  
ttk.Button(frm, text="Select file", command=lambda: openfile()).grid(column=0,row=0)
ttk.Button(frm, text="Generate timeline", command=lambda: generate()).grid(column=1,row=0)
mylabel = ttk.Label(frm, text="Here you will find the file name when you select it.")
mylabel.grid(columnspan=2, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(columnspan=2,row=2)
root.mainloop()