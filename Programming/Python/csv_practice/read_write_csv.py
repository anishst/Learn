from csv import reader, writer

# reading and writing to another file - OPTION 1

# with open('read_write_csv_INPUT.csv') as file:
# 	csv_reader = reader(file)
# 	capitalize = [[s.upper() for s in row] for row in csv_reader]
# 	for row in capitalize:
# 		print(row)

# with open('read_write_csv_OUTPUT.csv', 'w') as file:
# 	csv_writer= writer(file)
# 	for item in capitalize:
# 		csv_writer.writerow(item)

# reading and writing to another file - OPTION 2 - nest

# with open('read_write_csv_INPUT.csv') as file:
# 	csv_reader = reader(file)
# 	with open('read_write_csv_OUTPUT.csv', 'w') as file:
# 		csv_writer  = writer(file)
# 		for item in csv_reader:
# 			csv_writer.writerow([s.upper() for s in item])          


# reading and writing to another file - from a list

list_items = [3,3,4]
with open('read_write_csv_OUTPUT.csv', 'a') as file:
	csv_writer  = writer(file)
	for item in list_items:
		csv_writer.writerow(list_items) 
		# print([s.upper() for s in item])