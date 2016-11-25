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
                            $('.sidenav-dropdown' + projectid).append("<li><a href='/testtools/interface/detail/" + data[i].pk + "/'>\
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
