#!/usr/bin/node
const x = process.argv.slice(2).map(Number);
if (x.lenght <= 1) {
  console.log(0);
} else {
  x.sort((a, b) => b - a);
  console.log(x[1]);
}
