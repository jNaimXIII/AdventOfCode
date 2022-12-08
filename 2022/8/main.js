const fs = require("fs");

const file = fs.readFileSync("input.txt").toString().trim();

const grid = [];

file.split("\n").forEach((line) => {
  const row = line
    .trim()
    .split("")
    .map((n) => Number(n));

  grid.push(row);
});

let initX = 1;
let initY = 1;
let maxX = grid.length - 2;
let maxY = grid.map((r) => r[0]).length - 2;

let visibleTrees = 0;

visibleTrees += grid[0].length;
visibleTrees += grid[grid.length - 1].length;
for (let x = initX; x <= maxX; x++) {
  visibleTrees += 2;
}

for (let x = initX; x <= maxX; x++) {
  for (let y = initY; y <= maxY; y++) {
    const row = grid[x];
    const column = grid.map((r) => r[y]);
    const mainTree = grid[x][y];

    const left = row.slice(0, y);
    const right = row.slice(y + 1);
    const top = column.slice(0, x);
    const bottom = column.slice(x + 1);

    let visible = false;
    for (const direction of [left, right, top, bottom]) {
      const tallestTree = Math.max(...direction);

      if (tallestTree < mainTree) {
        visible = true;

        break;
      }
    }

    if (visible) visibleTrees++;
  }
}

// ANSWER (PART 1)
console.log(visibleTrees);

const viewDistances = [];

for (let x = initX; x <= maxX; x++) {
  for (let y = initY; y <= maxY; y++) {
    const row = grid[x];
    const column = grid.map((r) => r[y]);
    const mainTree = grid[x][y];

    const left = row.slice(0, y).reverse();
    const right = row.slice(y + 1);
    const top = column.slice(0, x).reverse();
    const bottom = column.slice(x + 1);

    const directionalViewDistances = [];

    for (const direction of [left, right, top, bottom]) {
      let viewDistance = 0;

      for (const tree of direction) {
        if (tree < mainTree) viewDistance++;

        if (tree >= mainTree) {
          viewDistance++;

          break;
        }
      }

      directionalViewDistances.push(viewDistance);
    }

    const [a, b, c, d] = directionalViewDistances;
    const scenicScore = a * b * c * d;
    viewDistances.push(scenicScore);
  }
}

// ANSWER (PART 2)
console.log(Math.max(...viewDistances));
