from collections import defaultdict

def get_laps(results):
    lap = defaultdict(dict)
    for result in results:
        lap[result['position']]['driver'] = result['driverId']
        lap[result['position']]['time'] = result['time']
    return lap