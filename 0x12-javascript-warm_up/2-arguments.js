#!/usr/lib/libSystem.B.dylib
function printArgs(arg1, arg2, arg3) {
  console.log(arg1);
  console.log(arg2);
  console.log(arg3);
}
printArgs();

if (process.printArgs.length === 2) {
  console.log('No arguments.');
} else if (process.printArgs.length === 3) {
  console.log('Argument found.');
} else {
  console.log('Arguments found.');
}
