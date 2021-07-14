import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from sklearn.decomposition import PCA
import numpy as np

colors = {
    'text': '#09b6f0'
}

#load data
df = px.data.iris()
features = ["sepal_width", "sepal_length", "petal_width", "petal_length"]
pca = PCA()
components = pca.fit_transform(df[features])

total_var = pca.explained_variance_ratio_.sum() * 100
labels = {str(i):f"PC{i+1}({var:.1f}%)" for i, var in enumerate(pca.explained_variance_ratio_*100)}
fig = px.scatter_matrix(
    components, 
    labels=labels,
    dimensions = range(4),
    color = df['species'],
    title=f'Total Explained Variance: {total_var:.2f}%'
)
fig.update_traces(diagonal_visible=False)

explained_var = pca.explained_variance_ratio_[0:3].sum() * 100

fig1 = px.scatter_3d(
    components[:,0:3], x=0, y=1, z=2, color=df['species'],
    title=f'Total Explained Variance: {explained_var:.2f}%',
    labels={'0': 'PC 1', '1': 'PC 2', '2': 'PC 3'}
)

exp_var_cumul = np.cumsum(pca.explained_variance_ratio_)
fig2 = px.area(
    x=range(1, exp_var_cumul.shape[0] + 1),
    y=exp_var_cumul,
    labels={"x": "# Components", "y": "Explained Variance"}
)

X = df[features]
loadings = pca.components_[0:2].T * np.sqrt(pca.explained_variance_[0:2])
fig3 = px.scatter(components, x=0, y=1, color=df['species'])
for i, feature in enumerate(features):
    fig3.add_shape(
        type='line',
        x0=0, y0=0,
        x1=loadings[i, 0],
        y1=loadings[i, 1]
    )
    fig3.add_annotation(
        x=loadings[i, 0],
        y=loadings[i, 1],
        ax=0, ay=0,
        xanchor="center",
        yanchor="bottom",
        text=feature,
    )

app = dash.Dash(__name__)

# initialise the app


""" @app.callback(Output("graph_with_slider", "figure"),Input("slider", "value")) """


app.layout = html.Div(children=[
        html.H1(children='My PCA App',
         style={
             'textAlign': 'center',
             'color': colors['text']

         }
    ),


    html.Div(children='''
    WEEK 11
    '''),

    dcc.Graph(
        id='graph_with_slider',
        figure=fig
    ),
    dcc.Slider(
        id='slider',
        min=2, max=4, value=3,
        marks={i: str(i) for i in range(2,5)}),
    dcc.Graph(
        id='graph1',
        figure=fig1
    ),
    dcc.Graph(
        id='graph2',
        figure=fig2
    ),
    dcc.Graph(
        id='graph3',
        figure=fig3
    )
])    

# RUN THE APP

if __name__ == '__main__':
    app.run_server(debug=True, port=5000)
