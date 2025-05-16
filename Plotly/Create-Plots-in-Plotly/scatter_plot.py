import plotly.express as px
import pandas as pd

px.data.__all__
#visualing the relationship between total bill and tip
tips_df = px.data.tips()
tips_df.head()

#create an interative scatter plot
fig=px.scatter(
    tips_df,
    x="total_bill",
    y="tip",
    color="day",  #color points by day
    size="size",     #adjust points by size
    title="Total Bill vs. Tip"
)
fig.show()

#Try to use plot graph objects
#create tracts for each day and customize the layout to match the Plotly Express version
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

tips_df = px.data.tips()
#create a trace for each day
traces=[]
for day in tips_df["day"].unique():
    day_df = tips_df[tips_df["day"]==day]
    traces.append(
        go.Scatter(x=day_df["total_bill"],
                   y=day_df["tip"],
                   mode="markers",
                   marker=dict(
                       size=day_df["size"]*4,
                       opacity=0.7
                   ),
                   name=day
        )
    )

#create a figure
fig=go.Figure(traces)
#update layout
fig.updaye_layout(
    title="Total Bill vs Tip",
    xaxis_title="Total Bill ($)",
    yaxis_title="Tip ($)",
    template="plotly"
)
fig.show()