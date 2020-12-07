//jshint esversion:6

const express = require("express");
const bodyParser = require("body-parser");
const mongoose = require("mongoose");
const port = process.env.PORT || 3000; // set port
const _ = require("lodash");

const app = express();

app.set('view engine', 'ejs');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));

mongoose.connect("mongodb://192.168.1.25:27017/todolistDB", { useNewUrlParser: true, useUnifiedTopology: true });
// using cloud atlas db
// mongoose.connect("mongodb+srv://<cloud usernamepwd and server ip>/todolistDB", { useNewUrlParser: true, useUnifiedTopology: true });

// new schema
const itemsSchema = {
  name: String
};

const Item = mongoose.model("Item", itemsSchema);


const item1 = new Item({
  name: "Welcome to your todolist!"
});

const item2 = new Item({
  name: "Hit the + button to add a new item."
});

const item3 = new Item({
  name: "<-- Hit this to delete an item."
});

const defaultItems = [item1, item2, item3];


const listSchema = {
  name: String,
  items: [itemsSchema]
};

const List = mongoose.model("List", listSchema);


app.get("/", function (req, res) {

  Item.find({}, function (err, foundItems) {

    if (foundItems.length === 0) {
      Item.insertMany(defaultItems, function (err) {
        if (err) {
          console.log(err);
        } else {
          console.log("Successfully savevd default items to DB.");
        }
      });
      res.redirect("/");
    } else {
      console.log("List is not empty")
      console.log(foundItems);
      res.render("list", { listTitle: "Today", newListItems: foundItems });
    }
  });

});

// to prevent 404 issues https://stackoverflow.com/questions/35408729/express-js-prevent-get-favicon-ico
app.get('/favicon.ico', (req, res) => res.status(204));

// route to create a custom to do list page
app.get("/:customListName", function (req, res) {
  // store Custom List name and covert to Uppercase string using lodash function
  const customListName = _.capitalize(req.params.customListName);
  console.log("Getting param");
  console.log(customListName);

  List.findOne({ name: customListName }, function (err, foundList) {
    if (!err) {
      if (!foundList) {
        //Create a new list
        const list = new List({
          name: customListName,
          items: defaultItems
        });
        list.save();
        res.redirect("/" + customListName);
      } else {
        //Show an existing list

        res.render("list", { listTitle: foundList.name, newListItems: foundList.items });
      }
    }
  });



});

app.post("/", function (req, res) {

  const itemName = req.body.newItem;
  const listName = req.body.list;
  console.log(itemName);
  console.log(listName);

  const item = new Item({
    name: itemName
  });

  if (listName === "Today") {
    item.save();
    res.redirect("/");
  } else {
    List.findOne({ name: listName }, function (err, foundList) {
      // push new item
      foundList.items.push(item);
      foundList.save();
      res.redirect("/" + listName);
    });
  }
});

app.post("/delete", function (req, res) {
  const checkedItemId = req.body.checkbox;
  const listName = req.body.listName;

  if (listName === "Today") {
    Item.findByIdAndRemove(checkedItemId, function (err) {
      if (!err) {
        console.log("Successfully deleted checked item.");
        res.redirect("/");
      }
    });
  } else {
    List.findOneAndUpdate({ name: listName }, { $pull: { items: { _id: checkedItemId } } }, function (err, foundList) {
      if (!err) {
        // console.log(`Removed item ${foundList.name}`);
        res.redirect("/" + listName);
      }
    });
  }


});

app.get("/about", function (req, res) {
  res.render("about");
});

app.listen(port, function () {
  console.log(`Server started on port ${port}`);
});
