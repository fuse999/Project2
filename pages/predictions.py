import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from app import app
import pandas as pd

df_with_pred = pd.read_csv('Prediction.csv')
fig = px.scatter(df_with_pred, x="pred_proba", y="undergrad_gpa", color="decision",
           hover_name="degree")
column1 = dbc.Col(
    [
        
        dcc.Markdown(
            """
            # Predictions
            """
        ),
        
        dcc.Markdown(
            """
            ## Explain Main Page Graph
            """
        ),
        
        dcc.Markdown(
            """
            ## Explain perdiction Fetures
            """
        ),
        
        #dcc.Markdown(
        #    """
        #    ## Predictions
        #    """
        #),
        
        #dcc.Markdown(
        #    """
        #    ## Predictions
        #    """
        #),
        
        #dcc.Markdown(
        #    """
        #    ## Predictions
        #    """
        #),
    ],
    md=4,
)

column2 = dbc.Col(
    [

       dcc.Graph(figure=fig), 
       html.Img(src='assets/feature graph.png', className='img-fluid'),
       #html.Img(src='assets/PDP for Undergrad GPA.png', className='img-fluid'),
       #html.Img(src='assets/gre_verbal.png', className='img-fluid'),
       #html.Img(src='assets/Gre_Quant.png', className='img-fluid'),
       #html.Img(src='assets/PDP Crurrent AVG GPA.png', className='img-fluid'),

    ]
)

layout = dbc.Row([column1, column2])