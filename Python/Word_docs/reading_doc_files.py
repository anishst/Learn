# https://github.com/mhammond/pywin32
# https://pbpython.com/windows-com.html
#  to docx conver script: https://gist.github.com/davecoutts/a6c377d754cf97008f28
#  
#  NOT WORKING 9/25/19 TRY 
# TODO: TRY WITH pypiwin32
import os

root = os.path.dirname(os.path.realpath(__file__))
word_file = os.path.join(root, 'Test.doc')

import win32com.client as win32
word = win32.gencache.EnsureDispatch('Word.Application')
docx_file = '{0}{1}'.format(word_file, 'x')
wordDoc = word.Documents.Open(word_file, False, False, False)
# wordDoc.SaveAs2(docx_file, FileFormat = 16)
wordDoc.Close()

word.Quit()


