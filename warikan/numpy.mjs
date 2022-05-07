export const sum = (array, axis = 0) => {
  array = axis === 0 ? array : transpose(array);

  let out = array[0].slice().fill(0);
  array.map((row) => {
    row.map((value, i) => {
      out[i] += value;
    });
  });
  return out;
};

export const transpose = (array) =>
  array[0].map((col, i) => array.map((row) => row[i]));

export const zeros = (n) =>
  Array(n)
    .fill()
    .map(() => Array(n).fill(0));

// console.log(sum(array, (axis = 0)));
// console.log(sum(array, (axis = 1)));
