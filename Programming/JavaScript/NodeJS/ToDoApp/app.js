const express = require('express')
// add https native lib for requests
const https = require('https')
const bodyParser = require('body-parser')
const app = express()
const port = 3000

// use EJS in express app
app.set('view engine', 'ejs');

app.get('/', (req, res) => {

    var todays = new Date()

    var options = {
        weekday: "long",
        day: "numeric",
        month: "long"
    }

    var day = new Date().toLocaleString("en-US", options)
    //  send value to list template file
    res.render("list", {
        kindOfDay: day
    })
})



app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
})
