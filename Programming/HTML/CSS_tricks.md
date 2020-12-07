# CSS Tricks

## Make card template with a circle images

```html
<!-- https://codesandbox.io/s/react-props-practice-completed-forked-g5f9e?file=/public/styles.css:258-928 -->


<div class="card"><div class="top"><h2 class="name">Beyonce</h2><img class="circle-img" src="https://blackhistorywall.files.wordpress.com/2010/02/picture-device-independent-bitmap-119.jpg" alt="avatar_img"></div><div class="bottom"><p class="info">+123 456 789</p><p class="info">b@beyonce.com</p></div></div>
```

```css
.card {
  border-radius: 25px;
  position: relative;
  padding: 25px 15px;
  background-color: #81ecec;
  margin: 50px 0;
  height: 200px;
  box-shadow: 0 2px 5px #ccc;
  text-align: left;
}

.top {
  border-radius: 25px 25px 0 0;
  height: 100px;
  width: 100%;
  background-color: #00cec9;
  position: absolute;
  top: 0;
  left: 0;
  display: flex;
}

.name {
  font-size: 2em;
  color: #2d3436;
  display: flex;
  flex: 1;
  margin: 10% 20px 0;
}

.card img {
  margin: 30px 20px 0 0;
}

.circle-img {
  border-radius: 50%;
  border: 7px solid #fff;
  width: 120px;
  height: 120px;
}

.bottom {
  margin-top: 120px;
}

.info {
  margin: 20px 0;
  color: #1a7e76;
}
/*  */
```


