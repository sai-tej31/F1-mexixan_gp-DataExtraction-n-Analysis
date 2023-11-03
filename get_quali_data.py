import requests
from bs4 import BeautifulSoup
import lxml
from collections import defaultdict
import json


year = 2023
round = 0

quali_season = defaultdict(dict)
while round<20:
    response = requests.get(f"http://ergast.com/api/f1/{year}/{round}/qualifying")
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, features='xml')
        results = soup.find("QualifyingList")
        if results == None:
            break
        results= results.find_all('QualifyingResult')
        quali_res = defaultdict(dict)
        for res in results:
            qu2 = res.find('Driver')
            quali_res[res['position']]['driverId'] = qu2['driverId']
            quali_res[res['position']]['num'] = res['number']
            quali_res[res['position']]['name'] = res.find('GivenName').text + ' ' + res.find('FamilyName').text
            quali_res[res['position']]['qualitimes'] = {}
            q1 = res.find('Q1')
            if q1 != None:
                quali_res[res['position']]['qualitimes']['Q1'] = q1.text
            q2 = res.find('Q2')
            if q2 != None:
                quali_res[res['position']]['qualitimes']['Q2'] = q2.text
            q3 = res.find('Q3')
            if q3 != None:
                quali_res[res['position']]['qualitimes']['Q3'] = q3.text
        quali_season[round] = quali_res
        quali_season
    round += 1
with open(f'data/quali/{year}_qualifying.json', 'w') as file:
    json.dump(quali_season, file)


