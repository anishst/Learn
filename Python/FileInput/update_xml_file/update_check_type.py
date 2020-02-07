import fileinput, re
check_type = 1

xml_file = r"input_checks.xml"
new_check_type_value = 1

import re

new_file = []
with open(xml_file) as f:
	for line in f:
		match = re.search(r'<checktype>(.+?)</checktype>', line)
		if match:
			modified_line = line.replace(match.group(1), str(new_check_type_value))
			new_file.append(modified_line)
		else:
			new_file.append(line)

with open(xml_file, 'w') as f:
	for line in new_file:
		f.write(line)