// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleString

var aestTime = new Date().toLocaleString("en-US", { timeZone: "Australia/Brisbane" });
aestTime = new Date(aestTime);
console.log('AEST time: ' + aestTime.toLocaleString())

var asiaTime = new Date().toLocaleString("en-US", { timeZone: "Asia/Shanghai" });
asiaTime = new Date(asiaTime);
console.log('Asia time: ' + asiaTime.toLocaleString())

var usaTime = new Date().toLocaleString("en-US", { timeZone: "America/New_York" });
usaTime = new Date(usaTime);
console.log('USA time: ' + usaTime.toLocaleString())

var indiaTime = new Date().toLocaleString("en-US", { timeZone: "Asia/Kolkata" });
// indiaTime = new Date(indiaTime);
console.log('India time: ' + indiaTime.toLocaleString())