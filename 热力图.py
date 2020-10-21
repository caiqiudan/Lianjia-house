import json
import requests
from openpyxl import load_workbook

def gain_location(adress):
    api_url = f'http://api.map.baidu.com/geocoding/v3/?city=西安市&address={adress}&ak=dklqhoC0zyTPuExa3I2XG1Sa5RO9n2Tw&output=json&callback=showLocation'

    r = requests.get(api_url)
    r = r.text
    r = r.strip('showLocation&&showLocation(')
    r = r.strip(')')
    jsonData = json.loads(r)
    return jsonData


wb = load_workbook(filename="西安二手房（链家）.xlsx")
ws = wb.get_sheet_by_name('热力图')
rows = ws.rows
# columns = ws.columns # 列

for row in rows:
    line = [col.value for col in row]

    if gain_location(line[0]).get('result',False):

        try:
            lng = gain_location(line[0])['result']['location']['lng']
            lat = gain_location(line[0])['result']['location']['lat']
            count = line[1]

            str_temp = '{"lat":' + str(lat) + ',"lng":' + str(lng) + ',"count":' + str(count) + '},'
            print(str_temp)
        except:
            print(line[0])

