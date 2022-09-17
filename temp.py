>>> def fromCSV(path,delimiter,quotechar):
...     import csv
...     data=list()
...     with open(path, newline='') as csvfile:
...             filecontent=csv.DictReader(csvfile, delimiter=delimiter, quotechar=quotechar)
...     for row in filecontent:
...             data.append(row)
...     return data
... 
>>> def extract_month(row):
...     value=row['Date']
...     MM=""
...     a=value.split("/")
...     MM=a[0]
...     new_row=row.copy()
...     new_row.update({'Month':MM})
...     return new_row
... 
>>> data=fromCSV(path='C:\Users\Kiosk\Downloads\JobReadyPython\JobReadyPython\data\stocks.csv', delimiter=',', quotechar='|')
  File "<stdin>", line 1
    data=fromCSV(path='C:\Users\Kiosk\Downloads\JobReadyPython\JobReadyPython\data\stocks.csv', delimiter=',', quotechar='|')
                                                                                              ^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape

                                                           ^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXX
X escape
>>> data=fromCSV(path='file:///C:/users/kiosk/downloads/stocks.csv', delimiter=',', quotechar='|')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in fromCSV
FileNotFoundError: [Errno 2] No such file or directory: 'file:///C:/users/kiosk/downloads/stocks.csv'
