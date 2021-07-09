/**
 * 格式化用户昵称，取姓，名用 ** 代替
 * @param {*} name 用户昵称
 */

 export default function(name){
    return name.substr(0, 1) + '***'
 }