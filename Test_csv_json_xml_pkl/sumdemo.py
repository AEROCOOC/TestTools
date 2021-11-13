import csv
import pandas as pd
import json
import xml.etree.ElementTree as ET
import xmltodict
from dicttoxml import dicttoxml
import _pickle as cPickle


###################################################################
## CSV
###################################################################

# -------------------------OPEN CSV------------------------------ #

filename = "./Test_csv_json_xml_pkl/data.csv"   # NOCS train.csv

field = []
rows = []

with open(filename, 'r') as csvfile:

    csvreader = csv.reader(csvfile)

    # fields = csvreader.next()
    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)

for row in rows[:10]:    # 读取前五行
    print(row)

# -------------------------WRITE CSV------------------------------ #

# Field names 
fields = ['Name', 'Goals', 'Assists', 'Shots'] 

# Rows of data in the csv file 
rows = [ ['Emily', '12', '18', '112'], 
         ['Katie', '8', '24', '96'], 
         ['John', '16', '9', '101'], 
         ['Mike', '3', '14', '82']]

filename = "./Test_csv_json_xml_pkl/data.csv"

# Writing to csv file 
with open(filename, 'w+') as csvfile:         # 'w'
    # Creating a csv writer object 
    csvwriter = csv.writer(csvfile) 

    # Writing the fields 
    csvwriter.writerow(fields) 

    # Writing the data rows 
    csvwriter.writerows(rows)

# -------------------------ADD CSV------------------------------ #

# # Field names 
# fields = ['Name', 'Goals', 'Assists', 'Shots'] 

# # Rows of data in the csv file 
# rows = [ ['wow', '12', '18', '112'], 
#          ['cool', '8', '24', '96'], 
#          ['test', '16', '9', '101'], 
#          ['well', '3', '14', '82']]

# filename = "./Test_csv_json_xml_pkl/data.csv"

# # Writing to csv file 
# with open(filename, 'a+') as csvfile:       # 'a+'
#     # Creating a csv writer object 
#     csvwriter = csv.writer(csvfile) 

#     # Writing the fields 
#     # csvwriter.writerow(fields) 

#     # Writing the data rows 
#     csvwriter.writerows(rows)





###################################################################
## TRANS
###################################################################

dic_from_csv = pd.read_csv('./Test_csv_json_xml_pkl/data.csv', header=0).to_dict('records')
print(dic_from_csv)

# -------------------------DICT->JSON------------------------------ #

with open("./Test_csv_json_xml_pkl/data.json", 'w+') as json_file:
    json.dump(dic_from_csv, json_file, indent=4)

# -------------------------DICT->XML------------------------------ #

# decode the dict and convert it to str
# then write a xml file
xml_data = dicttoxml(dic_from_csv).decode()
with open("./Test_csv_json_xml_pkl/data.xml", "w+") as xml_file:
    xml_file.write(xml_data)

# -------------------------DICT->PKL------------------------------ #

with open("./Test_csv_json_xml_pkl/data.pkl", 'wb') as pkl_file:
    cPickle.dump(dic_from_csv, pkl_file)






###################################################################
## JSON
###################################################################

# -------------------------OPEN JSON------------------------------ #

# read the data from file
# we now have a python dictionary
with open('./Test_csv_json_xml_pkl/data.json') as f:
    data_listofdict = json.load(f)

# we can do the same thing with pandas
# pandas read the file, turn it to df(dataframe)
data_df = pd.read_json('./Test_csv_json_xml_pkl/data.json', orient='records')
print(data_df)

# -------------------------WRITE JSON------------------------------ #

# we can write a dictionary to json like so
# use 'indent'  and 'sort_keys' to make the json
# file look nice
with open('./Test_csv_json_xml_pkl/data.json', 'w+') as json_file:
    json.dump(data_listofdict, json_file, indent=4)

# and again the same things with pandas
exports = data_df.to_json('./Test_csv_json_xml_pkl/new_data.json', orient='records')




###################################################################
## XML
###################################################################

# -------------------------READ XML------------------------------ #

tree = ET.parse('./Test_csv_json_xml_pkl/data.xml')
xml_data = tree.getroot()

xmlstr = ET.tostring(xml_data, encoding='utf8', method='xml')

data_dict = dict(xmltodict.parse(xmlstr))

print(data_dict)

# -------------------------WRITE XML------------------------------ #

xml_data = dicttoxml(data_listofdict).decode()
with open("./Test_csv_json_xml_pkl/new_data.xml", "w+") as xml_file:
    xml_file.write(xml_data)


###################################################################
## PKL
###################################################################

# -------------------------READ PKL------------------------------ #

fr = open('./Test_csv_json_xml_pkl/data.pkl','rb')    #open的参数是pkl文件的路径
inf = cPickle.load(fr)      #读取pkl文件的内容
print(inf)

# -------------------------WRITE PKL------------------------------ #

with open("./Test_csv_json_xml_pkl/new_data.pkl", 'wb') as pkl_file:
    cPickle.dump(dic_from_csv, pkl_file)


