import datetime
Results = []

Results.append(['test1','fail', "error reason"])
Results.append(['test2', 'Pass'])
Results.append(['test6', 'Pass'])
Results.append(['test3', 'Pass'])

f = open('helloworld.html','w')
message = f"""<html>
<head><title>Test</title>
</head>
<body>
"""

dt = f"""<h1>Stability Run - Test Results</h1><strong>Run Date: </strong>{datetime.datetime.now()}
<br/>Number of Tests: {len(Results)} <br/>
<hr noshade/>
<table>
"""

# testInfo = ""
for i in Results:
	if (i[1].lower() == 'pass'):
		dt  = dt + f"<tr><td>{str(i[0])}</td><td>{str(i[1]).title()}</td></tr>"
		print(dt)
	else:
		dt = dt + f"<tr><td>{str(i[0])}</td><td>{str(i[1]).title()}</td></tr>"
		print(dt)

message = message + dt  + "</table></body></html>"
print(message)
f.write(message)
f.close()		

# # Open results
import webbrowser
webbrowser.open_new_tab('helloworld.html')
