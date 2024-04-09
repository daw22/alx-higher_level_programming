#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  let i = 0;
  while (i < list.length) {
    if (list[i] === searchElement) {
      count += 1;
    }
    i++;
  }
  return (count);
};
