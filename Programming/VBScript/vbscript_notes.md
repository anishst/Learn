# VBScript

VBScript stands for Visual Basic Scripting 

- case-insensitive language
- used for scripting in HTML with IE browser, Windows, HP UFT scripting

## Resources
 - https://www.tutorialspoint.com/vbscript/index.htm

## Comments

- ``` ' This is a single quote comment ```
- ``` REM this is another comment using REM keyword ```

## Hello world app

```
<html>
   <body>
      <script language = "vbscript" type = "text/vbscript">
         document.write("Hello World!")
      </script>
   </body>
</html>

```

## Variables
- Variable Name must begin with an alphabet.
- Variable names cannot exceed 255 characters.
- Variables Should NOT contain a period (.)

```
REM declaring varialbes
Dim var1
Dim var1, var2
```

```
REM assigning values
string_value = "string value"
```

## Loops

```
REM For Loop
Dim a : a = 10
For i = 0 to a Step 2 
    document.write("The value is i is : " & i)
    document.write("<br></br>")
Next


' While wend loop
Dim a: a = 0
While a < 3:
    Msgbox(a)
    a = a + 1
wend

```

