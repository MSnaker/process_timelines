import pandas as pd

from timeline import TimeLine

file_name = './file/prova.xlsx'
data = pd.read_excel(file_name, sheet_name='Sheet1')

tl = TimeLine(data["timestamps"],data["caption"], "titolo")
print(tl.timestamps, '\n', tl.labels)

tl.plot()
