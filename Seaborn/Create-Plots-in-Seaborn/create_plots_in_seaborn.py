#import libraries
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#set global styles
sns.set_style("darkgrid")
sns.set_context("notebook")
sns.set_palette("muted")

#scatter plot of total bill vs tip (grouped by day)
tips = sns.load_dataset("tips")
plt.figure(figsize=(10,5))
sns.scatterplot(data=tips,
                x="total_bill",
                y="tip",
                hue="day")
plt.title("Total Bill vs Tip by Day")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.legend(title="Day of Week")
plt.show()

#scatter plot with custom style (poster, muted, darkgrid)
sns.set_style("darkgrid")
sns.set_context("poster")
sns.set_palette("muted")

sns.scatterplot(data=tips,
                x="total_bill",
                y="tip")
plt.title("Scatter Plot with Custom Aesthetics")
plt.show()

#violin plot: age by class and gender (titanic dataset)
titanic = sns.load_dataset("titanic")
plt.figure(figsize=(8,5))
sns.violinplot(data=titanic,
               x="class",
               y="age",
               hue="sex",
               palette="deep")
plt.title("Age Distribution by Passenger Class and Gender")
plt.show()

#line plot: total bill vs tip by time and sex
plt.figure(figsize=(8,5))
sns.lineplot(data=tips,
             x="total_bill",
             y="tip",
             hue="time",
             style="sex",
             markers=True,
             dashes=False,
             palette="muted")
plt.title("Total Bill vs Tip Amount")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.show()

#violin plot: total bill distribution by sex
plt.figure(figsize=(8,5))
sns.violinplot(data=tips,
               x="total_bill",
               hue="sex",
               split=True,
               palette="pastel")
plt.title("Total Bill Distribution by Gender")
plt.xlabel("Total Bill ($)")
plt.ylabel("Density")
plt.show()

#heatmap of flight passengers (year vs month)
flights = sns.load_dataset("flights")
flights_pivot = flights.pivot(index="year",
                              columns="month",
                              values="passengers")
plt.figure(figsize=(10,6))
sns.heatmap(flights_pivot,
            cmap="coolwarm",
            annot=True,
            linewidth=0.5)
plt.title("Monthly Airline Passenger Traffic (1949-1960)")
plt.show()

#pair plot iris dataset
iris = sns.load_dataset("iris")
sns.pairplot(iris,
             hue="species",
             markers=["o", "s", "D"],
             palette="coolwarm")
plt.suptitle("Pair Plot of Iris Features by Species", y=1.02)
plt.show()




