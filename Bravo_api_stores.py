import requests
import json
import pandas
import xlwt
from tempfile import TemporaryFile
import openpyxl


url = 'https://bravosupermarket.az/v1/api/stores'
# api headers?

r = requests.get(url)
print(f"Status code: {r.status_code}")

response_dict = r.json()

bravo_dicts = response_dict['data']


#this loop works 
#for bravo_dict in bravo_dicts:
 #   print(bravo_dict['translations'][0]['value'])
  #  print(bravo_dict['latitude'])
   # print(bravo_dict['longitude'])

name = []
latitude = []
longitude = []

for bravo_dict in bravo_dicts:
    name.append(bravo_dict['translations'][0]['value'])
    latitude.append(bravo_dict['latitude'])
    longitude.append(bravo_dict['longitude'])


df1 = pandas.DataFrame(name)
df2 = pandas.DataFrame(latitude)
df3 = pandas.DataFrame(longitude)
df4 = pandas.concat([df1,df2,df3], axis=1)

df4.columns = ['name', 'latitude', 'longitude']

pandas.DataFrame(df4).to_excel('location_and_names.xlsx')



#exporting name, latitude, longitude to excell using xlwt
#book = xlwt.Workbook()
#sheet1 = book.add_sheet('sheet1')
#data_for_excel = name, latitude, longitude
#for i,e in enumerate(data_for_excel):
#    sheet1.write(i,1,e)
#name="xlwt_excell.xls"
#book.save(name)
#book.save(TemporaryFile())

