
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


//***********************************requests targetting all articles ************************************************** */ 

//  chain routes - https://expressjs.com/en/guide/routing.html
app.route("/articles")
    .get(function (req, res) {
        Article.find({}, function (err, foundArticles) {
            console.log(foundArticles);
            if (!err) {
                res.send(foundArticles);
            } else {
                res.send(err);
            }

        })
    })
    .post(function (req, res) {

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
    .delete(function (req, res) {

        Article.deleteMany(function (err) {
            if (!err) {
                res.send("Successfully deleted article");
            } else {
                res.send("Error deleting article");
            }
        })

    });


//***********************************requests targetting specific article ************************************************** */ 

app.route("/articles/:articleTitle")
    .get(function (req, res) {
        Article.findOne({ title: req.params.articleTitle }, function (err, foundArticle) {
            if (foundArticle) {
                res.send(foundArticle);
            } else {
                res.send("Article not found");
            }
        });

    })
    .put(function (req, res) {
        console.log(req.params.articleTitle);
        Article.update(
            { title: req.params.articleTitle },
            { title: req.body.title, content: req.body.content },
            { overwrite: true },
            function (err) {
                if (!err) {
                    res.send("Successfully updated article");
                } else {
                    res.send("Error updating article");
                }
            }
        );
    })
    .patch(function (req, res) {

        Article.update(
            { title: req.params.articleTitle },
            // parse javascript object based on field passed in
            { $set: req.body },
            function (err) {
                if (!err) {
                    res.send("Successfully updated article");
                } else {
                    res.send("Error updating article");
                }
            }
        );
    })
    .delete(function (req, res) {

        Article.deleteOne(
            { title: req.params.articleTitle },
            function (err) {
                if (!err) {
                    res.send("Successfully deleted article");
                } else {
                    res.send("Error deleting article");
                }
            }
        );
    });

app.listen(port, function () {
    console.log(`Server started on port ${port}`);
});