// 定义两个常量
const APP_NAME = '在线问答系统'
const VERSION = '1.0'


function getName(){
    console.log('get name');
}
// 批量导出定义好的常量
export {
    APP_NAME,
    VERSION as v,
    getName
}