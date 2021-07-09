// 一、let 跟 var 的不同
// 1、let 需要先声明才能使用，不然会报错，比如下面这样就会报错，正确的是先 let 后打印
// console.log(a);
// let a = 0;

// 2、let 不能重复命名,即下面这样
// let a = 10;
// console.log(a);
// let a = 30;
// console.log(a);


// 3、块级作用域，变量只在代码块内部有效
// function func(){
//     let n = 5;
//     if(true){
//         let n = 10;
//     }
//     console.log(n);
// }
// func()

// let 变量只在{}作用域内有效
let a = 1;{
    let a = 2;
    console.log(a);
}
console.log(a);
// var 声明的变量不受 {} 作用域影响
var b = 1;{
    var b = 2;
    console.log(b);
}
console.log(b);





