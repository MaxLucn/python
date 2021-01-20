// 面向对象在 ES6 中的使用
// 类的继承、属性表达式

// 定义一个常量
const SHOW_INFO_FUNCTION_NAME = 'showDesc'

// 定一个 Animal 类
class Animal{
    // 构造函数，有 name, age  两个属性
    constructor(name, age){ 
        // 属性实例化  
        this.name = name;
        this.age = age;      
    }

    // 定义一个 eat 方法
    eat(){
        return 'Food'
    }

    // 定义一个 showInfo 方法
    showInfo(){
        console.log('动物的信息：名称->' + this.name + ', 年龄 ->' + this.age);   
    }
}

// 通过继承(extends)的方法写一个 cat 子类
class Cat extends Animal{
    // 重写构造方法，添加一个 color 属性
    constructor(name, age, color){
        // super 调用父类的属性
        super(name, age)
        // 实例化新的 color 属性
        this.color = color;
    }

    // 重写父类的 eat 方法
    eat(){
        // 调用父类的 eat 方法
        let result = super.eat()
        console.log('来自父类', result)
        return result + 'fish'
    }

    // 重写父类的 showInfo 方法
    showInfo(){
        console.log('猫的信息：名称->' + this.name + ', 年龄 ->' + this.age + ', 毛色 --->' + this.color);   
    }

    [SHOW_INFO_FUNCTION_NAME](){
        console.log('自定义的方法，方法名称来自属性表达式')
    }

    ['a' + 'bc'](){
        console.log('abc function');
    }
}

// 父类
// let animal = new Animal('TOMCAT', 8)
// animal.showInfo()
// console.log(animal.eat())

// 子类
let cat = new Cat('Tom', 4, 'balck')
cat.showInfo();
console.log(cat.eat());
// 属性表达式的调用
cat[SHOW_INFO_FUNCTION_NAME]();
cat.abc()
cat['a' + 'bc']()