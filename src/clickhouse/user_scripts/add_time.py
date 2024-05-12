#!/usr/bin/python3

import sys
import json
from datetime import datetime, timedelta


def add_time(x: float, unit: str, date: datetime) -> str:
    valid_units = ['minutes', 'hours']
    try:
        assert unit in valid_units
    except:
        return f"Unimplemented time unit '{unit}'.\nValid units are: {valid_units}"

    if unit == 'minutes':
        new_date = date + timedelta(minutes=x)
    else:
        new_date = date + timedelta(hours=x)
    return new_date.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == '__main__':
    for line in sys.stdin:
        value = json.loads(line)  # convert input to json string dict
        num = float(value['number'])  # cast string as number
        unit = value['time_unit']  # no cast needed as already string
        # DateTime64 from CH but json.loads casts all vals as str
        # convert the string to a datetime
        date = datetime.strptime(value['date'], "%Y-%m-%d %H:%M:%S")
        # json.dumps converts all vals back to strings (if possible)
        result = json.dumps({'result': add_time(num, unit, date)})
        print(result, end='\n')
        sys.stdout.flush()