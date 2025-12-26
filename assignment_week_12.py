def analyze_traffic_flow(filename):
    totals = {}
    congested_streets = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip().split(',')
            if len(line)!= 4:
                continue
            street, district, cars, trucks = line
            try:
                cars = int(cars)
                trucks = int(trucks)
            except ValueError:
                continue
            total_volume = cars + trucks
            if district in totals:
                totals[district]+=total_volume
            else:
                totals[district] = total_volume
            if total_volume> 500:
                congested_streets.append((street, total_volume))

    return totals, congested_streets


def write_traffic_report(district_totals, congested_streets):
    with open('traffic_report.txt', 'w') as file1:
        file1.write('DISTRICT TRAFFIC VOLUME\n')
        file1.write('-'*23 )
        for district, total in district_totals.items():
            file1.write(f'\n{district}: {total}')
        file1.write('\n')
        file1.write('\nCONGESTED STREETS (> 500 vehicles)\n')
        file1.write('-'*34)
        file1.write('\n')
        for street, volume in congested_streets:
            file1.write(f'{street} ({volume} vehicles)\n')


district_totals, congested_streets = analyze_traffic_flow('traffic_survey.txt')
write_traffic_report(district_totals, congested_streets)