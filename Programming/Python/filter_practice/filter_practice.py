people = [{"name": "John", "id": 1}, {"name": "Anish", "id": 4}, {"name": "Sandra", "id": 2}, {"name": "Kuttan", "id": 3}]

# filter out odd ids
for person in filter(lambda i: i["id"] % 2 == 0, people):
    print(person)
