import dash_dthree_hooks
import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_bootstrap_components as dbc

import random
import json

import pandas as pd

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.DataFrame({
    "text": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "value": [4, 1, 2, 2, 4, 5, 10, 1, 5, 2, 7, 5],
    "id": [ i for i in range(12)],
})


app.layout = html.Div(
    [
        # dash_dthree_hooks.Bubble(
        #     id='bubble-chart',
        # ),
        # html.Div(
        #     [
        #         dbc.Button(id="update-data", children="Update Data", color="success", className="mr-1"),
        #         html.P(id='clicked-output')
        #     ]
        # ),

        dash_dthree_hooks.WordCloud(
            id="wordcloud-chart",
            data=df.to_dict("records"),
            style={"fillSelected": "blue"}
            # selected=[1, 2, 3]
        ),
        html.Div(
            id="wordcloud-clicked"
        ),
        html.Div(
            id="wordcloud-selected"
        )
    ],
    style={
        "padding": "25px 50px"
    }
)

@app.callback(
    # Output('wordcloud-clicked', 'children'),
    Output("wordcloud-chart", 'selected'), 
    [Input("wordcloud-chart", 'clicked'), Input("wordcloud-chart", 'clickedTimestamp'), State("wordcloud-chart", 'selected')]
)
def clicked_word(word, timestamp, selected_ids):
    # print(word)

    if word is None:
        return selected_ids

    clicked_id = word["id"]

    if selected_ids is None:
       return [clicked_id]  

    if clicked_id in selected_ids:
        new_selected_ids = [ i for i in selected_ids if i != clicked_id  ]
    else:
        new_selected_ids = [*selected_ids, clicked_id]

    print(new_selected_ids)

    return new_selected_ids


# @app.callback(
#     Output('wordcloud-selected', 'children'), 
#     [Input("wordcloud-chart", 'selected')]
# )
# def selected_word(ids):
#     print(ids)

#     if ids is None:
#         return "No words selected"

#     return len(ids)



# @app.callback(
#     Output('bubble-chart', 'data'), 
#     [Input("update-data", 'n_clicks')]
# )
# def change_data(n_clicks):

#     colors = ['red', 'green', 'blue', 'orange', 'yellow', 'purple', 'gray']

#     n_points = random.randint(1, 10)

#     data = [
#         {
#             'id': id, 
#             'x': random.randint(0, 100),
#             'y': random.randint(0, 100),
#             'r': random.randint(0, 100),
#             'color': random.choice(colors)
#         } for id in range(n_points)  ]

#     return data

# @app.callback(
#     Output('clicked-output', 'children'), 
#     [Input("bubble-chart", 'clicked')]
# )
# def click_point(datum):
#     if datum is None:
#         return "Click on something!"
#     else:
#         datum_str = json.dumps(datum)
#         return datum_str

if __name__ == '__main__':
    app.run_server(debug=True)
