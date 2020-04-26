

#Import scikit-learn dataset library
from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Load dataset
wine = datasets.load_wine()

wine_data = wine.data
wine_target = wine.target.reshape((-1,1))

wine_dt = np.concatenate((wine_data, wine_target), axis =1)


wine_dt = pd.DataFrame(wine_dt).reset_index(drop=True)


plt.scatter(wine_dt[0], wine_dt[1], c=wine_dt[13])

wine_dt.to_csv('wine_data.txt', header=None, index=False)

