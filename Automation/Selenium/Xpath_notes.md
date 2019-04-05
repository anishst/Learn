# Xpath


## Using Chrome console to practice

1. bring up developer tools
2. switch to "Console" table
3. enter xpath commands using this format: ```$x('<xpath>')```

## Inputs fields

xpath | Description
------|------------
"//input[@value='Previous']"| by value
## Tables

xpath | Description
------|------------
"//table[@class='classname']" | get table by class name attribute
"//table[@class='classname']/tbody/tr" | get all rows 
"//table[@class='classname']/tbody/tr[1]/td" | get 1st row and cells
"//td[contains(text(), 'Settlement Date:')]/following-sibling::td[last()]" | using last td based on certain text

## Code to read table

### Method 1 - writing to a csv
```
table = driver.find_element_by_xpath(table_locator)
row_count = table.find_element_by_tag_name('tr')
with open('output_file.csv', 'a', newline='') as csvfile:
    wr = csv.writer(csvfile)
    for row in table.find_elements_by_css_selector('tr'):
        wr.writerow([d.text for d in row.find_elements_by_css_selector('td')])	
```

### Method 2

```
table_locator = "//table[@class='entriesTable stripe']"
table_id = driver.find_element_by_xpath(table_locator)
table_headers = table_id.find_elements_by_tag_name('thead')
row_count = table_id.find_elements_by_tag_name('tr')
col_count = table_id.find_elements_by_xpath(table_locator + "/tbody/tr[1]/td")
print(len(row_count))	
print(len(col_count))
with open('CIRA_DETAILS.csv', 'a', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    # write table header
    for rows in table_id.find_elements_by_tag_name('thead'):
        csv_writer.writerow([th.text.strip() for th in rows.find_elements_by_css_selector('th') ])
    # write table data
    for rows in table_id.find_elements_by_css_selector('tr'):			
        csv_writer.writerow([td.text.strip() for td in rows.find_elements_by_css_selector('td') ])

```

### Method 3

```
table_id = driver.find_element_by_xpath("//table[@class='entriesTable stripe']")
rows = table_id.find_elements_by_tag_name('tr')	
data_rows = table_id.find_elements_by_xpath("//table[@class='entriesTable stripe']/tbody/tr")
cols = table_id.find_elements_by_xpath("//table[@class='entriesTable stripe']/tbody/tr[1]/td")
print(f"Total Rows {len(rows)}")
print(f"Total Data Rows: {len(data_rows)}")
print(f"Total Columns: {len(cols)}")
for row in range(1, len(rows)):
    for col in range(1, len(cols)+1):
        row_values = driver.find_element_by_xpath("//table[@class='entriesTable stripe']/tbody/tr[" + str(row ) + "]/td[" + str(col) + "]").text
        print(row_values, end="")
```
