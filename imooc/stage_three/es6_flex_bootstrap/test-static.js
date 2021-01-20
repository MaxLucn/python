// 静态方法：可以直接通过类来调用的方法（无法通过类的实例来调用）
class MyDate{
    /**
     * 判断月份是否合理
     * @param {} month 月份
    */ 
    static validateMonth(month){
        month = Number.parseInt(month);
        return month >= 1 && month <= 12;
    };
};

console.log(MyDate.validateMonth(1));