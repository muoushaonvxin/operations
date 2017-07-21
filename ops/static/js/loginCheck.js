/**
 * Created by Selience on 2017/6/11.
 */

function getUserName(){
    var username = document.getElementsByClassName("username")[0].value;
    var password = document.getElementsByClassName("password")[0].value;

    if(username == ""){
        var user = document.getElementsByClassName("user")[0];
        user.innerHTML = "用户名不能为空";
        return false;
    } else if (!(username == "")) {

    }

    if(password == ""){
        var pass = document.getElementsByClassName("pass")[0];
        pass.innerHTML = "密码不能为空";
        return false;
    } else if (!(password == "")) {

    }
}
