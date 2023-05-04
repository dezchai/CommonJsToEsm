#  CommonJS to ESM
This is a small python script that can be used to convert a base NodeJs project to ESM. 
## Purpose
Popular modules such as [got](https://github.com/sindresorhus/got) and [node-fetch](https://github.com/node-fetch/node-fetch) require [certain changes](https://gist.github.com/sindresorhus/a39789f98801d908bbc7ff3ecc99d99c) in package.json and tsconfig.json in order to compile from Typescript. These changes are tedious to do everytime, so this python script serves to automate that process.
This will fix these compile errors caused by the packages being pure ESM:
```
ERR_UNKNOWN_FILE_EXTENSION
ReferenceError: exports is not defined in ES Module scope
ERR_REQUIRE_ESM
```
## Installation
Simply download the script and place it into a folder that's path is located inside of environemental variables (this will allow it to be run from anywhere). Or place the .py file in the root of your project. Then just run as so:
```
esm.py
```

## Other Notes
I chose python for this script as you can run the file as is and from anywhere when placed in env path. This will remove the comments from tsconfig.json, but I figured it would be better parsing the file and removing comments then using .replace() to keep the comments.

