import pandas as pd
import plotly.graph_objects as go
import os
import plotly.express as ex


def plot_age_sex(data_file, outfile):
	print('Creating age-sex barplot')

	data = pd.read_csv(data_file, sep='\t')

	c = ex.colors.qualitative.Safe
	fig = go.Figure()

	fig.add_trace(
	    go.Bar(x=data.Age, y=list(data.Male),
	           name="Male", marker_color=c[0])
	)

	fig.add_trace(
	    go.Bar(x=data.Age, y=list(data.Female),
	           name="Female", marker_color=c[1])
	)

	fig.update_layout(
	    template="plotly_white"
	)

	fig.update_layout(
	    title_text="COVID-19 cases by age group and sex",
	    font=dict(
	        size=18
	    ),
	    xaxis_title="Age",
	    yaxis_title="Number of cases",
	)

	fig.write_html(outfile)
	print('Plot saved to {}'.format(outfile))


data_file = '../data/cases_age_sex.tsv'
outfile = '../images/age-sex-plot.html'
plot_age_sex(data_file, outfile)
