/*
  Only seem to be able to do the first one. Second one needs some more fiddling
  around to solve. ;)
*/

const fs = require("fs");

const file = fs.readFileSync("input.txt").toString().trim();
const lines = file.split("\n");

let x = 1;
let xValues = [1, 1];
let nCycles = 1;

for (const instruction of lines) {
  if (instruction.startsWith("noop")) {
    handleCycleUpdate();
  }

  if (instruction.startsWith("addx")) {
    handleCycleUpdate();

    const value = Number(instruction.split(" ")[1]);
    x += value;

    handleCycleUpdate();
  }
}

function handleCycleUpdate() {
  xValues.push(x);
  nCycles++;
}

let signalStrengths = [];

const start = 20;
const step = 40;
const limit = 220;
for (let i = start; i <= limit; i += step) {
  const xValue = xValues[i];

  signalStrengths.push(xValue * i);
}
// ANSWER (PART 1)
console.log(signalStrengths.reduce((a, b) => a + b, 0));
