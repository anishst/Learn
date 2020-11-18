const express = require('express')
// add https native lib for requests
const https = require('https')
const app = express()
const port = 3000


app.get('/', (req, res) => {
    res.send('Server is up and running.')

    // make a request to weather app; use units=imperial to get Fahrenheit
    // https://openweathermap.org/current#data

    // read API key from environment variable
    const api_key = process.env['OPEN_WEATHER_API_KEY']
    URL = `https:api.openweathermap.org/data/2.5/weather?q=Tysons&units=imperial&appid=${api_key}`
    https.get(URL, (response) => {

        response.on('data', (data) => {
            // print hex value of data retured
            console.log(data)
            // conver to JSON
            const weatherData = JSON.parse(data)
            // print JSON data
            console.log(weatherData)
            //  you can use JSON.stringify to pack data into a string

            // get temp 
            const temp = weatherData.main.temp
            // get weather description
            const description = weatherData.weather[0].description
            console.log(temp, description)

        })

        // log response
        console.log(response)
        // log statusCode
        // see code info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
        console.log(response.statusCode)
    })
})


app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
})