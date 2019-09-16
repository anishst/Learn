// EXAMPLE OF A WEB APP USING EXPRESS FRAMEWORK

//  load express module
const express = require('express')


// create instance of app
const app = express();

// see https://expressjs.com/en/4x/api.html#req for all request options

//  define root route
app.get('/', (req, res) => {
    console.log(`rcvd request from ${req.hostname}`)
    res.send("Hello world from node express app!")
});

// define courses route
app.get('/api/courses', (req, res) => {
    // return array of number; in real world this could be html, db output etc.
    res.send([1, 2, 4])
});

//  dealing with parameters - sing params
app.get('/api/posts/:year', (req, res) => {
    // display id passed in
    // example request: http://localhost:3000/api/posts/2019
    res.send(req.params.year);
});


//  dealing with parameters - dual params
app.get('/api/posts/:year/:month', (req, res) => {
    // display id passed in
    // example request: http://localhost:3000/api/posts/2019/3
    res.send(req.params);
});

//  dealing with query string parameters
app.get('/api/testquery', (req, res) => {
    // display id passed in
    // example request: http://localhost:3000/api/testquery?sortBy=Nf
    res.send(req.query);
});
// use 3000 or env variable as the port number
const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Listening on port ${port} with nodemon`))
