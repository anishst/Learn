import numpy as np
import pandas as pd

HEADER = '''
<html>
    <head>
        <style>
            .df tbody tr:last-child { background-color: #FF0000; }

        </style>
    </head>
    <body>
'''
FOOTER = '''
    </body>
</html>
'''

df = pd.DataFrame({'a': np.arange(100), 'b': np.random.randn(100)})
with open('test.html', 'w') as f:
    f.write(HEADER)
    f.write(df.to_html(classes='df'))
    f.write(FOOTER)