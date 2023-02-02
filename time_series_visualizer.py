import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

dates = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) &
(df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot

    plot = df.plot(kind='line', figsize=(15,8), title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019', ylabel='Page Views', xlabel='Date')

    fig = plot.get_figure()




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['month'] = df_bar.index.month
    df_bar['year'] = df_bar.index.year
    print(df_bar['month'])
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean()
    df_bar = df_bar.unstack()
    # Draw bar plot


    fig = df_bar.plot.bar(legend=True, figsize= (10,5), ylabel='Average Page Views', xlabel='Years').figure
    plt.legend(dates)



    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, sharey=True, figsize=(12,6))
    sns.boxplot(ax=axes[0], x=df_box.year, y=df_box.value)
    sns.boxplot(ax=axes[1], x=df_box.month, y=df_box.value, order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

    axes[0].set(title='Year-wise Box Plot (Trend)', xlabel='Year', ylabel='Page Views')
    axes[1].set(title='Month-wise Box Plot (Seasonality)', xlabel='Month', ylabel='Page Views')


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
