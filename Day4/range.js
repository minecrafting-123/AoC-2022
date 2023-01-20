const fs = require('fs');
const myRe = new RegExp('([0-9]+)\-([0-9]+)\,([0-9]+)\-([0-9]+)');
let pairs = 0;

fs.readFileSync('./input.txt', 'utf-8').split('\n').forEach(line => {
    // Creates an array with information we want: specifically from 1 - 4, there are the four values we want
    let values = myRe.exec(line);
    if (((parseInt(values[1]) <= parseInt(values[3])) && (parseInt(values[2]) >= parseInt(values[4]))) || ((parseInt(values[3]) <= parseInt(values[1])) && (parseInt(values[4]) >= parseInt(values[2])))){
        pairs++;
    }
})

console.log(pairs)