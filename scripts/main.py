import json
import os

# print(json.load('data_672.json'))
directory_path = '/home/dvictoriano/Documents/data'

paths  = [ file for file in os.listdir(directory_path) if file.endswith('.json')]
# print(len(paths))

results  = []

for path in paths:
    with open(path, 'r') as file:
        data = json.load(file)
        results.extend(data['results'])


with open('data.json', 'w') as file:
    data  = {"results": results}
    json.dump(data, file, indent=4)  # 'indent' argument makes the file more readable


# file_path = 'data_672.json'
print(len(results))