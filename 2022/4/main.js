const fs = require("fs");

const file = fs.readFileSync("input.txt").toString().trim();
const sections = file.split("\n").map((line) => line.trim().split(","));

let fullyCoveredPairs = 0;
sections.forEach((section) => {
  let [a, b] = section;
  a = a.split("-").map((n) => Number(n));
  b = b.split("-").map((n) => Number(n));

  if (a[0] <= b[0] && a[1] >= b[1]) {
    fullyCoveredPairs++;
  } else if (b[0] <= a[0] && b[1] >= a[1]) {
    fullyCoveredPairs++;
  }
});

// ANSWER (PART 1)
console.log(fullyCoveredPairs);

let overlappingPairs = 0;
sections.forEach((section) => {
  let [a, b] = section;
  a = a.split("-").map((n) => Number(n));
  b = b.split("-").map((n) => Number(n));

  const a_sections = [];
  const b_sections = [];

  for (let i = a[0]; i <= a[1]; i++) a_sections.push(i);
  for (let i = b[0]; i <= b[1]; i++) b_sections.push(i);

  for (const a_section of a_sections) {
    if (b_sections.includes(a_section)) {
      overlappingPairs++;
      return;
    }
  }
});

// ANSWER (PART 2)
console.log(overlappingPairs);
