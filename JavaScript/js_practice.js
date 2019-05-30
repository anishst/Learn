// ========================================
//          Functions
// ========================================

// function sayHello(msg) {
//     return msg;
// }
// console.log(sayHello("Hello World!"))

// ========================================
//          Arrays
// ========================================

// simple array
var simpleArray = ["test", '233']
console.log(simpleArray)

// access array 1st item
console.log(simpleArray[0])

// modify array 1st item
simpleArray[0] = 'testModified' 
console.log(simpleArray[0])

//  add to array
simpleArray.push("new1", "new2")
console.log(simpleArray)

// using pop to remove item and store in variable
var removed_item = simpleArray.pop();
console.log("This was removed: " + removed_item)
console.log(simpleArray)

// nested array
var nestedArray = [["test1", '233'], ["test2", '523'] ]
console.log(nestedArray[0][0])



