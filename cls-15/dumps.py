import json
data = '{"name": "Alice", "age": 25}'
py_obj = json.loads(data)  
print(py_obj)
# {'name': 'Alice', 'age': 25}
json_str=json.dumps(py_obj,indent=2)
print(json_str)
