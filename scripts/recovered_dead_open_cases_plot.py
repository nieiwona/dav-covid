import plotly.graph_objects as go
import os

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

fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=16,
                  marker=dict(colors=colors))

fig.update_layout(
    title_text="Current state of confirmed cases of COVID-19 <br>Status by 2020-05-30"
)

fig.update_layout(
    font=dict(size=18)
)

fig.update_layout(
    autosize=False,
    width=700,
    height=700
)

fig.show()


directory = './../images/'
f = "recovered_dead_active_pieplot.html"
file_path = os.path.join(directory, f)
fig.write_html(file_path)
os.chdir(directory)
print(os.path.abspath(f))