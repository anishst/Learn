// testing custom module

exports.getDate = getDate;

function getDate() {
    let today = new Date();

    let options = {
        weekday: "long",
        day: "numeric",
        month: "long"
    }

    return today.toLocaleString("en-US", options);
}

exports.getDay = getDay;

function getDay() {
    let today = new Date();

    let options = {
        weekday: "long",

    }
    return today.toLocaleString("en-US", options);
}
