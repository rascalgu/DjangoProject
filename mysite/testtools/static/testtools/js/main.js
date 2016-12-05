/**
 * Created by gutongjie on 2016/10/19.
 */
function getScenarioList(projectid){
    $.ajax({url: "http://localhost:8000/testtools/project/list/ajax/" + projectid, type: "get", dataType: "json",
                success: function(data){
                    console.log(data);

                    $('.sidenav-dropdown'+projectid).html("");
                    if (data.length != 0) {
                        for (var i = 0; i < data.length; i++) {
                            $('.sidenav-dropdown' + projectid).append("<li><a href='/testtools/scenario/detail/" + data[i].pk + "/'>\
                            " + data[i].fields.test_scenario_name + "</a></li>");
                        }
                        $('.sidenav-dropdown'+projectid).append("<li><a href='/admin/testtools/project/"+projectid+"/change/' target='_blank'>添加场景</a></li>");
                    }
                    else {
                        $('.sidenav-dropdown'+projectid).append("<li><a href='/admin/testtools/project/"+projectid+"/change/' target='_blank'>添加场景</a></li>");
                    }
                },
                async: true,
            });
};


function getRequestResult(request_link){
    var param_name = document.getElementsByName('param-name');
    var param_value = document.getElementsByName('param-value');
    var test = "";
    for (var i = 0; i < param_name.length; i++) {
        test =  test + param_name[i].value.replace(/ /g,'') + "=" + param_value[i].value.replace(/ /g,'') + "&";
    }
    test=test.substring(0,test.length-1);
    url = request_link + "?" + test;

    $.ajax({
        url: url,
        dataType: "json",
        success: function(data) {
            $("#responsedata").html("");
            $("#responsedata").html(JSON.stringify(data));
        }
    });
}

//$(document).ready(function () {
//    $("#interfacelist li").click(function () {
//        var url = $(this).find('a').attr('href');
//        $.ajax({
//            url: url,
//            type: "get",
//            dataType: "text",
//            success: function (data) {
//                $("#responsedata").html(data);
//            },
//            async: false,
//        });
//    });
//});

