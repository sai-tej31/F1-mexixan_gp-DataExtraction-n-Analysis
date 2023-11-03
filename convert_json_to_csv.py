import csv
import json
from utils import convert_to_milli_seconds
def quali():
    with open('data/quali/2023_qualifying.json', 'r') as file:
        data = json.load(file)
    with open('data/output/output.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        csv_writer.writerow(["Round", "Pos", "Num","driverId", "Name", "Q1", "Q2", "Q3"])
        for round_key, positions in data.items():
            for pos_key, data_dict in positions.items():
                q1 = data_dict['qualitimes']['Q1'] if 'Q1' in data_dict['qualitimes'].keys() else None
                q2 = data_dict['qualitimes']['Q2'] if 'Q2' in data_dict['qualitimes'].keys() else None
                q3 = data_dict['qualitimes']['Q3'] if 'Q3' in data_dict['qualitimes'].keys() else None
                q1 = convert_to_milli_seconds(q1)
                q2 = convert_to_milli_seconds(q2)
                q3 = convert_to_milli_seconds(q3)
                csv_writer.writerow([round_key, pos_key, data_dict['num'], data_dict['driverId'], data_dict['name'], q1, q2, q3])



def laps():
    with open('data/laps/2023_19_laptimes.json', 'r') as file:
        data = json.load(file)
    with open('data/output/round_19_laps_output.csv', 'w', newline='') as csvfile:
        # Create a CSV writer object
        csv_writer = csv.writer(csvfile)

        # Write the header row
        csv_writer.writerow(["lap", "pos", "driver", "time"])

        # Iterate through the nested dictionary and write the data to the CSV
        for lap, lap_data in data.items():
            for pos, data_dict in lap_data.items():
                driver = data_dict["driver"]
                lap_time = convert_to_milli_seconds(data_dict["time"])
                csv_writer.writerow([lap, pos, driver, lap_time])

# laps()
quali()
