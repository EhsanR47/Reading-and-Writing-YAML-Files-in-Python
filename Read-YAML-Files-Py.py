import yaml

with open(r'category_1.yaml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    category_1 = yaml.load(file, Loader=yaml.FullLoader)

    print(category_1)




with open(r'category_2.yaml') as file:
    documents = yaml.full_load(file)

    for item, doc in documents.items():
        print(item, ":", doc)