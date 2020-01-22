import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import joblib
import plotly.graph_objs as go

app = dash.Dash()
model = joblib.load('model.dmp')

app.layout = html.Div(children=[
    html.H1(children='Simple Linear Regression', style={'textAlign': 'center'}),

    html.Div(children=[
        html.Label('Input your Features : '),
        dcc.Input(id='input1', placeholder='features 1', type='text'),
        dcc.Input(id='input2', placeholder='features 2', type='text'),
        dcc.Input(id='input3', placeholder='features 3', type='text'),
        dcc.Input(id='input4', placeholder='features 4', type='text'),
        html.Div(id='result')
    ], style={'textAlign': 'center'}),
])

@app.callback(
    Output(component_id='result', component_property='children'),
    [Input(component_id='input1', component_property='value'),
    Input(component_id='input2', component_property='value'),
    Input(component_id='input3', component_property='value'),
    Input(component_id='input4', component_property='value')])

def update_years_of_experience_input(input1, input2, input3, input4):
    try:
        prediction = model.predict([[input1,input2,input3,input4]])
        return 'Prediction is {}'.format(prediction)
    except ValueError:
        return 'Unable to give prediction'

if __name__ == '__main__':
    app.run_server(debug=True)
