import csv
import numpy as np
import pandas as pd

with open('cereal_data_no_missing.txt', newline='') as csvfile:
    spamreader1 = csv.reader(csvfile, delimiter='\t', quotechar='|')
    lista1 = list(spamreader1)
    matrix1 = np.array(lista1).astype("float")

with open('cereal_no_missing_matriz_PCA.txt', newline='') as csvfile:
    spamreader2 = csv.reader(csvfile, delimiter='\t', quotechar='|')
    lista2 = list(spamreader2)
    matrix2 = np.array(lista2).astype("float")

result = np.matmul(matrix1,matrix2)
##print(result)
n,m = result.shape
D4 = np.ones((n,1))
newresult = np.hstack((result,D4))
dFrame = pd.DataFrame(newresult,columns=['D1','D2','D3','D4'])
##jsonfile = dFrame.to_json(orient='index')

jsonfile = dFrame.to_json('cerealesrealdata.json',orient='records')
##print(jsonfile)