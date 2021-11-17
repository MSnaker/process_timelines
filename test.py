from numpy.core.numeric import empty_like
import pandas as pd
import numpy as np
from timeline import TimeLine
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

def openfile():
    global filename
    filename = askopenfilename()

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()  
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1,row=0)
ttk.Button(frm, text="Get file", command=lambda: openfile()).grid(column=1,rowspan=2)
root.mainloop()


# file_name = ''.join(['./file/',filename])
data = pd.read_excel(filename, sheet_name='Sheet1')

print(data)


# tl = TimeLine(data["timestamps"],data["caption"], "titolo")
# print(tl.timestamps, '\n', tl.labels)

# tl.plot()

# tatas  = [[[],[]],[[],[]]]
# tatas = np.zeros(10)
# print(len(tatas))

# levels = np.tile([-5, 5, -3, 3, -1, 1],
#                 int(np.ceil(len(tatas)/6)))[:len(tatas)]
# print(np.tile([-5, 5, -3, 3, -1, 1],
#                 int(np.ceil(len(tatas)/6))))

# timestampstest = [[0,2,3,4,5,6],[5,4,3,2],[1,4,7,10,13]]
# levels = np.empty_like(timestampstest, dtype=object)
# for curr in range(0,len(timestampstest)):
#     # Choose some nice levels
#     levels[curr] = np.tile([-5, 5, -3, 3, -1, 1],
#                     int(np.ceil(len(timestampstest[curr])/6)))[:len(timestampstest[curr])]
# np.ndarray.tolist(levels)

# print(levels)