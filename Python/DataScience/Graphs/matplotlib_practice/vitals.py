# https://www.youtube.com/watch?v=UO98lJQ3QGI&list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_

from matplotlib import pyplot as plt
import pandas as pd

def plot_height():

    plt.xkcd()

    df = pd.read_csv('vitals.csv')
    #  set style
    plt.style.use('seaborn')

    dates_x = df['Date']

    tony_h = df['tony_height']
    plt.plot(dates_x, tony_h, label='Tony', marker="o")

    leah_h = df['leah_height']
    plt.plot(dates_x, leah_h, label='Leah', marker="o")


    plt.xlabel('Date')
    plt.ylabel('Height')
    plt.title('Height History')

    plt.legend()

    plt.tight_layout()

    plt.savefig('height_plot.png')

    plt.show()

def plot_weight():

    plt.xkcd()

    df = pd.read_csv('vitals.csv')
    #  set style
    plt.style.use('seaborn')

    dates_x = df['Date']

    tony_h = df['tony_weight']
    plt.plot(dates_x, tony_h, label='Tony', marker="o")

    leah_h = df['leah_weight']
    plt.plot(dates_x, leah_h, label='Leah', marker="o")


    plt.xlabel('Date')
    plt.ylabel('Weight in pounds')
    plt.title('Weight History')

    plt.legend()

    plt.tight_layout()

    plt.savefig('weight_plot.png')

    plt.show()

# plot_height()
plot_weight()