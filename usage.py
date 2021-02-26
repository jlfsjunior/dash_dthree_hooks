import dash_dthree_hooks
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_bootstrap_components as dbc

import random

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dash_dthree_hooks.Bubble(
        id='bubble-chart',
        width=1000,
        height=600,
    ),
    dbc.Button(id="update-data", children="Success", color="success", className="mr-1"),
])


@app.callback(
    Output('bubble-chart', 'data'), 
    [Input("update-data", 'n_clicks')]
)
def change_data(n_clicks):

    colors = ['red', 'green', 'blue', 'orange', 'yellow', 'purple', 'gray']

    n_points = random.randint(1, 10)

    data = [
        {
            'id': id, 
            'x': random.randint(0, 100),
            'y': random.randint(0, 100),
            'r': random.randint(0, 100),
            'color': random.choice(colors)
        } for id in range(n_points)  ]

    return data


if __name__ == '__main__':
    app.run_server(debug=True)
