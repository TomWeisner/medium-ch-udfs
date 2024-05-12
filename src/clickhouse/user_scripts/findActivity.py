#!/usr/bin/python3
import sys
import json

from datetime import datetime
from typing import List, Tuple

import numpy as np
from scipy.signal import find_peaks, peak_widths


def find_activity(dts: List[datetime], y: List[float]) -> Tuple[List[List[int]], List[List[str]]]:
    """ main method for finding elevated heart activity """
    y = np.array(y)
    peaks, x = find_peaks(y, height=25, distance=2, prominence=5)
    peaks_rev, x = find_peaks(-y, distance=2, prominence=1)
    widths = peak_widths(y, peaks, rel_height=1000)

    left = np.array([np.floor(x) for x in widths[2]]).astype(int)
    right = np.array([np.floor(x) for x in widths[3]]).astype(int)

    pairs = list(list(a) for a in zip(left, right))
    peaks = peaks.tolist()

    for i, p in enumerate(pairs):
        left = p[0]
        if i > 0 and (p[0] < [pairs[x][1] for x in range(0, i)]).any():
            left = max([pr for pr in peaks_rev if pr <= peaks[i]])
        right = peaks[i]
        pairs[i] = [left, right]

    all_positions, all_times = [], []
    for i, p in enumerate(pairs):
        if p is None:
            continue
        l, r = pairs[i][0], peaks[i]
        position = [l, r]
        all_positions.append(position)
        l_time = dts[l]
        r_time = dts[r]
        times = [l_time, r_time]
        all_times.append([t.strftime('%Y-%m-%d %H:%M:%S') for t in times])

    return all_positions, all_times


if __name__ == '__main__':
    for line in sys.stdin:
        inputs = json.loads(line)

        values = inputs['values']
        dates = [datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in inputs['readingDates']]

        try:
            _, r = find_activity(dates, values)
        except:
            r = [[]]

        result = json.dumps({'result': r})
        print(result, end='\n')
        sys.stdout.flush()
