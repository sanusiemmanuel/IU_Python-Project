import numpy as np
import pandas as pd
import math

train = pd.read_csv("train.csv")
ideal = pd.read_csv('ideal.csv')
test = pd.read_csv('test.csv')

ideal_col = ideal.columns.tolist()
train_col = train.columns.tolist()
test_col = test.columns.tolist()

ideal_col.remove('x')
train_col.remove('x')
test_col.remove('x')

# Calculate Mean Squared Error
def printmse(true, pred):
    MSE = np.square(np.subtract(true,pred)).mean()
    return MSE

def GenrateIdealFuntion():
# Select 4 Ideal Function among the 50 Ideal Function
    global df
    result = {}
    for j in train_col:
        all_mse = []
        for i in ideal_col:
            mse = printmse(ideal[i].values, train[j].values)
            all_mse.append(mse)
            min_val = all_mse.index(min(all_mse))

        result[f'Train Col {j}'] = f"Ideal Col {ideal_col[min_val]} with mse of {min(all_mse)}"

    choosen_ideal = {
        "x" : train['x'],
        "y1" : ideal['y47'],
        "y2" : ideal['y18'],
        "y3" : ideal['y22'],
        "y4" : ideal['y2']
    }

    df = pd.DataFrame(choosen_ideal)
    df.to_csv("choosen_ideal.csv",index=False)

# Mapping of the test dataset
def MappingOfTestData():
    test_x = range(len(test))
    y_test = []
    y_deviation = []
    for i in test_x:
        l_mse = []
        l_val = []
        x, y = test.iloc[i]
        d = df.loc[df['x'] == x][['y1','y2','y3','y4']].values
        e = train.loc[train['x'] == x][['y1','y2','y3','y4']].values
        for h, g in zip(d[0], e[0]):
            l_val.append(h)
            l_mse.append(math.sqrt(printmse(y, h)))
            min_ind = l_mse.index(min(l_mse))
        y_test.append(l_val[min_ind])
        y_deviation.append(l_mse[min_ind]) 

    test_final = {
        'X' : test['x'].tolist(),
        'Y' : test['y'].tolist(),
        'Delta_Y' : y_test,
        'Y_Deviation' : y_deviation
    }

    assigned_dataset = pd.DataFrame(test_final)
    assigned_dataset.to_csv('assigned_dataset.csv', index=False)

