#!/usr/bin/node
const { argv } = require('node:process');
if (argv[2] != null) {
  console.log(argv[2]);
}
else
  {
  console.log('No argument');
  }
