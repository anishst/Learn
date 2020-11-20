const express = require('express')
// add https native lib for requests
const https = require('https')
const bodyParser = require('body-parser')
const app = express()
const port = 3000

// array to store items
let items = ["Buy Food"]

// use EJS in express app
app.set('view engine', 'ejs');

app.use(bodyParser.urlencoded({ extended: true }))
//  tell express to use files from public folder
app.use(express.static('public'))

app.get('/', (req, res) => {

    var todays = new Date()

    var options = {
        weekday: "long",
        day: "numeric",
        month: "long"
    }

    var day = new Date().toLocaleString("en-US", options)
    //  send value to list template file
    res.render("list", { kindOfDay: day, newListItems: items })
})

app.post("/", (req, res) => {

    console.log(req.body.newItem)
    //  add to array
    items.push(req.body.newItem)
    res.redirect("/");

})

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
})
