from bs4 import BeautifulSoup
import maps
import csv

folder = './sources_example/'

keys = ['id', 'pers_num', 'gp_name', 'team', 'pos', 'time', 'year', 'round', 'pilot', 'code', 'circuit', 'color', 'lon', 'lat']
id = 0

f = open('f1.csv', 'wb')
writer = csv.DictWriter(f, keys)
writer.writeheader()


def extract_data(page):
    global id
    soup = BeautifulSoup(page, "lxml")

    data = {}

    h1 = soup.body.h1.a.text
    h1_data = h1.split(' ')
    data['year'] = h1_data[0].encode('UTF-8')
    data['round'] = h1_data[1][5:].encode('UTF-8')
    data['gp_name'] = ' '.join(h1_data[4:]).strip(' \n').encode('UTF-8')
    data['code'] = maps.code_map[data['gp_name']]

    if data['code'] == 'EUR':
        data['code'] = maps.eur_code[data['year']]

    race = soup.body.find('h2', text='\nRace Information\n')
    data['circuit'] = race.findNext('table').findAll('tr')[1].findAll('td')[1].text.encode('UTF-8')
    data['lon'] = maps.circuts[data['circuit']][0]
    data['lat'] = maps.circuts[data['circuit']][1]

    final = soup.body.find('h2', text='\nFinal\n')
    table = final.findNext('table')
    for tr in table.findAll('tr'):
        if tr.has_attr('class') and ('head' in tr.attrs['class']):
            continue
        tds = tr.findAll('td')
        data['id'] = id
        id += 1
        data['pos'] = tds[0].text.encode('UTF-8')
        data['pers_num'] = tds[1].text.encode('UTF-8')
        data['pilot'] = tds[2].a.text.encode('UTF-8')
        data['team'] = tds[3].a.text.encode('UTF-8')
        data['time'] = tds[4].text.encode('UTF-8')
        data['color'] = maps.team_color[data['team']] if data['pos'] == '1' else '#ffffff'

        writer.writerow(data)


for i in range(1, 6):
    with open(folder + str(i) + '.html', 'r') as html:
        extract_data(html)
    print i


f.close()
