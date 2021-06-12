from selenium import webdriver
from selenium.webdriver.common.by import By

import time
driver = webdriver.Chrome()
driver.get('https://www.w3schools.com/html/html_tables.asp')

# locate the table
table_id = driver.find_element_by_xpath("//table[@id='customers']")

# print entire table - WORKING
# print(table_id.text)

# find row count using tr tag - method 1 - WORKING
rows = table_id.find_elements(By.TAG_NAME, 'tr')
print(len(rows))

# print row text easy way - WORKING
# rows = table_id.find_elements(By.TAG_NAME, 'tr')
# print(len(rows))
# for row in rows:
# 	print(row.text)

# find row count using tr tag - method 2 - WORKING
# row_count = len(driver.find_elements_by_xpath("//table[@id='customers']/tbody/tr"))
# print(row_count)
# col_count = len(driver.find_elements_by_xpath("//table[@id='customers']/tbody/tr[1]/th"))
# print(row_count, col_count)


# find row and column count using tr tag - method 3 - WORKING
# row_count = len(driver.find_elements_by_xpath("//table[@id='customers']/*/tr"))
# print(row_count)
# col_count = len(driver.find_elements_by_xpath("//table[@id='customers']/*/tr[1]/th"))
# print(col_count)


# col_count_new = len(driver.find_elements_by_xpath("//table[@id='customers']/tbody/tr[1]/th|//table[@id='customers']/tbody/tr[1]/td"))
# print(col_count_new)

# find row data using row number - method 1 WORKING
# row_number = 7
# for rows in driver.find_elements_by_xpath("//table[@id='customers']/tbody/tr[" + str(row_number) + "]"):
#     print([td.text.strip() for td in rows.find_elements_by_xpath('td')])

# find row data using row number - method 2 WORKING
# row_number = 7
# rows = table_id.find_elements(By.TAG_NAME, 'tr')
# for row in range(0, len(rows)):
# 	if row == row_number - 1:
# 		print(rows[row].text)
# 		break


# find row data using row number - method 3 WORKING - 
# row_number = 2
# for rows in driver.find_elements_by_xpath("//table[@id='customers']/*/tr[" + str(row_number) + "]"):
#     print([td.text.strip() for td in rows.find_elements_by_xpath('td') or 
#     								rows.find_elements_by_xpath('th')])


# find row data using row number - method 4 WORKING -
# row_number = 1
# rows = table_id.find_elements(By.XPATH, ".//tr[" + str(row_number) + "]")
# for row in rows:
# 	cells = row.find_elements(By.XPATH, ".//*[local-name(.)='th' or local-name(.)='td']")
# 	print([cell.text for cell in cells])

# find row data using row number - method 4 WORKING
# row_number = 7
# row_count = len(driver.find_elements_by_xpath("//table[@id='customers']/*/tr"))
# print(row_count)
# rows = table_id.find_elements(By.XPATH, ".//tr")
# print(rows[row_number-1].text)
# for row in range(0, row_count):
# 	print(rows[row].text)

# col_count = len(driver.find_elements_by_xpath("//table[@id='customers']/*/tr[1]/th"))
# print(col_count)

# find column data using col number - method 1 WORKING
col_number = 3
col_data = []
for rows in driver.find_elements_by_xpath("//table[@id='customers']/*/tr"):
    data = [td.text.strip() for td in rows.find_elements_by_xpath("td[" + str(col_number) + "]") or 
    								rows.find_elements_by_xpath("th[" + str(col_number) + "]")]
    for item in data:
    	col_data.append(item)

print(col_data)


# find col data using col number - method 2 WORKING -
# col_number = 3
# col_data = []
# rows = table_id.find_elements(By.XPATH, ".//tr")
# for row in rows:
# 	cells = row.find_elements(By.XPATH, ".//*[local-name(.)='th' or local-name(.)='td'][" + str(col_number) + "]")
# 	for cell in cells:
# 		col_data.append(cell.text)

# print(col_data)
# # print all data - WORKING

# for row in rows:
# 	cols = row.find_elements(By.TAG_NAME, 'td')
# 	for col in cols:
# 		print(col.text)
# 	print("-"*50)


# print specific row
# rows = table_id.find_elements(By.TAG_NAME, 'tr')
# print(rows[5].text)


# # # print all data - working
# print([row.text for row in rows])

# print all data using each cell - working
# file_name = 'my_output.csv'
# import csv
# with open(file_name, 'w', newline='') as csvfile:
# 	csv_writer = csv.writer(csvfile)
# 	for rows in table_id.find_elements_by_css_selector('tr'):
# 		csv_writer.writerow([td.text for td in rows.find_elements(By.XPATH, ".//*[local-name(.)='th' or local-name(.)='td']")])

# time.sleep(3)
driver.quit()

