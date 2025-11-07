#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let row = 0; row < x; row++) {
    let line = 'E';
    for (let col = 0; col < x; col++) {
      line += 'X';
    }
    console.log(line);
  }
}
