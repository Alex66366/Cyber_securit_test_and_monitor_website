import '../iconfont/iconfont.css'
function fun() {
    let name = document.getElementsByClassName("name")[0];
    let inputPassword = document.getElementsByClassName("inputPassword")[0];
    let password = document.getElementsByClassName("password")[0];

    if (name.value == "" || inputPassword.value == "") {
        alert("请输入账号和密码！");
        return false;
    }
    else if(name.length<1||name.length>10){
        alert("用户名长度应为1~10个中文字符")
        return false;
    }
    else if(inputPassword.length<8||inputPassword.length>16){
        alert("密码长度应为8~16个字符")
        return false;
    }
    else {
        password.value = md5(inputPassword.value);
        alert("登录成功，正在进入！");
        return true;
    }
}

