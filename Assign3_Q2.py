# Anne Tran (UCID: 30286177)
# Assign2_Q2
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("crime.csv")
fig, ax=plt.subplots(1,2, figsize=(15,6))

ax[0].hist(df["ViolentCrimesPerPop"], color="black", edgecolor="white")
ax[0].set_xlabel("Violent Crimes Per Population")
ax[0].set_ylabel("Frequency")
ax[0].set_title("Histogram of Violent Crimes Per Population")

ax[1].boxplot(df["ViolentCrimesPerPop"])
ax[1].set_xlabel("Violent Crimes")
ax[1].set_ylabel("Violent Crimes Per Population")
ax[1].set_title("Box Plot of Violent Crimes Per Population")

plt.show()




