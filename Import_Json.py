import json 

# some Json
x = '{"name": "Cong", "age": "39", "country": "Vietnam"}'
# parse x
y  = json.loads(x)
y1 = json.dumps(x)

#the result is a Python dictionary

print(y)
print(y["age"])

print("Print the y1")
print(y1)