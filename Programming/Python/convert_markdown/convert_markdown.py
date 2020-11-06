# https://www.devdungeon.com/content/convert-markdown-html-python

import markdown

# Simple conversion in memory
md_text = '# Hello\n\n**Text**'
html = markdown.markdown(md_text)
print(html)

# save to html file
markdown.markdownFromFile(
    input='test.md',
    output='output.html',
    encoding='utf8',
)