/**
 * Created by root on 8/9/17.
 */

// 全选
function SelectALl(){
    $('table :checkbox').prop('checked', true)
}

// 取消所有
function ClearAll(){
    $('table :checkbox').prop('checked', false)
}

// 反选
function ReverseALl(){
    $('table :checkbox').each(function(){
        var isChecked = $(this).prop('checked');
        if(isChecked){
            $(this).prop('checked', false);
        }else{
            $(this).prop('checked', true);
        }
    });
}

// 匹配checkbox，选中的checkbox
function SendValue(){
    var company_arr = [];
    $('table :checkbox').each(function(){
        var isChecked = $(this).prop('checked');
        if(isChecked) {
            $(this).parent('.position').nextAll().each(function () {
                company_arr.push($(this).html());
            });
        }
    });
    console.log(company_arr);
    return company_arr;
}

function CrackChoose() {
    var jsonstr = {};
    var company = new Array();
    company = SendValue();
    for(var i = 0; i <= company.length; i++){
        jsonstr[i] = company[i];
    }
    var jsonstr = JSON.stringify(jsonstr);

    $.ajax({
        // contentType: "application/json; charset=utf-8",
        url: "/host/dos_ssh_user_password/",
        type: "post",
        dataType: "json",
        data: { jsonstr:jsonstr },
        success: function(data){
            var a = data.jsonstr;
            console.log(a);
        },
        error: function(data){

        },
        complete: function(XMLHttpRequest, textStatus){
            console.log(XMLHttpRequest.status);
        }
    });
}