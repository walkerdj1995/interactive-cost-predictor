import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from train_model import random_model

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

layoutHome = html.Div([  
	# Add dashbaord header/title.            
    dbc.Row([
        dbc.Col([
                
        html.Label("Delivery Method"),
        dcc.Dropdown(id = 'delivery',
                options=[
                    {'label': i, 'value': i} for i in ['DB','DBB']
                        ],
                    placeholder="Select a Delivery Method",
                    value = 'DB',
                    multi=False
                    )],
        align = "center",
        
        width = {'size':3}),
        
        dbc.Col([
        html.Label("Project Type"),
        dcc.Dropdown(id = 'proj-typ',
                    options=[
                                {'label': i, 'value': i} for i in ['New Build','EPB','Other']
                            ],
                    placeholder="Select Project Type",
                    value = "New Build",
                    multi = False
                    )],                       
        align = "center",
        
        width = {'size':3}),
        
        dbc.Col([
        html.Label("Project Duration"),
        dcc.Slider(
                id = 'proj-dur',
                min=0,
                max=365,
                step=1,
                marks={
                        0 : '0 days',
                        183 : '6 Months',
                        365 : '12 Months'},
                value=60
            )],
        align = "center",
        
        width={"size": 3}),
        
        ],
        justify = 'around',
        style = {'padding':30}),

    dbc.Row([
        dbc.Col([
                
        html.Label("Project Cost"),
        dcc.Input(id='proj-cost',type='number',placeholder='Estimated Project Cost (£)')],
        align = "center",
        
        width = {'size':4}),

        dbc.Col([
                
        html.Label("Competition"),
        dcc.Input(id='comp',type='number',placeholder='Input number of other bidders')],
        align = "center",
        
        width = {'size':4}),
        
        
        dbc.Col([
        html.Label("Award Method"),
        dcc.Dropdown(id = 'award-method',
                    options=[
                                {'label': i, 'value': i} for i in ['Qualification-based selection','Low-bid selection']
                            ],
                    placeholder="Select Award Method",
                    multi = False
                    )],                       
        align = "center",
        
        width = {'size':4}),
        
        ],
        justify = 'around',
        style = {'padding':30}),

    dbc.Row([
        html.H1(id='prediction'),
    ])

            ]
        )

app.layout = html.Div(children=[
        dcc.Tabs(
                id='tabs',
                value = 'tabsLayoutHome',
                children = [
                        dcc.Tab(label = 'Cost-Overrun Predictor', value = 'tabsLayoutFin', children = layoutHome),
                        ])
])

@app.callback(
    Output("prediction", "children"),
    Input("delivery", "value"),
    Input("proj-typ", "value"),
    Input("proj-dur", "value"),
    Input("proj-cost", "value"),
    Input("comp", "value"),
    Input("award-method", "value"),
)

def predict(a,b,c,d,e,f):
    lvl = random_model()
    return f'Predicted Cost Overrun Level: {lvl}'


if __name__ == '__main__':
    app.run_server(debug=True)