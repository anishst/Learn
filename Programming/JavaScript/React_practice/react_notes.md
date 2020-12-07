# React

A JavaScript library for building user interfaces

- front-end framework


https://reactjs.org/

## Create React App

- https://reactjs.org/docs/create-a-new-react-app.html
- https://github.com/facebook/create-react-app/blob/master/packages/cra-template/template/README.md

## Deployment

- https://create-react-app.dev/docs/deployment/


## Simple App 
```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>JSX</title>
    <link rel="stylesheet" href="styles.css" />
  </head>

  <body>
    <div id="root"></div>
    <script src="../src/index.js" type="text/javascript"></script>
  </body>
</html>
```

```javascript
// index.js
import React from "react";
import ReactDOM from "react-dom";

const name = "Anish";
const currentDate = new Date();
const year = currentDate.getFullYear();

ReactDOM.render(
  <div>
    <p>Created by {name}</p>
    <p>Copyright {year}</p>
  </div>,
  document.getElementById("root")
);


```

## JSX Attributes & Styling React Elements

```javascript
// using an image example
import React from "react";
import ReactDOM from "react-dom";

// https://picsum.photos/
const img = "https://picsum.photos/200";

// heading css comes from css file in public folder
ReactDOM.render(
  <div>
    <h1 className="heading">My Favourite Foods</h1>
    <img alt="random" src={img + "?grayscale"} />

    <img
      className="food-img"
      alt="bacon"
      src="https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/delish-190621-air-fryer-bacon-0035-landscape-pf-1567632709.jpg?crop=0.645xw:0.967xh;0.170xw,0.0204xh&resize=480:*"/>
  </div>,
  document.getElementById("root")
);

```
## Inline Styling for React Elements

```javascript
import React from "react";
import ReactDOM from "react-dom";

const customStyle = {
  color: "red",
  fontSize: "20px",
  border: "1px solid black"
};

customStyle.color = "blue";

ReactDOM.render(
  <h1 style={customStyle}>Hello World!</h1>,
  document.getElementById("root")
);

```

## React Components

Allows separation of code 

- Airbnb Style Guide for React - https://github.com/airbnb/javascript/tree/master/react 



```javascript
// https://codesandbox.io/s/react-components-completed-forked-rzck2

// App.jsx example: 

import React from "react";
import Heading from "./Heading";
import List from "./List";

function App() {
  return (
    <div>
      <Heading />
      <List />
      <List />
    </div>
  );
}

export default App;

// main index.js

import React from "react";
import ReactDOM from "react-dom";
import App from "./components/App";

ReactDOM.render(<App />, document.getElementById("root"));

```
## Template

```javascript
// javascript goes here

```
## JSX

- JSX stands for JavaScript XML
- JSX allows us to write HTML in React.
- https://reactjs.org/docs/introducing-jsx.html
- https://www.w3schools.com/react/react_jsx.asp

## React Props

https://reactjs.org/docs/components-and-props.html

- good for pages with similiar items with same attributes

```javascript
//  without Props

import React from "react";
import ReactDOM from "react-dom";

ReactDOM.render(
  <div>
    <h1>My Contacts</h1>

    <h2>Beyonce</h2>
    <img
      src="https://blackhistorywall.files.wordpress.com/2010/02/picture-device-independent-bitmap-119.jpg"
      alt="avatar_img"
    />
    <p>+123 456 789</p>
    <p>b@beyonce.com</p>

    <h2>Jack Bauer</h2>
    <img
      src="https://pbs.twimg.com/profile_images/625247595825246208/X3XLea04_400x400.jpg"
      alt="avatar_img"
    />
    <p>+987 654 321</p>
    <p>jack@nowhere.com</p>

    <h2>Chuck Norris</h2>
    <img
      src="https://i.pinimg.com/originals/e3/94/47/e39447de921955826b1e498ccf9a39af.png"
      alt="avatar_img"
    />
    <p>+918 372 574</p>
    <p>gmail@chucknorris.com</p>
  </div>,
  document.getElementById("root")
);


//  With props
import React from "react";
import ReactDOM from "react-dom";

function Card(props) {
  return (
    <div>
      <h2>{props.name}</h2>
      <img src={props.img} alt="avatar_img" />
      <p>{props.tel}</p>
      <p>{props.email}</p>
    </div>
  );
}

ReactDOM.render(
  <div>
    <h1>My Contacts</h1>
    <Card
      name="Beyonce"
      img="https://blackhistorywall.files.wordpress.com/2010/02/picture-device-independent-bitmap-119.jpg"
      tel="+123 456 789"
      email="b@beyonce.com"
    />
    <Card
      name="Jack Bauer"
      img="https://pbs.twimg.com/profile_images/625247595825246208/X3XLea04_400x400.jpg"
      tel="+7387384587"
      email="jack@nowhere.com"
    />
  </div>,
  document.getElementById("root")
);

```
## Mapping Data to Components

- https://reactjs.org/docs/lists-and-keys.html

## Babel

Javascript complier

https://babeljs.io/


## Resources
- W3 tutorial: https://www.w3schools.com/react/default.asp
- https://www.appbrewery.co/p/web-development-course-resources/
- HTML Global Attributes - he global attributes are attributes that can be used with all HTML elements; https://www.w3schools.com/tags/ref_standardattributes.asp
- Airbnb Style Guide for React - https://github.com/airbnb/javascript/tree/master/react

## Tools
- Online code editor:  https://codesandbox.io/
- React Developer Tools - chrome extension





