// ES6 以前的面向对象编程
// function Point(x, y){
//     this.x = x;
//     this.y = y;
// }

// Point.prototype.toString = function(){
//     return '点的位置：('+ this.x +', '+ this.y +')';
// };

// let p = new Point(1, 2);
// console.log(p);

// ES6中引入 class 关键字；实现面向对象编程
class Point{
    constructor(x, y){    // 构造函数
        this.x = x;
        this.y = y;
    }
    toString(){
        return '点的位置：('+ this.x +', '+ this.y +')';
    }
}
// 函数的调用：关于类的实例
// 使用 new 关键字来实例化类
let p = new Point(1, 2);
console.log(p.toString());