const express = require('express')
// add https native lib for requests
const https = require('https')
const bodyParser = require('body-parser')
const app = express()
const port = 3000

// allows parsing form data
app.use(bodyParser.urlencoded({ extended: true }))

app.get('/', (req, res) => {

    res.sendFile(__dirname + '/index.html')
})

app.post("/", (req, res) => {

    // make a request to weather app; use units=imperial to get Fahrenheit

    // read API key from environment variable
    const api_key = process.env['OPEN_WEATHER_API_KEY']
    const query = req.body.cityName
    const unit = 'imperial' // imperial = Fahrenheit // https://openweathermap.org/current#data
    URL = `https:api.openweathermap.org/data/2.5/weather?q=${query}&units=${unit}&appid=${api_key}`
    https.get(URL, (response) => {

        response.on('data', (data) => {
            // conver hex value to JSON
            const weatherData = JSON.parse(data)
            // print JSON data
            console.log(weatherData)
            // get temp 
            const temp = weatherData.main.temp
            // get weather description
            const description = weatherData.weather[0].description
            const icon = weatherData.weather[0].icon
            console.log(temp, description)
            // display in browser
            res.write("<p>The weather is currently " + description + "</p>")
            res.write("<h1>The temperature in " + query + " is: " + temp + "</h1>")
            // display iconv - https://openweathermap.org/weather-conditions
            res.write(`<img src="http://openweathermap.org/img/wn/${icon}@2x.png"/>`)
            res.send()
        })
    })
})


app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
})
