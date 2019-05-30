// ========================================
//          Functions
// ========================================

// function sayHello(msg) {
//     return msg;
// }
// console.log(sayHello("Hello World!"))

// ========================================
//          If Else
// ========================================
// val = 5
// if (val >= 5) {
//     console.log("Value is greater than 5")
// }

// else {
//         console.log("Value is less than 5")
// }
// ========================================
//          If Else If
// ========================================
// val = 5
// if (val < 5) {
//     console.log("Value is less than 5")
// }
// else if (val > 5) {
//     console.log("Value is greater than 5")
// }
// else {
//     console.log("Value equal to 5")
// }
// ========================================
//          Switch Statement
// ========================================
//  EXAMPLE 1
// val = 0
// switch (val) {
//     case 1:
//         console.log("You Chose Option 1")
//         break;
//     case 2:
//         console.log("You Chose Option 2")
//         break;

//     case 3:
//         console.log("You Chose Option 3")
//         break;
//     default:
//         console.log("Please Chose Option")
//         break;
// }

// EXAMPLE 2
// val = 6
// switch (val) {
//     case 1:
//     case 2:
//     case 3:
//         console.log("Your value is between 1 and 3")
//         break;
//     case 4:
//     case 5:
//     case 6:
//         console.log("Your value is between 4 and 6")
//         break;        
//     default:
//         console.log("Invalid Value")
//         break;
// }
// ========================================
//          Scope
// ========================================
// var myGlobalVar = 5

// function checkScope() {
//     console.log(myGlobalVar);
// }
// console.log(myGlobalVar)
// checkScope()

// ========================================
//          Comparison Operators
// ========================================

// function testEqual(val) {
//     if (val == 12){
//         return 'Equal'
//     }
//     return 'Not Equal'
// }
// console.log(testEqual(12))

//  strict equal using ===; this does not perform type conversion
// function strictEqual(val) {
//     if (val === 12) {
//         return 'Equal'
//     }
//     return 'Not Equal'
// }
// console.log(strictEqual(12))
// console.log(strictEqual('12'))


// function notEqual(val) {
//     if (val != 12) {
//         return 'Not Equal'
//     }
//     return 'Equal'
// }
// console.log(notEqual(13))

// function testLogicalANDOR(val) {
//     if (val >=40 && val <=60){
//         console.log("Met logical AND expression")
//     }

//     if (val >= 40 || val <=60) {
//         console.log("Met logical OR expression")
//     }
// }
// testLogicalANDOR(353)

// ========================================
//          Arrays
// ========================================

// // simple array
// var simpleArray = ["test", '233']
// console.log(simpleArray)

// // access array 1st item
// console.log(simpleArray[0])

// // modify array 1st item
// simpleArray[0] = 'testModified' 
// console.log(simpleArray[0])

// //  add to end of array using push
// simpleArray.push("new1", "new2")
// console.log(simpleArray)

// //  add to beginning of array using unshift
// simpleArray.unshift("3", "4")
// console.log(simpleArray)

// // using pop to remove item and store in variable
// var removed_item = simpleArray.pop();
// console.log("This was removed using pop: " + removed_item)
// console.log(simpleArray)

// // using shift 
// var removed_item = simpleArray.shift();
// console.log("This was removed using shift: " + removed_item)
// console.log(simpleArray)

// // nested array
// var nestedArray = [["test1", '233'], ["test2", '523'] ]
// console.log(nestedArray[0][0])


// ========================================
//         JS Objects
// ========================================

// creating an object
var carObj = {
    "name": "Pilot",
    "tires": 4,
    "color of car": "blue"
};

// accessing object property
var nameValue = carObj.name  // access name of car using . notation
var colorValue = carObj["color of car"] //access color using [] notation; required if value has spaces
console.log(nameValue, colorValue)

// using variable
var nameValue = 'name'
console.log(carObj[nameValue])

// update object properities
carObj.name = "Honda Pilot"
console.log(carObj.name)

// add new property
carObj['make'] = 'Honda'
console.log(carObj)

// delete property
delete carObj.make
console.log(carObj)

// lookup example using object
var lookup = {
        1: "cool",
        2: "sad",
        3: "angry"
}
console.log(lookup[1])

// check if object has a property
console.log(lookup.hasOwnProperty(7))


// nested objects

