import plotly.graph_objects as go
import pandas as pd

data = pd.read_csv('./../data/covid_19_clean_complete.csv')
data_aus = data.loc[data['Country/Region'] == 'Australia']
data_aus.to_csv('./../data/aus_sick.csv', index=False)

labels = ['Recovered','Dead','Active cases']
values = [7183, 103, 6.606]

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
# fig.show()

