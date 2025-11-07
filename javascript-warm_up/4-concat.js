#!/usr/bin/node
const { argv } = require('node:process');
const firstArgv = argv[2];
const secondArgv = argv[3];
console.log(firstArgv, 'is', secondArgv);
