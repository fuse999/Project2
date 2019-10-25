import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Prediction and graph code

            https://github.com/fuse999/Project2

            or

            https://drive.google.com/file/d/136XggGZLLYWE9vldAQwJ0XRLSYohzK26/view?usp=sharing

            Data link

            https://www.kaggle.com/karun95/gradcafe-computer-science-results


            """
        ),

    ],
)

layout = dbc.Row([column1])