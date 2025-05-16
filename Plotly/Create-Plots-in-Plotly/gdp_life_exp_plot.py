import plotly.express as px

#load the Gapminder dataset
gapminder_df = px.data.gapminder()
gapminder_df.describe()

#filter data for the year 2007
gapminder_df_2007 =  gapminder_df[gapminder_df["year"] == 2007]

#create an interactive scatter plot
fig = px.scatter(
    gapminder_df_2007,
    x="gdpPercap",
    y="lifeExp",
    color="continent",
    size="pop",
    hover_name = "country",
    title="GDP per Capita vs. Life Expectancy (2007)",
    log_x=True,
)

#update the hover template using fig.update_traces()
fig.update_traces(
    hovertemplate="<b>GDP per Capita: </b> %{x} <br>"
                  "<b>Life Expectancy: </b> %{y} years"
                  "<b>Country:</b> %{hovertext} </br>"
)


#add a range slider to filer the dataset by GDP per Captia
fig.update_layout(
    dragmode='zoom',
    xaxis=dict(
        rangeslider=dict(visible=True),
        title="GDP per Capita"
    ),
    yaxis=dict(title="Life Expectancy")
)

fig.show()