#create a 1x2 subplot grid
## in the left subplot, create a scatter plot of petal length vs. petal width from the iris dataset
## in the right subplot, create a histogram of sepal lengths.

#import libraries
import plotly.express as px
import plotly.subplots as sp

iris_df = px.data.iris()
iris_df.describe()

#create two subplots
fig=sp.make_subplots(
    rows=1,
    cols=2,
    subplot_titles=("Petal length vs. Petal width", "Histogram of sepal lengths")
)

#create a scatter plot
scatter_fig = px.scatter(
    iris_df,
    x="petal_length",
    y="petal_wodth",
    color="species",
)

#add scatter plot to the first subplot
for trace in scatter_fig.data:
    fig.add_trace(trace, row=1, col=1)

#create a histogram 
histogram_fig = px.histogram(
    iris_df,
    x="sepal_length",
    color="species",
)

#add histogram to the second subplot
for trace in histogram_fig.data:
    fig.add_trace(trace, row=1, col=2)

#update layout of the overall subplot
fig.update_layout(title_text="Iris dataset subplots")

#add axis labels for the scatter plot
fig.update_xaxes(title_text="Petal Length", row=1, col=1)
fig.update_yaxes(title_text="Petal Width", row=1, col=1)

#add axis label for the histogram
fig.update_xaxes(title_text="Petal Length", row=1, col=2)
fig.update_yaxes(title_text="Sepal Length", row=1, col=2)


fig.show()