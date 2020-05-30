import plotly.graph_objects as go

values = []
total_cases = 7183
total_deaths = 103
total_recovered = 6606

values = []
values.append(total_recovered)
values.append(total_deaths)
values.append(total_cases - total_recovered - total_deaths)
labels = ['Recovered','Dead','Active cases']
colors = ['rgb(169,220,103', 'rgb(0,0,0)', '#3c19f0']

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=14,
                  marker=dict(colors=colors))

fig.update_layout(
    title_text="Current status of confirmed cases of covid-19"
)

fig.show()

