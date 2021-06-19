import plotly.figure_factory as px
import pandas as pd

df = pd.read_csv('data.csv')

fig = px.create_distplot([df['Avg Rating'].tolist()], ['Rating'], 
#show_hist = False
)

fig.show()