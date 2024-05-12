""" plot the generated data """
import matplotlib
matplotlib.use('Qt5Agg')  # Set the backend to Qt5Agg
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from src.data.generate import gen_data

def plot(times, heart_rates):
    fig, ax = plt.subplots(figsize=(12,8))
    label_fontsize = 11
    ax.spines[['right', 'top']].set_visible(False)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H'))
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=2))
    ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
    ax.tick_params(axis='x', labelrotation=0)
    ax.set_xlim(min(times), max(times))
    ax.set_xlabel('Hour of day', fontsize=label_fontsize)
    ax.set_ylim(min(heart_rates)-5, max(heart_rates)+5)
    ax.set_ylabel('Heart rate (BPM)', fontsize=label_fontsize)
    ax.plot(times, heart_rates, '-', label='BPM')
    ax.legend(loc=0)
    return fig, ax

if __name__ == '__main__':
    t, v = gen_data()
    plot(times=t, heart_rates=v)