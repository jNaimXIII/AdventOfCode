const fs = require("fs");

const file = fs.readFileSync("input.txt").toString().trim();
const pairs = file.split("\n").map((line) => line.trim().split(" "));

const scoreMap = [
  [0, 0],
  ["A", "X"],
  ["B", "Y"],
  ["C", "Z"],
];

const getHandScore = (hand) => {
  return scoreMap.findIndex((pair) => pair.includes(hand));
};

const powerMap = {
  A: "Z",
  B: "X",
  C: "Y",
  X: "C",
  Y: "A",
  Z: "B",
};

const getRoundScore = (handA, handB) => {
  const handScore = getHandScore(handB);

  if (powerMap[handB] == handA) return 6 + handScore;
  else if (powerMap[handA] == handB) {
    return 0 + handScore;
  } else return 3 + handScore;
};

let score;

score = 0;
for (const pair of pairs) {
  const [handA, handB] = pair;

  score += getRoundScore(handA, handB);
}

// ANSWER (PART 1)
console.log(score);

score = 0;
for (const pair of pairs) {
  const [handA, move] = pair;

  let handB;
  if (move == "Z") {
    const loosingHand = powerMap[handA];
    const winningMove = powerMap[loosingHand];

    const winningIndex = getHandScore(winningMove);
    handB = scoreMap[winningIndex][1];
  } else if (move == "X") handB = powerMap[handA];
  else if (move == "Y") handB = handA;

  score += getRoundScore(handA, handB);
}

// ANSWER (PART 2)
console.log(score);
