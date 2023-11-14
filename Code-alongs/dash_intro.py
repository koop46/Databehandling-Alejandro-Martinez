from dash import Dash, html, dcc, callback, Output, Input
import plotly_express as px

df

app = Dash(__name__)


app.layout = html.Div([
    html.H1(children="My dash application"),
    html.H2(id="my-H2", children="more info..."),
    dcc.Dropdown(id="my-dropdown", options=["Uno", "dos", "tre"], value=2007),
    dcc.Graph(id="my-graph", figure={})]        
    )


@callback(
    Output("my_graph", component_property="figure"),
    Input("my_dropdown", component_property="value")
)
def update_heading2(year):
    return px.strip(df.query=("year==@year"), x="lifeExp", color="continent")



app.run(debug=True)



