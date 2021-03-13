# Icestudio-cli
Small utilities for working with .ice icestudio files in the command line


## Test files

The Icestudio files used for testing are located in the **Test-files** folder

* **test-01-info.ice**: It only contains a basic info block

## External node.js modules

* [colors](https://nodejs.org/en/knowledge/command-line/how-to-get-colors-on-the-command-line/): Print colors on the command line

## Quick start

* Install all the packages: `npm install`
* Run the test.js example: `node test.js`

```
----------------------------------------
File: Test-files/test-01-info.ice
----------------------------------------
Raw content: 
{ version: '1.2',
  package:
   { name: '', version: '', description: '', author: '', image: '' },
  design:
   { board: 'alhambra-ii', graph: { blocks: [Array], wires: [] } },
  dependencies: {} }

```

