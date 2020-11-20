const express = require('express')
// add https native lib for requests
const https = require('https')
const bodyParser = require('body-parser')
// use custom date module
const date = require(__dirname + "/date.js")
console.log(date)
const app = express()
const port = 3000

// array to store items
let items = ["Buy Food"]
let workItems = []

// use EJS in express app
app.set('view engine', 'ejs');

app.use(bodyParser.urlencoded({ extended: true }))
//  tell express to use files from public folder
app.use(express.static('public'))

app.get('/', (req, res) => {

    // call the getDate from custom module
    let day = date.getDate()
    //  send value to list template file
    res.render("list", { listTitle: day, newListItems: items })
})

app.post("/", (req, res) => {

    console.log(req.body.newItem)
    let item = req.body.newItem

    // check for listTitle value from list.ejs file and write to correct array
    if (req.body.list === "Work") {
        workItems.push(item)
        res.redirect("/work")
    } else {
        items.push(item)
        res.redirect("/");
    }


})

app.get("/work", (req, res) => {
    res.render("list", { listTitle: "Work", newListItems: workItems })
})

app.get("/about", (req, res) => {
    res.render("about")
})


app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
})
