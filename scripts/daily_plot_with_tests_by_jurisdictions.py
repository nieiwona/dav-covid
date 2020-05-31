import plotly.graph_objects as go
import pandas as pd
from plotly.subplots import make_subplots
import os

data_tests = pd.read_csv('./../data/Australia-COVID-Data.csv')
data_total = pd.read_csv('./../data/aus_covid_data.csv')
data = pd.read_csv('./../data/covid_19_clean_complete.csv')
data_aus = data.loc[data['Country/Region']=='Australia']
states_dates = data_aus[24:960]
nsw_cases_all = states_dates.loc[states_dates['Province/State'] == 'New South Wales']
nsw_cases = nsw_cases_all['Confirmed'].tolist()
vic_cases_all = states_dates.loc[states_dates['Province/State'] == 'Victoria']
vic_cases = vic_cases_all['Confirmed'].tolist()
qld_cases_all = states_dates.loc[states_dates['Province/State'] == 'Queensland']
qld_cases = qld_cases_all['Confirmed'].tolist()
total_dates = data_total.loc[(data_total['date'] >= '2020-01-25') & (data_total['date'] <= '2020-05-20')]
dates = data_tests['date'].tolist()
daily_tests = data_tests['daily'].tolist()
total_tests = data_tests['total'].tolist()
nsw_tests = data_tests['NSW'].tolist()
vic_tests = data_tests['VIC'].tolist()
qld_tests = data_tests['QLD'].tolist()

marker_color = 'rgb(111,201,163)'

# # Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Daily plot
fig.add_trace(
    go.Scatter(x=dates, y=list(total_dates.new_cases),
           name="New cases", line=dict(color='#3c19f0'),
           fill='tozeroy', fillcolor='#3c19f0', mode='lines'))


fig.add_trace(
    go.Scatter(x=dates, y=daily_tests, mode='lines+markers', marker_color=marker_color,
               name="Tests daily", yaxis="y2"))

# Cumulative plot
fig.add_trace(
    go.Scatter(x=dates, y=list(total_dates.total_cases),
           name="Cases", line=dict(color='#3c19f0'),
           fill='tozeroy', fillcolor='#3c19f0', mode='lines'))

fig.add_trace(
    go.Scatter(x=dates, y=total_tests, mode='lines+markers', marker_color=marker_color,
               name="Tests performed", yaxis="y2"))

# New South Walses (NSW)
fig.add_trace(
    go.Scatter(x=dates, y=nsw_cases,
           name="Cases", line=dict(color='#3c19f0'),
           fill='tozeroy', fillcolor='#3c19f0', mode='lines'))

fig.add_trace(
    go.Scatter(x=dates, y=nsw_tests, mode='lines+markers', marker_color=marker_color,
               name="Tests performed", yaxis="y2"))

# Victoria (VIC)
fig.add_trace(
    go.Scatter(x=dates, y=vic_cases,
           name="Cases", line=dict(color='#3c19f0'),
           fill='tozeroy', fillcolor='#3c19f0', mode='lines'))

fig.add_trace(
    go.Scatter(x=dates, y=vic_tests, mode='lines+markers', marker_color=marker_color,
               name="Tests performed", yaxis="y2"))

# Queensland (GLD)
fig.add_trace(
    go.Scatter(x=dates, y=qld_cases,
           name="Cases", line=dict(color='#3c19f0'),
           fill='tozeroy', fillcolor='#3c19f0', mode='lines'))

fig.add_trace(
    go.Scatter(x=dates, y=qld_tests, mode='lines+markers', marker_color=marker_color,
               name="Tests performed", yaxis="y2"))

# Create axis objects
fig.update_layout(
    xaxis=dict(
        domain=[0.7, 0.5]
    ),
    yaxis=dict(
        title="New infections",
        titlefont=dict(
            color="#1910d8"
        ),
        tickfont=dict(
            color="#1910d8"
        ),
        side='right'
    ),
    yaxis2=dict(
        title="Tests performed",
        titlefont=dict(
            color=marker_color
        ),
        tickfont=dict(
            color=marker_color
        ),
        side="left",
    )
)

# Add Annotations and Buttons
daily = [dict(x=dates, y=list(total_dates.new_cases)),
         dict(x=dates, y=daily_tests)
         ]
cumulative = [dict(x=dates, y=list(total_dates.total_cases)),
              dict(x=dates, y=total_tests)
              ]
nsw = [dict(x=dates, y=nsw_cases),
       dict(x=dates, y=nsw_tests)
       ]
vic = [dict(x=dates, y=vic_cases),
       dict(x=dates, y=vic_tests)
       ]
qld = [dict(x=dates, y=qld_cases),
       dict(x=dates, y=qld_tests)
       ]


fig.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            direction="right",
            active=0,
            x=0.57,
            y=1.2,
            buttons=list([
                dict(label="Daily",
                     method="update",
                     args=[{"visible": [True, True, False, False, False, False, False, False, False, False]},
                           {"title": "Cases daily",
                            "annotations": daily}]),
                dict(label="Cumulative",
                     method="update",
                     args=[{"visible": [False, False, True, True, False, False, False, False, False, False]},
                           {"title": "Cases cumulatively",
                            "annotations": cumulative}]),
                dict(label="NSW",
                     method="update",
                     args=[{"visible": [False, False, False, False, True, True, False, False, False, False]},
                           {"title": "New South Wales",
                            "annotations": nsw}]),
                dict(label="VIC",
                     method="update",
                     args=[{"visible": [False, False, False, False, False, False, True, True, False, False]},
                           {"title": "Victoria",
                            "annotations": vic}]),
                dict(label="QLD",
                     method="update",
                     args=[{"visible": [False, False, False, False, False, False, False, False, True, True]},
                           {"title": "Queensland",
                            "annotations": qld}])
            ]),
        )
    ])




# Set title
fig.update_layout(
    title_text="New cases of covid-19 and tests performed in Australia daily"
)

# Set template
fig.update_layout(
    template="plotly_white"
)

fig.update_layout(showlegend=True)

fig.show()

directory = './../images/'
f = "daily_plot_with_tests.html"
file_path = os.path.join(directory, f)
fig.write_html(file_path)
os.chdir(directory)
print(os.path.abspath(f))
