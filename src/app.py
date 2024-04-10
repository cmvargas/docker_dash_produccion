from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import os

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')
debug = False if os.environ["DASH_DEBUG_MODE"] == "False" else True

app = Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1(children='Numero de poblacion por pais a traves de los años', style={'textAlign':'center'}),
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8050", debug=debug)