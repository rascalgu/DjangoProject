/**
 * Created by gutongjie on 2016/10/19.
 */
function getInterfaceList(projectid){
    $.ajax({url: "http://localhost:8000/testtools/project/list/ajax/" + projectid, type: "get", dataType: "json",
                success: function(data){
                    console.log(data);
                    $('.sidenav-dropdown'+projectid).html("");
                    for (var i=0;i<data.length;i++){
                        $('.sidenav-dropdown'+projectid).append("<li><a href='/testtools/interface/detail/"+data[i].pk+"/'>\
                        "+data[i].fields.interface_sn+"\
                        "+data[i].fields.interface_name+"</a></li>");
                    }
                },
                async: true,
            });
};
