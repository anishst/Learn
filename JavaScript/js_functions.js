// ****************************************
// simple function
// ****************************************
function sayHello(){
    console.log("Hello world! from a simple function");
}
// call function
sayHello()

// ****************************************
// simple function - return value
// ****************************************
function getGreeting(){
    return "Hello world! was returned as value";
}
// call function
console.log(getGreeting())

// ****************************************
// Arrow notation
// ****************************************
// you can omit word function
// takes a single arg
// if single expression omit curly braces and return statement

// const f1 = function() { return "hello!"}
// OR
const f1 = () => "hello from a arrow function!";
console.log(f1())
