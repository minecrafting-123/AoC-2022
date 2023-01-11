const fs = require('fs');

const yes = fs.readFileSync('./input.txt', 'utf-8').split("\r\n\r\n").map(a => {
    return a.split("\r\n").reduce((accumulator, currentValue) => accumulator + parseInt(currentValue), 0);
}).sort((a,b) => b-a);

console.log(yes[0])
console.log(yes[1])
console.log(yes[2])
console.log(yes[0] + yes[1] + yes[2])