
const express = require("express");
const bodyParser = require("body-parser");
const mongoose = require("mongoose");
const ejs = require("ejs");
const port = process.env.PORT || 3000; // set port


const app = express();

app.set('view engine', 'ejs');

app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(express.static("public"));


mongoose.connect("mongodb://192.168.1.25:27017/wikiDB", { useNewUrlParser: true, useUnifiedTopology: true });

// crate article schema
const articleSchema = {
    title: String,
    content: String
}

// crate article model
const Article = mongoose.model("Article", articleSchema);

// create get route - get all articles
app.get("/articles", function (req, res) {
    Article.find({}, function (err, foundArticles) {
        console.log(foundArticles);
        if (!err) {
            res.send(foundArticles);
        } else {
            res.send(err);
        }

    })
})

// create post route - new article
app.post("/articles", function (req, res) {

    const newArticle = new Article({
        title: req.body.title,
        content: req.body.content
    });

    newArticle.save(function (err) {
        if (!err) {
            res.send("Successfully saved article");
        } else {
            res.send(err);
        }
    });

})

// delete  article
app.delete("/articles", function (req, res) {

    Article.deleteMany(function (err) {
        if (!err) {
            res.send("Successfully deleted article");
        } else {
            res.send("Error deleting article");
        }
    })

})


app.listen(port, function () {
    console.log(`Server started on port ${port}`);
});