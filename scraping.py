import requests

# for Araz stores
#response = requests.get('https://www.arazmarket.az/az/stores/')
#html = response.text

#with open("response.txt", "w", encoding="utf8") as f:
 #   print(html, file=f)

# for Bravo stores
#response2 = requests.get('https://bravosupermarket.az/v1/api/stores')
#content = response2.text 

#with open("response2.txt", "w", encoding="utf8") as f:
#    f.write(content)

# for Bazarstore stores (read comment below)
response3 = requests.get('https://www.google.com/maps/d/embed?mid=1tHYnXU2-QLxX6ngBdtOTer7fteYMDgaL&ll=40.39289756927581%2C49.86941905720734&z=12')
content2 = response3.text

with open("response3.txt", "w", encoding="utf8") as f:
    f.write(content2)
#Bazarstore map is custom, to get lattitude and longitude for stores just go to the custom map, downoal kml file.