# https://docs.python.org/3.7/library/unicodedata.html
import unicodedata

for i in range(1,5):
    print(chr(i))
    # print(unicodedata.decimal(chr(i)))
    print(unicodedata.normalize('NFC', (chr(i))))



#  look up examples
print(unicodedata.lookup('RIGHT CURLY BRACKET')	)

#  FIND MALAYALAM WORDS = https://www.unicode.org/charts/PDF/U0D00.pdf
print(unicodedata.lookup('MALAYALAM LETTER A')	)
print(unicodedata.lookup('MALAYALAM LETTER NA')	)
print(unicodedata.lookup('MALAYALAM VOWEL SIGN I')	)
print(unicodedata.lookup('MALAYALAM LETTER SSA'),unicodedata.lookup('MALAYALAM SIGN VIRAMA')	)
print(unicodedata.lookup('MALAYALAM SIGN VIRAMA')	)

