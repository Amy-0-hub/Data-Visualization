#create a scatter plot of the iris dataset with customized colors and markers.
## adjust the axis titles and ranges to enhance clarity
## add an annotation to one of the points to highlight an important observation

#import libraries
import plotly.graph_objects as go
import plotly.express as px

#input dataset
iris_df = px.data.iris()
iris_df.head()
iris_df.describe()


#I want to choose "sepal_width" and "species" features to use to represent the x- and y-axes
fig = go.Figure(data=go.Scatter(x=iris_df["sepal_width"],
                                y=iris_df["species_id"],
                                mode = "markers",
                                marker = dict(color="red")))

#update layout for axes customrization
fig.update_layout(
    title = 'Scatter plot of the iris dataset',
    xaxis_title = 'sepal_width',
    yaxis_title="species_id",
    xaxis=dict(range=[2,5]),  #set x-axis range
    yaxis=dict(range=[0,5])    #set y-axis range
)

#add annotation for specific points
fig.add_annotation(
    x=3.0,
    y=2.0,
    text="Example Annotation",
    showarrow=True,
    arrowhead=2,
    ax=20,
    ay=-30
)

fig.show()