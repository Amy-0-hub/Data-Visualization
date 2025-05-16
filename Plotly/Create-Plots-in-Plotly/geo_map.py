#create an interactive map using gapminder dataset
import plotly.express as px

gapminder_df = px.data.gapminder()

#create a scatter geo plot for year 2007
fig=px.scatter_geo(
    gapminder_df[gapminder_df["year"] == 2007],
    locations="country",
    locationmode = "country names",
    size="lifeExp",
    hover_name = "country",
    color="gdpPercap",
    projection="natural earth",
    title="Life expectancy and GDP per Capita (2007)"
)


fig.show()