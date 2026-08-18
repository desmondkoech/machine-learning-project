import pandas as pd
import numpy as np

def synth(n=500):
    x = np.linspace(0,100,n)
    y = 2.0*x + np.random.normal(0,10,n)
    pd.DataFrame({'x':x,'y':y}).to_csv('data/sample_large.csv', index=False)
    print('Wrote data/sample_large.csv')

if __name__=='__main__':
    synth()
