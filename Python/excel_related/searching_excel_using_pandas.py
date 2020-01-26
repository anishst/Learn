import pandas as pd

# Assign spreadsheet filename to `file`
xls_file = 'Statistical-09262019_081550.xls'

search_values = ['Statistical Report', 'OTC Endpoint']

df = pd.read_excel(xls_file)


report_items = df.values.tolist()


for value in search_values:
    print(f"Searching for {value}")
    if value in report_items:
        print(report_items)
        print("Found it")
    else:
        print(report_items)
        print("Didn't find")
