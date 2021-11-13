# CSV--JSON--XML--PKL

```diff
-	written by Aero
+	ref: https://github.com/LaiXiansong/learn_csv_json_xml
+	2021/11/13
```

## tips

### open()

```python
open(name[, mode[, buffering]])
```

| mode | Description                                                |
| :--- | ---------------------------------------------------------- |
| t    | 文本模式                                                   |
| x    | 写模式，如果文件已经存在则会报错                           |
| b    | 二进制                                                     |
| +    | 打开一个文件进行更新（可读可写）                           |
| U    | 通用换行模式（不推荐）                                     |
|      |  |
| r    | 以只读的方式打开文件，其指针会出现在文件的开头，为默认模式 |
| rb   | 以二进制打开文件**只读**，指针出现在开头，多用于图片。     |
| r+   | 用于读写文件                                               |
| rb+  | 二进制打开文件**读写**，一般用于图片                       |
|      |  |
| w    | 写入文件，如已存在原文件则删除原文件之中的内容。           |
| wb   | 二进制打开文件进行写入，其余同w                            |
| w+   | 读写，存在则清空                                           |
| wb+  | 二进制读写，存在则清空                                     |
|      |  |
| a    | 追加，指针放在结尾                                         |
| ab   | 二进制打开追加，指针结尾                                   |
| a+   | 打开进行追加，已存在则放在结尾，不存在则新建               |
| ab+  | 二进制打开进行追加                                         |



## csv格式

```python
import csv
```

### 读取csv格式

````python
filename = "./Test_dataFile/training.csv"   # NOCS train.csv

field = []
rows = []

with open(filename, 'r') as csvfile:

    csvreader = csv.reader(csvfile)

    # fields = csvreader.next()
    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)

for row in rows[:5]:    # 读取前五行
    print(row)
````

### 写入csv格式

```python
import csv

# Field names 
fields = ['Name', 'Goals', 'Assists', 'Shots'] 

# Rows of data in the csv file 
rows = [ ['Emily', '12', '18', '112'], 
         ['Katie', '8', '24', '96'], 
         ['John', '16', '9', '101'], 
         ['Mike', '3', '14', '82']]

filename = "./Test_dataFile/soccer.csv"

# Writing to csv file 
with open(filename, 'w+') as csvfile: 
    # Creating a csv writer object 
    csvwriter = csv.writer(csvfile) 

    # Writing the fields 
    csvwriter.writerow(fields) 

    # Writing the data rows 
    csvwriter.writerows(rows)
    
# 读取写入的csv数据
filed = []
rows = []

with open("./Test_dataFile/soccer.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    filed = next(csvfile)
    for row in csvreader:
        rows.append(row)
print(filed)
for row in rows:
    print(row)
```

## 格式转换

```python
import pandas as pd
```

### dict -> json

```python
with open("./Test_csv_json_xml_pkl/data.json", 'w+') as json_file:
    json.dump(dic_from_csv, json_file, indent=4)
```

### dict -> xml

```python
# decode the dict and convert it to str
# then write a xml file
xml_data = dicttoxml(dic_from_csv).decode()
with open("./Test_csv_json_xml_pkl/data.xml", "w+") as xml_file:
    xml_file.write(xml_data)
```

### dict -> pkl

```python
with open("./Test_csv_json_xml_pkl/data.pkl", 'wb') as pkl_file:
    cPickle.dump(dic_from_csv, pkl_file)

```



## json格式

```python
import json
import pandas as pd
```

### 读取json

```python
# read the data from file
# we now have a python dictionary
with open('./Test_csv_json_xml_pkl/data.json') as f:
    data_listofdict = json.load(f)

# we can do the same thing with pandas
# pandas read the file, turn it to df(dataframe)
data_df = pd.read_json('./Test_csv_json_xml_pkl/data.json', orient='records')
print(data_df)
```

### 写入json

```python
# we can write a dictionary to json like so
# use 'indent'  and 'sort_keys' to make the json
# file look nice
with open('./Test_csv_json_xml_pkl/data.json', 'w+') as json_file:
    json.dump(data_listofdict, json_file, indent=4)

# and again the same things with pandas
exports = data_df.to_json('./Test_csv_json_xml_pkl/new_data.json', orient='records')
```



## xml格式

```python
import xml.etree.ElementTree as ET
import xmltodict
```

### 读取xml

```python
tree = ET.parse('./Test_csv_json_xml_pkl/data.xml')
xml_data = tree.getroot()

xmlstr = ET.tostring(xml_data, encoding='utf8', method='xml')

data_dict = dict(xmltodict.parse(xmlstr))

print(data_dict)
```

### 写入xml

```python
xml_data = dicttoxml(data_listofdict).decode()
with open("./Test_csv_json_xml_pkl/new_data.xml", "w+") as xml_file:
    xml_file.write(xml_data)
```



## pkl格式

```python
import _pickle as pickle
```

### 读取pkl

```python
fr = open('./Test_csv_json_xml_pkl/data.pkl','rb')    #open的参数是pkl文件的路径
inf = cPickle.load(fr)      #读取pkl文件的内容
print(inf)
```

### 写入pkl

```python
with open("./Test_csv_json_xml_pkl/new_data.pkl", 'wb') as pkl_file:
    cPickle.dump(dic_from_csv, pkl_file)
```