// 解构赋值
// 一、数组的解构赋值
// 1、按顺序将值赋值对应的变量
// let d = [1, 2, 3];
// let [a, b, c] = d;
// console.log(a);
// console.log(b);
// console.log(c);

// 2、 用 ... 表示解构运算符，将剩余的内容全部赋值
// let [u, ...f] = [1, 2, 4, 5, 7];
// console.log(u);
// console.log(f);

// //3、结构赋值失败，变量值为 undefined
// let [w, o] = [1];
// console.log(w);
// console.log(o);
// // 为了防止结构赋值失败，可以在解构之前给变量设置默认值
// console.log('----------------')
// let [w1, o1=34] = [1];
// console.log(w1);
// console.log(o1);


// 二、对象的解构赋值。在对象的解构赋值中，与顺序无关，但变量名与属性名必须一致
// 1、按顺序把值赋值给对应的变量
// let {name, sex} = {name:'Tom', sex:'boy'};
// console.log(name);
// console.log(sex);

// 2、可以解构对象中的常量、方法
// console.log(Math.PI);
// let{PI, sin} = Math;
// console.log(PI);
// console.log(sin(PI/2)) // sin 90度

// //3、结构赋值失败，变量值为 undefined
// // 为了防止结构赋值失败，可以在解构之前给变量设置默认值
// let {x, y=3} = {x:2};
// console.log(x)
// console.log(y)

// 4、重新指定变量名称
// let {color:sky} = {color:'blue'};
// console.log(sky)

// 5、复杂对象的解构赋值
let{title, author:{name, age}} = {
    title:'新闻',
    author:{
        name:"Tom",
        age:23
    }
}
console.log(name);
console.log(age);