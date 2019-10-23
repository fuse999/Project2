import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

from app import app

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has 
twelve columns.

There are three main layout components in dash-bootstrap-components: Container, 
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column 
should take up a third of the width. Since we don't specify behaviour on 
smaller size screens Bootstrap will allow the rows to wrap so as not to squash 
the content.
"""

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Improveing Your Chances

            Using Mr.Acceptor will hellp you to to improve your likelyhood of getting into your graduating university.

            This is my first app I have made duing my short but amazing journey At Lambda Bootcamp. This is my second project in the course and shows just how far i have come in the last 6 weeks!!!

            To the right is A graphical representation of the data I used to train this application that I made.

            """
        ),
        dcc.Link(dbc.Button('Try It', color='primary'), href='/predictions'),
        dcc.Markdown(
            """

            Just click the button below to see my code for this project.

            """
        ),
        dcc.Link(dbc.Button('My Code', color='primary'), href='/process'),
    ],
    md=4,
)

df_with_pred = pd.read_csv('Pred_Data.csv')
# Making easy filters
cpass = df_with_pred['decision'] == 0
cfail = df_with_pred['decision'] == 1
right = (cpass) == (df_with_pred['pred_proba'] > 0.50)
wrong = ~right

fig = px.scatter(df_with_pred, x="decision", y="gre_quant", color="pred_proba",
           hover_name="degree")


column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])