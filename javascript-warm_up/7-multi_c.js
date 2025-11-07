#!/usr/local/bin/node
const n = parseInt(process.argv[2]);
if (isNaN(n)) {
  console.log('Missing number of occurrences');
} else {
  let res = '';
  let x = 0;
  while (x < n) {
    res += 'C is fun\n';
    x++;
  }
  if (res) console.log(res.trimEnd());
}
