function init() {
    let num = document.getElementById("num");
    num.value = 0;
    num.disabled = "disabled";
    let oButton = document.getElementsByTagName("input");
    let btn_num1;
    let fh;
    for (let i = 0; i < oButton.length;i++){
        oButton[i].onclick = function(){
            if (isNumber(this.value)){
                num.value = (num.value + this.value) * 1;
            }else{
                // alert("fei");
                let btn_num = this.value;
                switch (btn_num){
                    case "+":
                        // alert('+');
                        btn_num1 = Number(num.value);
                        num.value = 0;
                        fh = "+";
                        break;
                    case "-":
                        btn_num1 = Number(num.value);
                        num.value = 0;
                        fh = "-";
                        break;
                    case "*":
                        btn_num1 = Number(num.value);
                        num.value = 0;
                        fh = "*";
                        break;
                    case "/":
                        btn_num1 = Number(num.value);
                        num.value = 0;
                        fh = "/";
                        break;
                    case ".":
                        num.value= dec_number(num.value);
                        break;
                    case "=":
                        switch(fh){
                            case "+":
                                num.value = btn_num1 + Number(num.value);
                                break;
                            case "-":
                                num.value = btn_num1 - Number(num.value);
                                break;
                            case "*":
                                num.value = btn_num1 * Number(num.value);
                                break;
                            case "/":
                                if (Number(num.value) === 0){
                                    alert("除数不能为 0 ！！！")
                                    num.value = 0;
                                }else{
                                    num.value = btn_num1 / Number(num.value);
                                }
                                break;
                        }
                        break;
                    case "√":
                        alert('grnhao');
                        break;
                    case "+/-":
                        num.value = sign(num.value);
                        break;
                    case "⟵":
                        num.value = back(num.value);
                        break;
                    case "c":
                        num.value = 0;
                        break;
                }
            }
        }
    }

}
/* 正负号 */
function sign(n){
    if(n.indexOf("-")=== -1){
        n = "-" + n;
    }else{
        n = n.substr(1,n.length);
    }
    return n;
}
/* 退位键 */
function back(n){
    n = n.substr(0, n.length-1);
    if(isNull(n)){
        n = "0";
    }
    return n;
}



/* 小数点 */
function dec_number(n){
    if (n.indexOf(".") === -1){
        n = n + ".";
    }
    return n;
}

/*  验证文本框是否为空或者0 */
function isNull(n){
    if (n ==="0" || n.length === 0){
        return true;
    }
}


function isNumber(n){
    // if (!isNaN(n)){
    //     return true; //参数 n 是数字
    // }else{
    //     return false; // 参数 n 不是数字
    // } !isNaN(n);
    return !isNaN(n);
}
// function num_1_click(){
//     let num = document.getElementById("num");
//     // 获取文本框的值
//     let n = num.value;
//     // 文本框的值做字符串的拼接，在链接 1
//     if (n==="0"){
//         n="1";
//     }else{
//         n = n + "1";
//     }
//     // 再把链接之后的新值赋值给文本框
//     document.getElementById("num").value=n;
// }