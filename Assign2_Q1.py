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