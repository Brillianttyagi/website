$('#notification').length && $.getJSON("/communication/notification/?page=1",{},
    function (data_with_pagiantion, textStatus, jqXHR) {
        let nt=''
        data=data_with_pagiantion.results
        for(x in data){
            console.log(x)
            nt+='<div  class="notification_item d-flex align-items-center dropdown-item" href="" notification_id="'+data[x].id+'" style="font-weight:normal;'+(data[x].isReaded==false?"background-color: #eaecf4;":"")+'" >\
                    <div class="mr-3">\
                        <div class="icon-circle" style="background-color: #01011e;">\
                            <i class="fas fa-file-alt text-white"></i>\
                        </div>\
                    </div>\
                    <div style="display:inline;vertical-align:middle;">\
                        <span class="small text-gray-500"></span>\
                        <p style="display:inline;">'+data[x].message+'</p>\
                    </div>\
                    <div style="margin: auto;">\
                        <i class="fas fa-envelope"></i> \
                    </div>\
                </div>'
        }
        $('#notification')[0].innerHTML=nt
        console.log(data)
    }
);

$('#notification').on('click','.notification_item',(e)=>{
    let target = e.currentTarget
    target.style.backgroundColor='inherit'
    let id = target.getAttribute('notification_id')
    $.post("/communication/notification/"+id+"/markasread/");
})



$('#notification_markallasread').on('click',(e)=>{
   $.post("/communication/notification/markallasread/");
})