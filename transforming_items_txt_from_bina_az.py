import re

txt_filename = "Bina_az_yeni_tikili_all.txt"

opening_txt = open(txt_filename, 'r')

reading_txt = opening_txt.read()

pattern = re.compile('id.{10}')

yeni_tikili_items_list = pattern.findall(reading_txt)

final_yeni_tikili_items_list = [s.replace('id":"', '') for s in yeni_tikili_items_list]

#print(final_yeni_tikili_items_list)

with open("bina_az_yeni_tikili_all_items_id.txt", "a", encoding="utf8") as f:
        f.write(str(final_yeni_tikili_items_list))

