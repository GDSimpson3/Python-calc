const { spawn } = require("child_process");

var numberein = process.argv[2];
console.log(`The first number was taken as ${numberein}`);

var numberzwei = process.argv[3];
console.log(`The second number was taken as ${numberzwei}`);

var numbertype = process.argv[4];
console.log(`The type of sum was taken as ${numbertype}`);

let number1 = numberein;
let number2 = numberzwei;
let typeofsum = numbertype;

const childPython = spawn("python3", [
  "python1.py",
  number1,
  number2,
  typeofsum,
]);
// const childPython = spawn("python", ["python.py"]);

childPython.stdout.on("data", (data) => {
  console.log(`Your answer is: ${data}`);
});

childPython.stderr.on("data", (data) => {
  console.log(`stdout: ${data}`);
});

// childPython.on("close", (code) => {
//   console.log(`child procs: ${code}`);
// });
