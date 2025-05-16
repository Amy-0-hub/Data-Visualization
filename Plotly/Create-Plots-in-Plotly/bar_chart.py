import pandas as pd
import plotly.express as px

df=px.data.tips()
df.head()

#calculate average tip amount by day
average_tip_day = df.groupby("day")["tip"].mean().reset_index()

#create a bar chart using average values
fig=px.bar(
    average_tip_day,
    x="day",
    y="tip",
    color="day",
    title = "Average tip by each day"
)

#update the y-axis label
fig.update_layout(
    yaxis_title="Average tip ($)"
)

#display the figure
fig.show()