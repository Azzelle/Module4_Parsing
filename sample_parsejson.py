import json
import yaml

#Example of json
x = '{"name": "Azzelle Leira Rodil", "age" : "22", "city" : "Quezon City"}'

#Parse Json
y = json.loads(x)
print("The output of json file is", y)
print("Age: ", y['age'])
print("Name: ", y['name'])
print("City: ", y['city'])