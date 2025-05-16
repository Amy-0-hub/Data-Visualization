import plotly.express as px

iris_df = px.data.iris()
fig = px.scatter_3d(
    iris_df,
    x="petal_width",
    y="petal_length",
    z="sepal_length",
    color="species",
    title="3D Scatter Plot of Iris Dataset"
)

fig.show()

#create another 3D surface plot 
#easy example
import numpy as np
import plotly.graph_objects as go

#create grid data
x=np.linspace(-5,5,100)
y=np.linspace(-5,5,100)
x, y = np.meshgrid(x,y)
z=np.cos(np.sqrt(x**2 + y**2))

#create a 3D susrface plot
fig=go.Figure(data=[
    go.Surface(
        z=z,
        x=x,
        y=y,
        colorscale="Viridis"
    )
]) 

#update layout
fig.update_layout(
    title="3D Surface Plot",
    scene = dict(zaxis_title="Z Value",
                xaxis_title="X Value",
                yaxis_title="Y Value")
)

fig.show()