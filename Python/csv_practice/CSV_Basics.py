import csv

# example: reading file 
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader) # skip header in csv file

    for line in csv_reader:
      print (line) # print all line
      # print(line[0]) # use index to print first item


# with open('new_names.csv', 'a') as csv_file:
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerow(string)
