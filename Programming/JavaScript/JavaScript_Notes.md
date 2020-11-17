# JavaScript

JavaScript is a scripting or programming language that allows you to implement complex things on web pages.

- https://developer.mozilla.org/en-US/docs/Web/JavaScript
### Node JS vs JavaScript

JavaScript is a programming language, which runs in web browsers. Whereas Node.js is an interpreter or running environment for JavaScript which holds a lot of requiring libraries and all. Node.js is the V8 engine bundled with some libraries to do I/O and networking, so that you can use JavaScript outside of the browser, to create shell scripts, backend services or run on hardware. https://www.quora.com/What-is-the-difference-between-JavaScript-and-Node-js

## Comments

``` var number = 5 // inline comment```

```
/* this is multi
line comment
*/ 
```

## Data Types
undefined, null, bool, string, symbol, number and object

## Output result to console

```console.log('hello world')```

## Variables

``` var myname = 'Anish'; ```

```let ourName = 'test'; ```

``` const pi = 3.14; ```

```var a=2;```

- case sensitive
- use camel case 

### assignments

```var addition = 45 + 3;```

```var subtract = 45 - 3;```

```var multiply = 45 * 3;```

```var division = 45 / 3;```

```var remainder = 45 % 3;```
### Increment Decrement

```myVar = myVar + 1;```

```myVar++;```

```myVar = myVar - 1;```

```myVar--;```

### adding/subtract/multiply shorcuts
```a = a + 12```

```a += 12```

```a = a - 12```

```a -= 12```

```a = a * 12```

```a *= 12```

```a = a / 12```

```a /= 12```

# Strings

## Escaping chars

### using backslash
```var myString = "I am \"double quoted\" string inside "\double quotes\"";```
### using single quote
```var myString = 'I am "double quoted" string inside "double quotes"';```

## String concatenate

```var myString = 'first part ' + 'second part';```

```var myString = "first part"; myString +="seond part" ```

## Find String Length

```var firstName = 'Anish';```

```var firstNameLen = 0;```

```firstNameLen = firstName.length; ```

## Find items using Index
```var firstName = 'Anish';```

```firstName[0]; // get first letter```

```firstName[firstName.length - 1]; // get last letter```

## Callback functions

A callback is a function passed as an argument to another function

https://www.w3schools.com/js/js_callback.asp

## DOM Manipulation

- ````document.querySelector("h1");```


## JQuery

jQuery is a JavaScript Library. jQuery greatly simplifies JavaScript programming.

- include jquery script tag at the end of the html doc

### Select elementSize

- js way: ```document.querySelector("h1");```
- jquery way: ```$("h1");```
```javascript

$(document).ready(function(){
  $("button").click(function(){
    $("p").slideToggle();
  });
});
```

- get font size: ```console.log($("h1").css("font-size"));```
- add class: ```console.log($("h1").addClass("big_title"));```
- remove class: ```console.log($("h1").removeClass("big_title"));```
- add element before: ```$("h1").before("<button>New</button>");```
- add element after: ```$("h1").after("<button>New</button>");```
- add element into the item selected after opening tag: ```$("h1").prepend("<button>New</button>");```
- add element into the item selected end of opening tag: ```$("h1").append("<button>New</button>");```
- remove buttons: ```$("button").remove();```
- hide ```$("h1").hide()```
- show ```$("h1").show()```
- toggle: ```$("h1").toggle()```
- fade: ```$("h1").fadeOut()```
- slide:```$("h1").slideToggle()```
- animate: ```$("h1").animate({ opacity: 1 })```

## Resources
-  https://www.quackit.com/javascript/tutorial/
- Mozilla: https://developer.mozilla.org/en-US/docs/Web/JavaScript
- Javascript Info: https://javascript.info/
- JavaScript and CSS minifier: https://www.minifier.org/
- command line: https://www.learnenough.com/command-line-tutorial/basics


## Tools

- https://hyper.is/

## Plugins for VSCode

- prettier
- emmet
- bracket pair colorizer
- javascript ES6 code snippets
- live server