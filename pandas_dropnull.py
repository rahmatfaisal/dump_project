import pandas as pd
import numpy as np

df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
    "toy": [np.nan, 'Batmobile', 'Bullwhip'],
    "born": [pd.NaT, pd.Timestamp("1940-04-25"),pd.NaT]})

print(df.dropna())          # Will drop NAN at data the default
print(df.dropna(axis=0))    # Will drop NAN at O or index
print(df.dropna(axis=1))    # Will drop NAN at 1 or columns
