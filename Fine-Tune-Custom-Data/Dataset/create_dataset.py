import json
import random


with open('data.json', 'r') as file:
    data = json.load(file)

for index, item in enumerate(data):
    item['index'] = index

random.shuffle(data)
split_ratio = 0.8
split_index = int(len(data) * split_ratio)
train_data = data[:split_index]
test_data = data[split_index:]
with open('data_train.json', 'w') as file:
    json.dump(train_data, file, indent=4)
    
with open('data_test.json', 'w') as file:
    json.dump(test_data, file, indent=4)