from matplotlib.animation import FuncAnimation
import pandas as pd
import matplotlib.pyplot as plt
import os


def nice_axes(ax):
    ax.set_facecolor('white')
    ax.tick_params(labelsize=8, length=0)
    ax.grid(True, axis='x', color='.8')
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(False)
 

def prepare_data(df, steps=5):
    df = df.reset_index()
    df.index = df.index * steps
    last_idx = df.index[-1] + 1
    df_expanded = df.reindex(range(last_idx))
    df_expanded['date'] = df_expanded['date'].fillna(method='ffill')
    df_rank_expanded = df_expanded.rank(axis=1, method='first')
    df_expanded = df_expanded.interpolate()
    df_rank_expanded = df_rank_expanded.interpolate()
    return df_expanded, df_rank_expanded


def plot_bars(data_file, outfile):
    print('Creating bar plot')
    colors = plt.cm.Dark2(range(6))
    data = pd.read_csv(data_file, sep='\t', index_col=0)
    data.index.name = 'date'
    df_expanded, df_rank_expanded = prepare_data(data)
    labels = list(df_expanded.columns)[1:]
    texts = []
    fig = plt.Figure(figsize=(8, 13))
    ax = fig.add_subplot()
    fig.subplots_adjust(left=0.25, top=0.95, bottom=0.05)
    ax.clear()
    nice_axes(ax)
    ax.set_ylim(.2, 6.8)

    def update(i):
        for txt in texts:    
            txt.set_visible(False)
        for bar in ax.containers:
            bar.remove()
        y = df_rank_expanded.iloc[i].values.astype(float)
        width = df_expanded.iloc[i].values[1:].astype(float)
        ax.barh(y=y, width=width, color=['C1' if el == 'Australia' else 'C0' for el in labels], 
                tick_label=[r"$\bf{Australia}$" if l == 'Australia' else l for l in labels])
        for tick in ax.yaxis.get_major_ticks():
            tick.label.set_fontsize(15)
        for tick in ax.xaxis.get_major_ticks():
            tick.label.set_fontsize(15) 
        ax.set_ylim(0, max(y)+1)
        ax.set_title(r'New cases of COVID-19 per million residents', fontsize=20)
        txt = ax.text(ax.get_xlim()[1]*0.95, 2, df_expanded['date'][i], ha='right', fontsize=25)
        texts.append(txt)

    anim = FuncAnimation(fig=fig, func=update, frames=len(df_expanded), 
                         interval=100, repeat=False)
    html = anim.to_html5_video()
    with open(outfile, 'w') as f:
        f.write(html)
    print('Plot saved to {}'.format(outfile))


data_dir = '../data/'
data_file = os.path.join(data_dir, 'countries_cases_per_million.tsv')
outfile = '../images/barplot.html'
plot_bars(data_file, outfile)
