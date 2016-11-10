/**
 * Created by gutongjie on 2016/10/19.
 */
function getInterfaceList(categoryid){
    $.ajax({url: "http://localhost:8000/testtools/interface/list/ajax/" + categoryid, type: "get", dataType: "json",
                success: function(data){
                    console.log(data);
                    $('.sidenav-dropdown'+categoryid).html("");
                    for (var i=0;i<data.length;i++){
                        $('.sidenav-dropdown'+categoryid).append("<li><a href='/testtools/interface/detail/"+data[i].pk+"/'>"+data[i].fields.interface_name+"</a></li>");
                    }
                },
                async: true,
            });
};
