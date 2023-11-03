import requests
from bs4 import BeautifulSoup
import lxml
from collections import defaultdict
from get_lap_timings import get_laps
import json


laps = defaultdict(lambda : defaultdict(dict))

year = 2023
round = 18
lap_num = 0
for round in range(0,20):
    while True:
        response = requests.get(f'http://ergast.com/api/f1/{year}/{round}/laps/{lap_num}')
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, features='xml')
            results = soup.find("LapsList")
            if results == None:
                break
            results= results.find_all("Timing")
            laps[results[0]['lap']] = get_laps(results)

            
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
        lap_num += 1


    with open(f'data/laps/{year}_{round}_laptimes.json', 'w') as file:
        json.dump(laps, file)


