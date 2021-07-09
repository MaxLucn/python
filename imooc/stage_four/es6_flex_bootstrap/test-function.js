// function point(x=0, y, z){
//     console.log('x', x);
//     console.log('y', y);
//     console.log('z', z);
// }
// point(1, 1);
// // x 1
// // y 1
// // z undefined
// // 这里需要注意的是有默认值的变量应该放在最后面，即function point(y, z，x=0)


// 当形参为对象时，可使用解构对象
// function fetch(url, {body = '', method = 'GET', headers = {}}){
//     $.ajax({
//         url,
//         method
//     })
// }
// fetch('www.baidu.com')


// 箭头函数：定义箭头函数
// // 传一个参数
// let f1 = v => v;  // 等同于
// let f1 = function(v){
//     return v;
// };
// // 传两个参数
// let f2 = (a, b) => a + b;  // 等同于 
// let f2 = function(a, b){
//     return a + b;
// };


// // 函数体包含多条语句，使用 {} 包含语句块
// let f3 = (a, b) => {
//     console.log(a, b);
//     return a + b;
// };

// // 箭头函数的使用：数组遍历
// let arr = [1, 2, 3];
// arr.map(function(x){
//     return x * x;
// });
// console.log(arr);
// console.log('--------');
// let arr_1 = [1, 2, 3];  // 上面的函数块可以用箭头函数表示
// arr_1.map(x => x * x);
// console.log(arr_1);


// 箭头函数体内的 this 指向定义时所在的对象，不是实例化后的对象(在函数定义时绑定)
// 1、第一个演示
// let user = {
//     name: 'Tom',
//     age: 23,
//     info(){
//         return this.name + this.age
//     },
//     info_arrow:() =>{
//         return this.name + this.age
//     }
// }
// console.log(user.info());
// console.log(user.info_arrow());

// 2、第二个演示
let myobj = {
    a(){
        console.log('a', this);  // myobj
        setTimeout(() =>{
            console.log('timeout', this);  //myobj
        },100);
    },
    b:() =>{
        console.log('b', this);  // window
    }
};
// console.log(myobj.a());
// console.log(myobj.b());
myobj.a()
myobj.b()