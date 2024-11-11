import json
with open('new_test_hw.json', 'r', encoding='UTF-8') as file:
    json_data = json.load(file)
print(json_data)
def find_companies(data):
    companies = []
    if isinstance(data, list):
        for item in data:
            companies.extend(find_companies(item))
    elif isinstance(data, dict):
         if 'id' in data and 'title' in data:
                companies.append(str(data['id']) + "," + str(data['title']))
                for value in data.values():
                    companies.extend(find_companies(value))
    return companies
result = find_companies(json_data)

