// ES6 以前的面向对象编程
function Point(x, y){
    this.x = x;
    this.y = y;
}

Point.prototype.toString = function(){
    return '点的位置：('+ this.x +', '+ this.y +')';
};

let p = new Point(1, 2);
console.log(p);