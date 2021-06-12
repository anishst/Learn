# Selenium Selectors

# Xpath


### Basic Syntax
- / start at root of DOM
- // look anywhere in dom
- ```*``` any tag
- ```//tagname[@attribute='Value']```
- ```//tagname[@attribute='Value'][@attribute='Value']```

## Absolute vs Relative

### Absolute
- direct way to locate; using single slash "/" means start at root
- not recommended as changes in page structure will break xpath

### Relative
- starts from midddle of DOM
- Starts with a double slash “//” that means it can start to search anywhere in the DOM structure

## Using Chrome console to practice

1. bring up developer tools
2. switch to "Console" table
3. enter xpath commands using this format: ```$x('<xpath>')```

## Wilcard usage

- ```//*[@*='content']``` - find any element with any attribute value of 'content'
## Text
- ```//tag[text()=‘value‘]```
- ```//tag[contains(text(), ‘partialvalue‘)]```

## Contains

- syntax: ```//tag[contains(@attribute, ‘value‘)]```

Examples:

```"//td[contains(text(), 'Google')]"```

``` //input[contains(@id, ‘search')]```

## Finding Parent/siblings
- ```"//tagname[@attribute, ‘value‘]/.."```
- ```"//tagname[@attribute, ‘value‘]/parent::tagname"```
- ```"//tagname[@attribute, ‘value‘]/following-sibling::tagname"```
- ```"//tagname[@attribute, ‘value‘]/preceding-sibling::tagname"```
-  using index:```"//tagname[@attribute, ‘value‘]/preceding-sibling::tagname[1]"```
- ```//div[@id='someid']//a``` - find all links under the div tag
- ```//div[@id='someid']/a``` - find all children links under the div tag

## Position and Index

- ```//a[@href="#edit"][1]``` - get first link using index
- ```//a[@href="#edit"][position()=3]``` - get 3rd link using position
- ```//a[@href="#edit"][last()]``` - get last link 
- ```//a[@href="#edit"][last()-2 ]``` - get 2nd to last link 
- ```//a[@href="#edit"][position()<3]``` - get  position less than 3
## Starts-with

- checks the starting text of an attribute.
- Syntax: ```//tag[starts-with(@attribute, ‘value‘)]```

Examples:

```"//td[contains(text(), 'Google')]"```

``` //input[contains(@id, ‘search')]```
## Inputs fields

xpath | Description
------|------------
"//input[@value='Previous']"| by value

## Chaining Declarations

- chain multiple relative XPath declarations with “//” double slash

```//div[@class=’form-group’]//input[@id=’user-message’]```

## OR and AND


```//*[@id=’user-message’ or @class=’form-control’]```

```//*[@id=’user-message’ and @class=’form-control’]```

```td.text.strip() for td in rows.find_elements_by_xpath("td[" + str(col_number) + "]") or rows.find_elements_by_xpath("th[" + str(col_number) + "]")```

Using | symbol:
```driver.find_elements_by_xpath("//table[@id='customers']/tbody/tr[1]/th|//table[@id='customers']/tbody/tr[1]/td"))```

## Text

- text of an element
- syntax: ```//tag[text()=’text value‘]```

Examples:

- ```//label[text()=’Enter message’]```

## Finding items based on text on page

```
//text()[contains(., '<search text>')]/following::span/input[@type='checkbox']
```
```
"//li[text()[contains(.,'Terminal Configuration')]]/ul/li[contains(.,'Modify')]"
```
## Diff between following and following-sibiling

the following axis contains all nodes in the same document as the context node that are after the context node in document order, excluding any descendants and excluding attribute nodes and namespace nodes

the following-sibling axis contains all the following siblings of the context node; if the context node is an attribute node or namespace node, the following-sibling axis is empty


## Dynamic Values

xpath | Description
------|------------
```input[starts-with(@id,'ctrl')]```|  starts with ctrl|
```input[ends-with(@id,'_userName')]```| ends with _userName|
```Input[contains(@id,'userName')]```|contains

## Tables

xpath | Description
------|------------
"//table[@class='classname']" | get table by class name attribute
"//table[@class='classname']/tbody/tr" | get all rows 
"//table[@class='classname']/tbody/tr[1]/td" | get 1st row and cells
"//td[contains(text(), 'Google')]" | using contains
"//td[contains(text(), 'Settlement Date:')]/following-sibling::td[last()]" | using last td based on certain text
"//td[contains(text(), 'OTCnet (External)')]/preceding-sibling::td/div/input[@type='checkbox']" | using preceding
"//table[@class='entriesTable stripe']//a" | find all link tags within a table
"/descendant::table[@class='reviewTable stripe'][4]" | find using table class


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


# find value by attribute
```python
elms = driver.find_elements_by_xpath("//li")
for elm in elms:
    print(elm.get_attribute("href"))
    print(elm.text)

print(" ==============================================")
elms = driver.find_elements_by_xpath("//*")
for elm in elms:
    print(elm.get_attribute("id"))
```

## Add-ons for xpath

- chropath for google chrome/firefox
## Resources

- https://www.swtestacademy.com/xpath-selenium/

# CSS Selectors

## Using Chrome console to practice

1. bring up developer tools
2. switch to "Console" table
3. enter xpath commands using this format: ```$$('<css selector>')```

```$$("input[type='text")```

### Syntax

- basic : ```input[type='text']```
- concatenation: ```input[type='text'][id='someid']```
- starts with ```input[id^='text']```
- ends with ```input[id$='text']```
- contains ```input[id*='text']```
- by id ```#<idname>```
- by id of specific element```input#<idname>```
- tagname ``tagname``
- class name ```.<classname>```
- class name specific element```div.<classname>```
- class with mutliples classes; add . after each class```.<classname.<classname>.....```
- first child: ```div.<classname> > div > div:first-child```
- last child: ```div.<classname> > div > div:last-child```
- nth  child: ```div.<classname> > div > div:nth-child(<number>)```

code examples: 
`````"div[class='searchformwrapper'] > form > input[type='submit']"`````