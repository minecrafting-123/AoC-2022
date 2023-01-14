const fs = require('fs');
let totalPoints = 0;
let groupsCounted = 0;
let groups = [];
let sackString = "";
//read the file input.txt and split it by line, for each line...
fs.readFileSync('./input.txt', 'utf-8').split("\n").forEach(line => {
//appends to the groups[] three lines at a time
    sackString += line + " ";
    groupsCounted++;
    if (groupsCounted >= 3){
        groups.push(sackString);
        sackString = "";
        groupsCounted = 0;
    }
});
//for each three line cluster in groups[]...
groups.forEach(item => {
    //makes arrays from the three lines
    let set = item.split(" ");
    let str0 = set[0].split("");
    let str1 = set[1].split("");
    let str2 = set[2].split("");
    //finds characters that are common to all three strings and removes them from the original to prevent any overcounting
    let common = str0.map(char => {
        if (str1.includes(char) && str2.includes(char)){
            str1 = str1.filter(thing => thing != char);
            str2 = str2.filter(thing => thing != char);
            return char;
        }
    }).filter(x => x !== undefined);
    //translates the characters into numbers for the final answer
    common.forEach(element => {
        if (65 <= element.charCodeAt() && element.charCodeAt() <= 90){
            totalPoints += element.charCodeAt() - 38;
        } else if(97 <= element.charCodeAt() && element.charCodeAt() <= 122){
            totalPoints += element.charCodeAt() - 96
        }
    })
});

console.log(totalPoints);