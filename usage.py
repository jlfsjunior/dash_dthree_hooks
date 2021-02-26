import dash_dthree_hooks
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_bootstrap_components as dbc

import random
import json

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    [
        dash_dthree_hooks.Bubble(
            id='bubble-chart',
        ),
        html.Div(
            [
                dbc.Button(id="update-data", children="Update Data", color="success", className="mr-1"),
                html.P(id='clicked-output')
            ]
        )
    ],
    style={
        "padding": "25px 50px"
    }
)


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

@app.callback(
    Output('clicked-output', 'children'), 
    [Input("bubble-chart", 'clicked')]
)
def click_point(datum):

    print(datum)

    datum_str = json.dumps(datum)

    return datum_str

if __name__ == '__main__':
    app.run_server(debug=True)
