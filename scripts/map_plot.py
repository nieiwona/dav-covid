import geopandas as gpd
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects
import os, shutil
import numpy as np
from matplotlib.animation import FuncAnimation


def plot_map(map_file, cities_file, cases_file, outfile):
	map_df = gpd.read_file(map_file)
	notnone = [i for i, la in enumerate([el is not None for el in map_df['iso3166_2']]) if la]
	map_df = map_df.loc[notnone]
	map_df['id'] = [el.replace('AU-', '') for el in map_df['iso3166_2'].values]
	map_df = map_df[['id', 'name', 'geometry']]

	cases = pd.read_csv(cases_file, sep='\t')
	cases = cases.rename({'Unnamed: 0': 'id'}, axis=1)

	dates = list(cases.columns)
	dates.remove('id')

	merged = map_df.merge(cases, on='id')

	cities = pd.read_csv(cities_file, sep='\t')
	cities = gpd.GeoDataFrame(cities, geometry=gpd.points_from_xy(cities.Longitude, cities.Latitude))

	dates = dates[dates.index('2020-03-10')::2]

	fig, ax = plt.subplots(1, figsize=(10, 10))
	texts = []
	val = cases.drop('id', axis=1)
	vmin, vmax = np.min(val.values), np.max(val.values)
	norm = plt.Normalize(vmin=vmin, vmax=vmax)
	cbar = plt.cm.ScalarMappable(norm=norm, cmap='Blues')
	ax_cbar = fig.colorbar(cbar, ax=ax, fraction=0.03, pad=0.09)
	ax_cbar.set_label('Cases', fontsize=15)

	def init():
   		ax.axis('off')

	def update(date):
		print(date)
		for txt in texts:
			txt.set_visible(False)
		merged.plot(column=date, cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8', 
					norm=plt.Normalize(vmin=vmin, vmax=vmax), vmin=vmin, vmax=vmax)
		cities.plot(ax=ax, color='red', alpha=0.8)
		for x, y, label in zip(cities.geometry.x, cities.geometry.y, cities.City):
			if label in ['Sydney', 'Logan City', 'Geelong', 'Adelaide']:
				ax.annotate(label, xy=(x, y), xytext=(-5, 0), ha='right', textcoords="offset points", fontsize=13)
			elif label in ['Gold Coast', 'Canberra']:
				ax.annotate(label, xy=(x, y), xytext=(5, -6), textcoords="offset points", fontsize=13)
			else:
				ax.annotate(label, xy=(x, y), xytext=(8, 0), textcoords="offset points", fontsize=13)
		for el in [child for child in ax.get_children() if isinstance(child, matplotlib.text.Annotation)]:
			el.set_path_effects([PathEffects.withStroke(linewidth=5, foreground='w')])    
		ax.set_title('New cases of COVID-19 in Australia', fontdict={'fontsize': 25, 'fontweight': 3})
		txt = ax.annotate(date, xy=(0.1, 0.33), xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=30)
		texts.append(txt)

	anim = FuncAnimation(fig=fig, func=update, init_func=init, frames=dates, repeat=False, interval=300, cache_frame_data=False)
	html = anim.to_html5_video()
	with open(outfile, 'w') as f:
		f.write(html)


data_dir = '../data/'
map_file = os.path.join(data_dir, 'Australia_Polygon.shp')
cities_file = os.path.join(data_dir, 'cities.tsv')
cases_file = os.path.join(data_dir, 'australia_sum_cases.tsv')
outfile = '../images/map.html'

plot_map(map_file, cities_file, cases_file, outfile)

