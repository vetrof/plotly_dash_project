from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
from django_plotly_dash import DjangoDash
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('dash_app', external_stylesheets=external_stylesheets)

# Load data from CSV
df = pd.read_csv('data.csv')


app.layout = html.Div([
    html.H1(""),

    dcc.Input(
        id='attribute-search',
        type='text',
        placeholder='Search attribute...',
        value=''
    ),

    # Dropdown for selecting parameters on the X-axis
    dcc.Dropdown(
        id='x-axis-dropdown',
        options=[
            {'label': col, 'value': col} for col in df.columns
        ],
        value='dAge',
        multi=False,
        placeholder='Select parameter on X-axis'
    ),

    # Dropdown for selecting parameters on the Y-axis
    dcc.Dropdown(
        id='y-axis-dropdown',
        options=[
            {'label': col, 'value': col} for col in df.columns
        ],
        value='dHours',
        multi=False,
        placeholder='Select parameter on Y-axis'
    ),

    # Data loading indicator
    dcc.Loading(
        id="loading-indicator",
        type="default",
        children=[
            # Scatter plot
            dcc.Graph(id='scatter-plot'),

            # Histogram
            dcc.Graph(id='histogram')
        ]
    )
])


@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('attribute-search', 'value'),
     Input('x-axis-dropdown', 'value'),
     Input('y-axis-dropdown', 'value')]
)
def update_scatter_plot(selected_attribute, selected_x_axis, selected_y_axis):
    if not selected_attribute:
        # Return the current scatter plot if no attribute is selected
        return px.scatter(df, x=df[selected_x_axis], y=df[selected_y_axis],
                          title=f'Scatter Plot: {selected_x_axis}, {selected_y_axis}')

    # Use selected parameters in the scatter plot
    fig = px.scatter(df, x=df[selected_x_axis], y=df[selected_y_axis],
                     title=f'Scatter Plot: {selected_x_axis}, {selected_y_axis}')
    return fig


@app.callback(
    Output('histogram', 'figure'),
    [Input('attribute-search', 'value'),
     Input('x-axis-dropdown', 'value')]
)
def update_histogram(selected_attribute, selected_x_axis):
    if not selected_attribute:
        return px.histogram(df, x=df[selected_x_axis], title=f'Histogram: {selected_x_axis}')

    fig = px.histogram(df, x=df[selected_x_axis], title=f'Histogram: {selected_x_axis}')
    return fig
