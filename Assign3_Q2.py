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

ax[1].boxplot(df["ViolentCrimesPerPop"], showfliers=True)
ax[1].set_xlabel("Violent Crimes")
ax[1].set_ylabel("Violent Crimes Per Population")
ax[1].set_title("Box Plot of Violent Crimes Per Population")

plt.show()

# Answer the questions-------------------------------------------------------------------------
# Histogram divide the range of values into a number of bins and reflect the frequency of each bin. According to this histogram, this is right-skewed histogram because it shows the peak values on the left side of the histogram and lower values are on the right side.
# Box plot summary the median value, max and min values, 25th, 50th, 75th percentile of data. The middle line in the box determine the median value which is ~0.385 . Lower bound of the box determine the 25th percentile which is ~0.2 and 75th percentile is ~0.645 which is show on the top bound of the box. Two handle of the box determine the max and values are ~0.017 and ~0.995.
# Generally, box plot can show the outliers like a dot, but there is no outliers shown in this box plot.




