"use strict";

// babel 的使用：将箭头函数转换为普通函数
var add = function add(a, b) {
  return a + b;
};

var result = add(1, 2);
console.log(result);
