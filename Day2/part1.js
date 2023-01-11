const fs = require('fs');
let totalPoints = 0;

fs.readFileSync('./input.txt', 'utf-8').split("\n").forEach(set => {
    const [a, b] = set.split(" ");
    if ((a == "A" && b == "Y") || (a == "B" && b == "Z") || (a == "C" && b == "X")) {
        totalPoints += 6;
    } else if ((a == "A" && b == "X") || (a == "B" && b == "Y") || (a == "C" && b == "Z")) {
        totalPoints += 3;
    }
    if (b == "X") {
        totalPoints += 1;
    }
    else if (b == "Y") {
        totalPoints += 2;
    }
    else if (b == "Z") {
        totalPoints += 3;
    }
})

console.log(totalPoints);