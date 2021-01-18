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
function fetch(url, {body = '', method = 'GET', headers = {}}){
    $.ajax({
        url,
        method
    })
}
fetch()