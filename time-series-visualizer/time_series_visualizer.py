import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)


# Clean data
df = df[
  (df.value > df.value.quantile(0.025)) &
  (df.value < df.value.quantile(0.975))
]


def draw_line_plot():
    # Draw line plot
    plt.close()
    fig, ax = plt.subplots(figsize=(16, 5))
    plt.plot(df, color="red")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy().rename(columns={"value": "Average Page Views"})
    df_bar["Years"] = [i.year for i in df_bar.index]
    df_bar["Months"] = [i.month for i in df_bar.index]
    df_bar = df_bar.sort_values(by=["Months"])
    df_bar["Months"] = [i.strftime("%B") for i in df_bar.index]
    # Draw bar plot
    plt.close()
    fig, ax = plt.subplots(figsize=(11, 10))
    sns.barplot(x="Years", y="Average Page Views", hue="Months", data=df_bar, ci=None, saturation=1, edgecolor=".2")
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
    plt.close()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 7))

    sns.boxplot(data=df_box, x="year", y="value", ax=ax1)
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")
    ax1.set_title("Year-wise Box Plot (Trend)")

    sns.boxplot(data=df_box, x="month", y="value", ax=ax2, order=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
