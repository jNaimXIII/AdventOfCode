const fs = require("fs");

const file = fs.readFileSync("input.txt").toString().trim();

function uniqueStringLocator(uniqueItems) {
  return () => {
    const buffer = [];
    let currentChar = 0;

    for (const char of file) {
      buffer.push(char);

      currentChar++;

      if (buffer.length < uniqueItems) continue;

      const allUniqueCodes = buffer.every((code) => {
        let codeCount = 0;

        buffer.forEach((item) => {
          if (item === code) codeCount++;
        });

        return codeCount <= 1;
      });

      if (allUniqueCodes) break;

      buffer.shift();
    }

    return currentChar;
  };
}

const packetLocator = uniqueStringLocator(4);

// ANSWER (PART 1)
console.log(packetLocator());

const messageLocator = uniqueStringLocator(14);

// ANSWER (PART 2)
console.log(messageLocator());
