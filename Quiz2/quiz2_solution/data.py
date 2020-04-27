

#Import scikit-learn dataset library
from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Load dataset
wine = datasets.load_wine()

wine_data = wine.data
wine_target = wine.target.reshape((-1,1))

#wine_dt = np.concatenate((wine_data, wine_target), axis =1)

wine_dt = pd.DataFrame(wine_data).reset_index(drop=True)
wine_dt.columns = ['alcohol','malicAcid','ash','ashalcalinity','magnesium'
            	,'totalPhenols','flavanoids','nonFlavanoid','proanthocyanins'
            	,'colorIntensity','hue','od280','proline']


#1) Alcohol, 2) Malic acid, 3) Ash, 4) Alcalinity of ash, 5) Magnesium, 6) Total phenols,
# 7) Flavanoids, 8) Nonflavanoid phenols, 9) Proanthocyanins, 10)Color intensity, 11)Hue,
# 12)OD280 of diluted wines, 13)Proline.


#plt.scatter(wine_dt[0], wine_dt[1], c=wine_dt[13])

wine_dt.to_csv('wine_data.txt', index=False)

