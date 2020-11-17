const express = require('express')
const app = express()
const port = 3000

// callback function with arrow
app.get('/', (req, res) => {
    res.send('<h1>Hello World! - NodeJS</h1>')
})


app.get('/about', (req, res) => {
    res.send('<h1>NodeJS App by Anish</h1>')
})

// non-arrow way
app.get('/callback', function (req, res) {
    res.send('This is using callback function')
})

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
})