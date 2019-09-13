// https://nodejs.org/en/docs/guides/blocking-vs-non-blocking/

const fs = require('fs');
const data = fs.readFileSync('Node_js_notes.md'); // blocks here until file is read
console.log(data.r);
// moreWork(); // will run after console.log

function read(file, callback) {
    fs.readFile(file, 'utf8', function(err, data) {
        if (err) {
            console.log(err);
        }
        callback(data);
    });
}

var output = read('Node_js_notes.md', function(data) {
    console.log(data);
});