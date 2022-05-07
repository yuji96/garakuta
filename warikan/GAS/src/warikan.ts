import { zeros } from "../../numpy.mjs";

const print = console.log;

const members = ["A", "B", "C"];
const array = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
];

const log = [
  ["A", 10000, null],
  ["B", 7000, null],
  ["C", 3500, null],
  ["D", 12000, null],
  ["B", 3000, '"{"A": 2000, "B": 1200, "C": 1000, "D": 2000}"'],
];

const n = members.length;
let transition = zeros(n);
let account = zeros(n);

print(log);

// log.map(row => {
  
// })