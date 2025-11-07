#!/usr/bin/node
const { argv } = require('node:process');
if (argv[3] != null) {
  console.log('Arguments found');
} else if (argv[2] != null) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
