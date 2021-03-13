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

//-- Functions for printing the icestudio elements
//-- Print the whole icestudio root element
function print_root(ice)
{
  console.log("Icestudio ROOT: ".blue);

  console.log("  Version: ".white + ice['version']);
  console.log("  Board: ".white + ice['design']['board'])

  //-- Get the total number of top-level blocks
  let nb = ice['design']['graph']['blocks'].length;

  console.log("  Blocks: ".white + nb)

   //-- Get the total number of wires
  let wires = ice['design']['graph']['wires'].length;
  console.log("  Wires: ".white + wires)


  console.log("");
  console.log("Raw content: ".red);
  console.log(ice);

}


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

print_root(ice);
console.log("");

