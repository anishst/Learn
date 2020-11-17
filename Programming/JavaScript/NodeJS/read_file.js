// This script reads from a file

const fs = require('fs');

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