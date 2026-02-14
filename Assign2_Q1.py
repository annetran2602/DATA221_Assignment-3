# Anne Tran (UCID: 30286177)
# Assign2_Q1

import pandas as pd
import numpy as np

df=pd.read_csv("crime.csv")
mean=np.mean(df["ViolentCrimesPerPop"].values)
median=np.median(df["ViolentCrimesPerPop"].values)
standardDeviation=np.std(df["ViolentCrimesPerPop"].values)
min=np.min(df["ViolentCrimesPerPop"].values)
max=np.max(df["ViolentCrimesPerPop"].values)
print(f"Mean:{mean:.03f}")
print(f"Median: {median}")
print(f"Standard deviation: {standardDeviation:.03f}")
print(f"Min value: {min}")
print(f"Max value: {max}")

#-------------------------------------------------------------------------------------
# Since we have median=0.441 and mean=0.39 where mean is greater than median. So that the distribution is right skewed because high values pull the mean to the right that makes it greater than median by ~0.06.
# If there are extreme values like very large or small values, it would affect the mean since it calculate based on the sum of all values whereas larger value will pull the mean to the right. However, median will not be affect much because it is only determined based on the middle position of dataset.