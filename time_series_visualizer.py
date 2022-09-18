import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig = plt.figure()
    fig.set_figwidth(15)
  
    plt.plot(df, color='red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019', fontsize=14)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Page Views', fontsize=14)
    plt.ylim([0,180000])
    plt.grid(False)




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    Months = ['January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November', 'December']

    df_bar = df.copy()
    df_bar['Months'] = df_bar.index.month_name()
    df_bar['year'] = df_bar.index.year
    df_bar = df_bar.pivot_table(
            values='value',
            index='year',
            columns='Months',
            aggfunc='mean'
        )
        
    df_bar = df_bar[Months]
   # Draw bar plot
    fig = plt.figure()
    fig = df_bar.plot(kind="bar", figsize=(10, 10)).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")



    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
     'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['month'] = pd.Categorical(df_box['month'], categories=month, ordered=True)
    df_box.sort_values('month', inplace=True)


    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(figsize=(15, 9), ncols=2, sharex=False)
    sns.despine(left=True)
    
    ax2 = sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Page Views')
    ax2.set_title('Year-wise Box Plot (Trend)')
    
    ax2 = sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    ax2.set_title('Month-wise Box Plot (Seasonality)')
      





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
