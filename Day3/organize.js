const fs = require('fs');
let totalPoints = 0;

fs.readFileSync('./input.txt', 'utf-8').split("\n").forEach(set => {
    a = set.substring(0, set.length/2);
    b = set.substring(set.length/2);
    str1 = a.split("");
    str2 = b.split("");

    common = str1.map(char => {
        if (str2.includes(char)){
            index = str2.indexOf(char);
            str2 = str2.filter(thing => thing != char);
            return char;
        }
    }).filter(x => x !== undefined);
    common.forEach(element => {
        if (65 <= element.charCodeAt() && element.charCodeAt() <= 90){
            totalPoints += element.charCodeAt() - 38;
        } else if(97 <= element.charCodeAt() && element.charCodeAt() <= 122){
            totalPoints += element.charCodeAt() - 96
        }
    })
})

console.log(totalPoints);