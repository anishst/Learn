# Excel Tips


## Copy text after last separator in cell
A1: text : text : text

```=TRIM(RIGHT(SUBSTITUTE(A1,":",REPT(" ",LEN(A1))),LEN(A1)))```


## Unlock excel files

Run below command:

```taskkill /f /im excel.exe```
