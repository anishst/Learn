# Wiki REST API

Practice REST command

1. create folder 
2. create files:  app.js
3. initialize project cmd line: ```npm init -y```
4. install express body parser and ejs: ```npm install express body-parser ejs mongoose```
6. run app : ```node server.js```


data example: 
```json
{
    "_id" : "5c18e1892998bdb3b3d355bf",
    "title" : "REST",
    "content" : "REST is short for REpresentational State Transfer. IIt's an architectural style for designing APIs."
}


{
    "_id" : ObjectId("5c139771d79ac8eac11e754a"),
    "title" : "API",
    "content" : "API stands for Application Programming Interface. It is a set of subroutine definitions, communication protocols, and tools for building software. In general terms, it is a set of clearly defined methods of communication among various components. A good API makes it easier to develop a computer program by providing all the building blocks, which are then put together by the programmer."
}


{
    "_id" : ObjectId("5c1398aad79ac8eac11e7561"),
    "title" : "Bootstrap",
    "content" : "This is a framework developed by Twitter that contains pre-made front-end templates for web design"
}


{
    "_id" : ObjectId("5c1398ecd79ac8eac11e7567"),
    "title" : "DOM",
    "content" : "The Document Object Model is like an API for interacting with our HTML"
}


{
    "_id" : "5c18f35cde40ab6cc551cd60",
    "title" : "Jack Bauer",
    "content" : "Jack Bauer once stepped into quicksand. The quicksand couldn't escape and nearly drowned.",
    "__v" : 0
}
```

- fetch all articles : http://localhost:3000/articles
- fetch specific article: localhost:3000/articles/REST
- fetch specific article with space: localhost:3000/articles/Jack%20Bauer
    - URL encoding: https://www.w3schools.com/tags/ref_urlencode.ASP
- use **Postman** to post new articles
# resources

- https://github.com/londonappbrewery/Build-Your-Own-RESTful-API
