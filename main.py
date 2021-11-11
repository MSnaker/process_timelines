import numpy as np
import pandas as pd
from timeline import TimeLine

file_name = './file/timestamps.xlsx'
data = pd.read_excel(file_name, sheet_name='Sheet1')

# print(len(data.columns))

l=0
while(l<len(data.columns)):

    print('Numero ',str(l/3+1))
    i = 0
    datalabels,datatimes = [],[]
    for element in data[data.columns[l]]:
        if not np.isnan(element):
            datatimes.append(element)
            datalabels.append(''.join([data[data.columns[l+1]][i],'\n Handler: ',data[data.columns[l+2]][i]]))
        i+=1

    tl = TimeLine(datatimes,datalabels,''.join(["numero",str(l/3+1)]))
    tl.plot()
    l+=3
