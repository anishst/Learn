// ****************************************
// simple function
// ****************************************
function sayHello() {
    console.log("Hello world! from a simple function");
}
// call function
sayHello()

// ****************************************
// simple function - return value
// ****************************************
function getGreeting() {
    return "Hello world! was returned as value";
}
// call function
console.log(getGreeting())

// ****************************************
// Arrow Functions
// ****************************************
// you can omit word function
// takes a single arg
// if single expression omit curly braces and return statement

// const f1 = function() { return "hello!"}
// OR
const f1 = () => "hello from a arrow function!";
console.log(f1())

const years = [1999, 1965, 1937, 1979, 2001]

// ES5 using map

var ages5 = years.map(function (el) {
    return 2016 - el
});
console.log(ages5);

// ES6 arrow callback function
let ages6 = years.map(el => 2016 - el)
console.log(ages6);

//  access element and index - one line
ages6 = years.map((el, index) => `Age elment ${index + 1}: ${2016 - el}.`);
console.log(ages6);

//  access element and index - more than one line require curly braces
ages6 = years.map((el, index) => {
    const now = new Date().getFullYear();
    const age = now - el;
    return `Age element ${index + 1}: ${age}`;
});
console.log(ages6);

