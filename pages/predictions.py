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
            ## What is my data
            The data set I have aquired contains information gathered from 1500+ schools between 2009 and 2020,
             about almost all students applying to enter a graduate degree program in computer science. 

            """
        ),
        
        dcc.Markdown(
            """
            ## Why am I predicting with the data
            I am predicting with this data because I myself would like to become a computer engineer and found this information interesting. By using this information I was hoping to help myself and others learn what the most important features are when applying for a graduate degree.
            """
        ),
        
        dcc.Markdown(
            """
            ## Explanation of first graph
            I have included this graph because the student’s undergrad gpa was almost the highest ranked feature in relation to being accepted into a graduate program. This graph shows a student’s undergrad gpa in relation to the predicted probability of acceptance based on all top 9 features, excluding the student requested id. The trend that the graph shows is that as a student’s undergrad gpa increases, the probability of that student being accepted into a graduate program also increases. 
            """
        ),
        
        dcc.Markdown(
            """
            ## Explanation of second graph
            This graph shows the top 9 features of importance in relation to being accepted into a graduate program. One of the most important was the student’s undergrad gpa, which makes sense because it shows their pattern of educational accomplishment. Another factor that had a big influence was their Graduation Requirement Examination (GRE) scores. Of the three parts of the GRE, the writing (awa) score was not as important as the quantitative or verbal; and the verbal was more important than the quantitative.
            """
        ),
        
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

       html.Img(src='assets/feature graph.png', className='img-fluid'),
       dcc.Graph(figure=fig),
       #html.Img(src='assets/PDP for Undergrad GPA.png', className='img-fluid'),
       #html.Img(src='assets/gre_verbal.png', className='img-fluid'),
       #html.Img(src='assets/Gre_Quant.png', className='img-fluid'),
       #html.Img(src='assets/PDP Crurrent AVG GPA.png', className='img-fluid'),

    ]
)

layout = dbc.Row([column1, column2])