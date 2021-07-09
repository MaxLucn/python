// 二、const 用来声明常量，const 的三大特性
// 1、声明的时候必须赋值，否则会报错
// const NAME;
// NAME = 'Jim';
// console.log(NAME);

// const NAME = 'Jim';
// console.log(NAME);


// 2、常量是只读的，不能重新赋值，比如下面这种就会报错
// const PI = 3.1415926;
// PI = 235235623;


// 3、块级作用域，只在代码块内有效,下面的代码应该把 console 放在代码块里面
// if (true){
//     const NAME = 'Kim';
// }
// console.log(NAME);