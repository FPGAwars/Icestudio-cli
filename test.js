//-------------------------
//-- Simple test file
//-------------------------

//-- fs module for accesing the filesystem
const fs = require('fs');

//-- Module for printing in colors on the console
const colors = require('colors');

//-- Icestudio file to analyze
const ICE_FILE = 'Test-files/test-01-info.ice'

//-- Header length in characteres
const HLEN = 40;

console.log("");
console.log("-".repeat(HLEN));
console.log(`File: ${ICE_FILE}`);
console.log("-".repeat(HLEN));

//-- Icestudio file data
let ice_data;

//-- Read the Icestudio file
try {
  ice_data = fs.readFileSync(ICE_FILE);

} catch (error) {
  console.log(error.message.red + '\n');
  process.exit(1);  
}

//-- The icestudio file is in JSON format
//-- Parse it and get the root Object
let ice = JSON.parse(ice_data);

console.log("Raw content: ".blue);

console.log(ice);
console.log("");

