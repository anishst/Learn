import datetime
Results = []

Results.append(['test1','fail', "error reason"])
Results.append(['test2', 'Pass'])
f = open('helloworld.html','w')
message = """<html>
<head><title>Test</title>
<style>
/*Source: https://fonts.google.com/*/
@import url('https://fonts.googleapis.com/css?family=Tangerine');
@import url('https://fonts.googleapis.com/css?family=Baloo+Bhaina|Magra');
@import url('https://fonts.googleapis.com/css?family=Rancho');
body {
margin:15;
font-family: 'Magra', sans-serif;
font-size: 25px;
}
h1 {
	color: gray;
}
tab1 { padding-left: 4em; }
</style>

</head>
<body>
"""

dt = """<h1>Stability Run - Test Results</h1><strong>Run Date: </strong>{}
<br/>Number of Tests: {} <br/>
<hr noshade/>""".format(datetime.datetime.now(),len(Results))
testInfo = ""
for i in Results:
	if (i[1].lower() == 'pass'):
		testInfo = testInfo + str(i[0]) + "&nbsp;&nbsp;&nbsp;&nbsp;<b>" + str(i[1]).title() + "</b>&nbsp;&nbsp;&nbsp;&nbsp;<br/>"
	else:
		testInfo = testInfo + str(i[0]) + " &nbsp;&nbsp;&nbsp;&nbsp;<i>" + str(i[1]).title() + "&nbsp;&nbsp;&nbsp;&nbsp;" + str(i[2]) + "</i>&nbsp;&nbsp;&nbsp;&nbsp;<br/>"
message = message + dt + testInfo + "</body></html>"
f.write(message)
f.close()		

# # Open results
import webbrowser
webbrowser.open_new_tab('helloworld.html')
