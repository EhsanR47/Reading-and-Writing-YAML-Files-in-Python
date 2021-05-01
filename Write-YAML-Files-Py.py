import yaml

dict_file = [{'countries' : ['Iran', 'USA', 'Germany', 'France', 'Italy']}
    ,{'sports' : ['tennis','soccer', 'football', 'basketball']}]

with open(r'category_3.yaml', 'w') as file:
    documents = yaml.dump(dict_file, file)