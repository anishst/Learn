const mongoose = require('mongoose');
mongoose.connect('mongodb://192.168.1.25:27017/test', { useNewUrlParser: true, useUnifiedTopology: true });



// new collection schema
const personSchema = new mongoose.Schema({
    name: String,
    address: String,
    zip: Number

})

//  new model from schema
const Person = mongoose.model('Person', personSchema)

//  create a new person collection
const person = new Person({
    name: "Anish",
    address: "123 main st",
    zip: 2333
})

//  save to collection
person.save()

const person2 = new Person({
    name: "Ligy",
    address: "123 main st",
    zip: 2333
})

//  save to collection
person2.save()

const person3 = new Person({
    name: "Tony",
    address: "123 main st",
    zip: 2333
})

const person4 = new Person({
    name: "Leah",
    address: "123 main st",
    zip: 2333
})

// inset many records at once
Person.insertMany([person3, person4], function (err) {
    if (err) {
        console.log(err)
    } else {
        console.log("Successfully save all persons")
    }
})

//  read from db a
Person.find(function (err, person) {
    if (err) {
        console.log(err)
    } else {
        console.log(person)
        // close connection
        // mongoose.connection.close()
        person.forEach(person => {
            // print only name
            console.log(person.name)
            // drop collection
        });
    }
})


// update person 

Person.updateOne({ _id: "5fb9d3d4b7870d3da810de96" }, { name: "test12121212" }, function (err) {
    if (err) {
        console.log(err)
    } else {
        console.log("Update successful")
    }
})

Person.find(function (err, person) {
    if (err) {
        console.log(err)
    } else {
        console.log(person)
        // close connection
        // mongoose.connection.close()
        person.forEach(person => {
            // print only name
            console.log(person.name)
            // drop collection
        });
    }
})


// delete item
Person.deleteOne({ _id: "5fb9d3d4b7870d3da810de96" }, function (err) {
    if (err) {
        console.log(err)
    } else {
        console.log("delete successful")
    }
})

// delete specic name
Person.deleteMany({ name: "Anish" }, function (err) {
    if (err) {
        console.log(err)
    }
    else {
        console.log("delete specic name successful")
        // mongoose.connection.close()
    }
})

// delete all
Person.deleteMany({}, function (err) {
    if (err) {
        console.log(err)
    }
    else {
        console.log("deleteMany successful")
        mongoose.connection.close()
    }
})


