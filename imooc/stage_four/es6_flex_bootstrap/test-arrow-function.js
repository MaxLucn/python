// babel 的使用：将箭头函数转换为普通函数

let add = (a, b) => a + b

let result = add(1, 2)
console.log(result)


// babel test-arrow-function.js -o test-3.js  --presets=@babel/preset-env
// 使用 babel 方法把箭头函数转换为普通函数，转换之后的文件：test-3.js