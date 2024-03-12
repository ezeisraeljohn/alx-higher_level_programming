#!/usr/bin/node

exports.esrever = function (list) {
  const copyList = [];
  for (let i = list.length - 1, j = 0; i >= 0 && j < list.length; j++, i--) {
    copyList[j] = list[i];
  }
  return copyList;
};
