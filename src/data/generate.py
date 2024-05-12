""" generate heart rate data """
from typing import Tuple, List
from datetime import datetime, timedelta

import numpy as np
import scipy.stats as ss


def gen_data() -> Tuple[List[datetime], List[float]]:
    np.random.seed(222)

    start_datetime = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

    n = 24 * 12  # data points every 5 minutes

    times = [start_datetime + timedelta(minutes=5 * i) for i in range(n)]

    base_heart_rate = 65  # bpm

    activities = [
        # how far into day, std, peak height above base, slant
        {'when': 0.00 * n, 'duration': 17, 'size': 3, 'skew': -2},
        {'when': 0.25 * n, 'duration': 15, 'size': 10, 'skew': -4},
        {'when': 0.30 * n, 'duration': 5,  'size': 50, 'skew': 4},
        {'when': 0.50 * n, 'duration': 3,  'size': 25, 'skew': 4},
        {'when': 0.50 * n, 'duration': 15, 'size': 10, 'skew': 2},
        {'when': 0.70 * n, 'duration': 2,  'size': 70, 'skew': 2},
        {'when': 0.70 * n, 'duration': 15, 'size': 10, 'skew': 2},
        {'when': 0.80 * n, 'duration': 25, 'size': 10, 'skew': -2}

    ]

    heart_rates = [base_heart_rate + np.random.uniform(low=0, high=3) for i in range(n)]

    for activity in activities:
        skewed_distribution = ss.skewnorm(a=4, loc=activity['when'], scale=activity['duration'])
        heart_rates_activity = [skewed_distribution.pdf(i) for i in range(n)]
        heart_rates_activity /= max(heart_rates_activity)  # normalise between 0 and 1
        heart_rates_activity *= activity['size']  # rescale between 0 and size
        heart_rates = [x + y for x, y in zip(heart_rates, heart_rates_activity)]

    return times, heart_rates
