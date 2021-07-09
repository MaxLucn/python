// function show1(){
// 	// alert("12345");

// 	// document.getElementById("UserName").value="999";

// 	var xb = document.getElementsByName("xb");
// 	var xbText;
// 	if(xb[0].checked){
// 		xbText = xb[0].value;
// 	 }else{
// 	 	xbText = xb[1].value;
// 	 }
// 	 alert(xbText); 
// }


// 对表单元素设置3、4、5
function ymd() {
    // 获取 id = yyyy 的控件（表单元素）
    var yyyy = document.getElementById("yyyy");
    var mm = document.getElementById("mm");
    var dd = document.getElementById("dd");

    var date = new Date();
    var year = parseInt(date.getFullYear());
    initSelect(yyyy, 1999, year);
    initSelect(mm, 1, 12);
    initSelect(dd, 1, 31);
    // 获取 yyyy 的所有条目
    var n = yyyy.length;
    // 列表框选中某一个条目
    yyyy.selectedIndex = Math.round(n / 2);
    // 将某个列表框的条目数设置为0，效果为删除
    // dd.options.length=0;
}

/* 给列表框赋值，传递三个参数：表单元素，开始值，结束值 */
function initSelect(obj, start, end) {
    for (var i = start; i <= end; i++) {
        // 给 yyyy 表单元素添加条目，第一个 i 表示显示的名字，第二个 i 表示值
        obj.options.add(new Option(i, i));
    }
}

function selectYmd() {
    var yyyy = document.getElementById("yyyy");
    var mm = document.getElementById("mm");
    var dd = document.getElementById("dd");
    var m = parseInt(mm.value);
    var dayEnd;
    if (m === 4 || m === 6 || m === 9 || m === 11) {
        dayEnd = 30;
    } else if (m === 2) {
        dayEnd = 28;
        y = parseInt(yyyy.value);
        if ((y % 4 === 0 && y % 100 !== 0) || y % 400 === 0) {
            dayEnd = 29;
        }
    } else {
        dayEnd = 31;
    }
    dd.options.length = 0;
    initSelect(dd, 1, dayEnd);
}

// 删除列表框的某一个条目，即：按索引号删除
function deleteSelect() {
    var dd = document.getElementById("dd");
    // dd.options.remove(1);
    for (i = dd.length; i >= 0; i--) {
        dd.options.remove(0);
    }
}