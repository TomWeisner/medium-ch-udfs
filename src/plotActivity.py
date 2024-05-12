""" overlay the generated data plot with identified periods of activity """
from datetime import datetime

import numpy as np

from src.data.generate import gen_data
from src.clickhouse.user_scripts.findActivity import find_activity
from src.data.plotGenerate import plot


if __name__ == '__main__':
    times, heart_rates = gen_data()
    activity_indexes, activity_times = find_activity(times, heart_rates)
    fig, ax = plot(times, heart_rates)
    for i, a in enumerate(activity_indexes):
        peak = a[-1]
        Y = heart_rates[peak]
        X = [times[a[0]], times[a[1]]]
        ax.plot(times[peak], heart_rates[peak], 'rx', markersize=10, label='Peak' if i == 0 else '')  # only one label
        ax.fill_between(X, Y, 60, alpha=0.3, color='green', label='Activity' if i == 0 else '')

        avg_activity_time = datetime.fromtimestamp(np.mean([dt.timestamp() for dt in X]))
        activity_time_range_str = f"{X[0].strftime('%H:%M')}-{X[1].strftime('%H:%M')}"
        ax.text(avg_activity_time, Y+3, activity_time_range_str, ha='center', fontsize=11)
    ax.legend()
    #plt.savefig(f'src/figures/heart_rate_{datetime.now().strftime("%Y%m%d")}.png')
